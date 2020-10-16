# agogf-bot
The bot for the "A Group of Good Friends" discord.
README last updated: 10/16/2020
This bot was originally just a fun project to assist with new people joining the group, but it has eventually turned into a multi-function bot to assist with a lot of the games we play and to assist with organization.

    PRIMARY DUTIES OF THE BOT;
1. When a new member joins, they will be given a unique role, a unique channel, and a message greeting them to give them a sort of run-down of what the discord is about. They can choose to talk to the few people who have permission to the channel, rather than the hundreds of people who already exist. They're also given very limited permissions and can only receive more by manually having their roles changed in discord itself.
2. When a person leaves, the bot notifies the 'officers' of who left and deletes their unique role and channel combination for automatic clean-up. 
3. Provide a ton of commands for Quality-of-Life improvements across various games the group plays - Like for people who don't mute their microphone during Among Us (Looking at you, Chris.)


    GETTING THIS BOT OPERATIONAL ON YOUR SERVER;

A. Create an environment file with the following variables declared:

    DISCORDTOKEN= (The bot's token as displayed on the discord developer portal)
    OWNER= (The full screen name of the person you want to be able to execute some of the sensitive commands INCLUDING the pound sign. Something like JohnDoes#1234)
    RAID_CHANNEL= (Whatever channel is used primarily for your raiding channel)
    AMONGUS_CHANNEL= (Whatever channel is used primarily for your Among Us channels)
    OFFICER_CHANNEL= (Whatever channel is used for your private officer chat.)

B. Fill out the greeting you would like to have when a stranger joins your discord in the discord.py file. This is currently redacted from this repo.

    CURRENT PLANS;

The following commands are not-yet implemented, though planned:
    $token - Fetch the price of a token in US.
    $rio [player] - Fetch the general raider.io score of a character.
    $m+ - Fetches the affixes for the week in the US.
    $privchan - Create a private test channel between the author and officers.
    Figure out music-playing capabilities over voice chat. 

A lot of us are thinking of fun little ideas just to make this a challenging bot to expand upon, such as:
    $weather [zipcode] - Fetch the weather/forecast by zip code
    $dhealth - Look up the health/status of discord servers
But these are relatively lower on the priority list. 

