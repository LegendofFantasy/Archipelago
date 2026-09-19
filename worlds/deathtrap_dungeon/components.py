from worlds.LauncherComponents import Component, Type, components, launch

def run_client(*args: str) -> None:
    from .client import launch_deathtrap_dungeon_client

    launch(launch_deathtrap_dungeon_client, name="Deathtrap Dungeon Client", args=args)

components.append(
    Component(
        "Deathtrap Dungeon Client",
        func=run_client,
        game_name="Deathtrap Dungeon",
        component_type=Type.CLIENT,
    )
)
