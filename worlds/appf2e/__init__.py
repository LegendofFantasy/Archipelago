from worlds.LauncherComponents import Component, Type, components, launch

from .world import APPF2eWorld as APPF2eWorld

def run_client(*args: str) -> None:
    from .client import launch_ap_pf2e_client

    launch(launch_ap_pf2e_client, name="AP Pathfinder 2e Client", args=args)


components.append(
    Component(
        "AP Pathfinder 2e Client",
        func=run_client,
        game_name="AP Pathfinder 2e",
        component_type=Type.CLIENT,
    )
)
