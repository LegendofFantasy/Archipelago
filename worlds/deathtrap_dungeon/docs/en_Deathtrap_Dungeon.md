# Deathtrap Dungeon

## What is Deathtrap Dungeon?

Deathtrap Dungeon is a gamebook written by Ian Livingstone for Steve Jackson and Ian Livingstone's Fighting 
Fantasy series. It features the player entering the titular dungeon with the goal of reaching the end alive.

This implementation connects to a specialized companion app that facilitates communication with Archipelago and
automates statistic and inventory management, but you will still require a copy of the book.
For more details, read the [setup guide](setup_en.md).

## What is randomized in this game?

Each one of the locations within the game in which you find an item is a viable location for this game.

Beyond that, there are options to add extra locations at each of the game's bad endings, to add locations at the
beginning and shuffle some of the game's starting items, and to remove some of the characters from the game, thus
blocking anything that the player would need them for behind getting items that make them appear once again. Finally,
there's an option to make all the gems in the game necessary to obtain to reach the goal. The developer recommends
turning all of these options on as without them the game is fairly open and has fewer requirements for completion, but
feel free to mix and match as you desire. Playing without these options will give a nearly vanilla experience which
could be preferable for an initial playthrough.

Alongside adding additional locations there is also the option to add progressive statistics. These items increase the
base level of your Skill, Stamina, and Luck when your character is created at the beginning of each run by one (two in
the case of Stamina). So, for example, with three Progressive Skills your Skill will range from 10-12 rather than the
usual 7-12. Note that these items are never considered by logic; all battles are considered winnable and all statistic
checks passable with nothing. These items are just for convenience.

Logic may expect for you to fail statistic  checks (usually Tests of Luck); there is an option built into the
companion app that will make it so that you always fail ensuring that these are always accessible even if you have 
high stats. Logic, especially with -sanity settings on, will likely require you to restart the game at least once.
