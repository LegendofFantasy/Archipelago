from worlds.LauncherComponents import Component, Type, components, launch

def run_client(*args: str) -> None:
    from .client import launch_scorpion_swamp_client

    launch(launch_scorpion_swamp_client, name="Scorpion Swamp Client", args=args)

components.append(
    Component(
        "Scorpion Swamp Client",
        func=run_client,
        game_name="Scorpion Swamp",
        component_type=Type.CLIENT,
    )
)
