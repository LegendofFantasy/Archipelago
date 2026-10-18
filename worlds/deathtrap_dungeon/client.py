# Most of this code is sourced from the League of Legends APWorld found at: https://github.com/gaithernOrg/LoLAP and
# has been edited to fit the needs of this project.

from __future__ import annotations
import os
import sys
import asyncio
import shutil
import requests
import json

import ModuleUpdate
ModuleUpdate.update()

import Utils

from worlds.deathtrap_dungeon.world import DeathtrapDungeonWorld

check_num = 0

###Set up game communication path###
if "localappdata" in os.environ:
    game_communication_path = os.path.expandvars(r"%localappdata%/AP Fighting Fantasy/Deathtrap Dungeon")
    game_cache_path = os.path.expandvars(r"%localappdata%/AP Fighting Fantasy/cache")
else:
    game_communication_path = os.path.expandvars(r"$HOME/AP Fighting Fantasy/Deathtrap Dungeon")
    game_cache_path = os.path.expandvars(r"$HOME/AP Fighting Fantasy/cache")
if not os.path.exists(game_communication_path):
    os.makedirs(game_communication_path)
if not os.path.exists(game_cache_path):
    os.makedirs(game_cache_path)

###Client###
if __name__ == "__main__":
    Utils.init_logging("DeathtrapDungeonClient", exception_logger="Client")

from NetUtils import NetworkItem, ClientStatus
from CommonClient import logger, get_base_parser, ClientCommandProcessor, \
    server_loop

tracker_loaded = False
try:
    from worlds.tracker.TrackerClient import (TrackerGameContext as SuperContext,
                                              TrackerCommandProcessor as SuperCommandProcessor)
    tracker_loaded = True
except ModuleNotFoundError:
    from CommonClient import (CommonContext as SuperContext,
                              ClientCommandProcessor as SuperCommandProcessor)

try:
    from Utils import gui_enabled
except ImportError:
    from CommonClient import gui_enabled


def check_stdin() -> None:
    if Utils.is_windows and sys.stdin:
        print("WARNING: Console input is not routed reliably on Windows, use the GUI instead.")

class DeathtrapDungeonCommandProcessor(SuperCommandProcessor):
    pass

class DeathtrapDungeonContext(SuperContext):
    command_processor: int = DeathtrapDungeonCommandProcessor
    game = "Deathtrap Dungeon"
    tags = {"AP"}
    items_handling = 0b111  # full remote

    def __init__(self, server_address, password):
        super(DeathtrapDungeonContext, self).__init__(server_address, password)
        self.scouts_seed = ""
        self.send_index: int = 0
        self.syncing = False
        self.awaiting_bridge = False
        # self.game_communication_path: files go in this path to pass data between us and the actual game
        if "localappdata" in os.environ:
            self.game_communication_path = os.path.expandvars(r"%localappdata%/AP Fighting Fantasy/Deathtrap Dungeon")
            self.game_cache_path = os.path.expandvars(r"%localappdata%/AP Fighting Fantasy/cache")
        else:
            self.game_communication_path = os.path.expandvars(r"$HOME/AP Fighting Fantasy/Deathtrap Dungeon")
            self.game_cache_path = os.path.expandvars(r"$HOME/AP Fighting Fantasy/cache")
        if not os.path.exists(self.game_communication_path):
            os.makedirs(self.game_communication_path)
        if not os.path.exists(self.game_cache_path):
            os.makedirs(self.game_cache_path)
        for root, dirs, files in os.walk(self.game_communication_path):
            for file in files:
                if file.find("obtain") <= -1:
                    os.remove(root+"/"+file)

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(DeathtrapDungeonContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def connection_closed(self):
        await super(DeathtrapDungeonContext, self).connection_closed()
        for root, dirs, files in os.walk(self.game_communication_path):
            for file in files:
                if file.find("obtain") <= -1:
                    os.remove(root + "/" + file)

    @property
    def endpoints(self):
        if self.server:
            return [self.server]
        else:
            return []

    async def shutdown(self):
        await super(DeathtrapDungeonContext, self).shutdown()
        for root, dirs, files in os.walk(self.game_communication_path):
            for file in files:
                if file.find("obtain") <= -1:
                    os.remove(root+"/"+file)

    def on_package(self, cmd: str, args: dict):

        super().on_package(cmd, args)

        if cmd in {"RoomInfo"}:
            if not self.scouts_seed:
                self.scouts_seed = args["seed_name"]

        if cmd in {"Connected"}:
            if not os.path.exists(self.game_communication_path):
                os.makedirs(self.game_communication_path)
            for ss in self.checked_locations:
                filename = f"send{ss}"
                with open(os.path.join(self.game_communication_path, filename), 'w') as f:
                    f.close()
            #Handle Slot Data
            for slot_data_key in list(args['slot_data'].keys()):
                with open(os.path.join(self.game_communication_path, slot_data_key.replace(" ", "_") + ".cfg"), 'w') as f:
                    f.write(str(args['slot_data'][slot_data_key]))
                    f.close()
            #End Handle Slot Data
            with open(os.path.join(self.game_communication_path, "scouts"), 'a') as f:
                f.write(f"{self.scouts_seed}_{self.slot}")
                f.close()
            
        if cmd in {"ReceivedItems"}:
            start_index = args["index"]
            if start_index != len(self.items_received):
                for item in args['items']:
                    check_num = 0
                    for filename in os.listdir(self.game_communication_path):
                        if filename.startswith("AP"):
                            if int(filename.split("_")[-1].split(".")[0]) > check_num:
                                check_num = int(filename.split("_")[-1].split(".")[0])
                    item_id = ""
                    location_id = ""
                    player = ""
                    found = False
                    for filename in os.listdir(self.game_communication_path):
                        if filename.startswith(f"AP"):
                            with open(os.path.join(self.game_communication_path, filename), 'r') as f:
                                item_id = str(f.readline()).replace("\n", "")
                                location_id = str(f.readline()).replace("\n", "")
                                player = str(f.readline()).replace("\n", "")
                                if str(item_id) == str(NetworkItem(*item).item) and str(location_id) == str(NetworkItem(*item).location) and str(player) == str(NetworkItem(*item).player) and int(location_id) > 0:
                                    found = True
                    if not found:
                        filename = f"AP_{str(check_num+1)}.item"
                        with open(os.path.join(self.game_communication_path, filename), 'w') as f:
                            f.write(str(NetworkItem(*item).item) + "\n" + str(NetworkItem(*item).location) + "\n" + str(NetworkItem(*item).player))
                            f.close()

        if cmd in {"RoomUpdate"}:
            if "checked_locations" in args:
                for ss in self.checked_locations:
                    filename = f"send{ss}"
                    with open(os.path.join(self.game_communication_path, filename), 'w') as f:
                        f.close()

        if cmd in {"LocationInfo"}:
            scouts = {}
            for location in self.locations_info:
                scouts[location] = {
                    "item" : self.item_names.lookup_in_slot(
                        self.locations_info[location].item, self.locations_info[location].player),
                    "player" : self.player_names[self.locations_info[location].player],
                    "flags" : self.locations_info[location].flags
                }
            with open(os.path.join(self.game_cache_path, f"{self.scouts_seed}_{self.slot}"), 'w') as f:
                f.write(json.dumps(scouts))
                f.close()

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = "Archipelago Deathtrap Dungeon Client"
        return ui

async def game_watcher(ctx: DeathtrapDungeonContext):
    while not ctx.exit_event.is_set():
        if ctx.syncing == True:
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        sending = []
        hints = []
        victory = False
        request_scouts = False
        for root, dirs, files in os.walk(ctx.game_communication_path):
            for file in files:
                if file.find("send") > -1:
                    st = file.split("send", -1)[1]
                    if st != "nil":
                        sending = sending+[(int(st))]
                if file.find("hint") > -1:
                    st = file.split("hint", -1)[1]
                    if st != "nil":
                        hints = hints+[(int(st))]
                    os.remove(root + "/" + file)
                if file.find("victory") > -1:
                    victory = True
                    os.remove(root + "/victory")
                if file.find("request_scouts") > -1:
                    request_scouts = True
                    os.remove(root + "/request_scouts")
        ctx.locations_checked = sending
        await ctx.check_locations(sending)
        message = []
        if hints:
            message.append({"cmd": "CreateHints", "locations": hints})
        if request_scouts:
            message.append({"cmd": "LocationScouts", "locations": list(ctx.server_locations)})
        if message:
            await ctx.send_msgs(message)
        if not ctx.finished_game and victory:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True
        await asyncio.sleep(0.1)


def launch_deathtrap_dungeon_client():
    async def main(args):
        ctx = DeathtrapDungeonContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if tracker_loaded:
            ctx.run_generator()
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        progression_watcher = asyncio.create_task(
            game_watcher(ctx), name="DeathtrapDungeonProgressionWatcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await progression_watcher

        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="Deathtrap Dungeon Client, for text interfacing.")

    args, rest = parser.parse_known_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()
