# [ DEPRICATED WARNING ]
A newer version should be published sooner or later!

# discord-python-leveling-card

A repository to help you with your discord leveling card.

useable with discord.py or any other forks.


# example of generated card

<img src="https://raw.githubusercontent.com/ResetXD/discord-python-leveling-card/master/level.png">


# how to use


import
```py
from DiscordLeveling import level_maker
 ```
 
 and use
 ```py
 await level_maker(
    "background image url",
    "user avatar url",
    "username",
    int(current_experience),
    int(current_level),
    int(max_experience),
    bar_color_hex
    )
```
