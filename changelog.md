# NearBot v0.7.2

1. Added the `move` command in the new Administration cog (as in [Issue 5](https://github.com/hirusha-adi/Near/issues/21))
    - moves users from one voice channel to another
    - from [SDS Autocrat](https://github.com/ThatRex/SDS-Autocrat/blob/main/src/commands/move.ts)
    - requested by Rex
2. Depend on the environment var `BOT_TOKEN` only and not on `token.txt`
    - `token.txt` will be useless from now on

# NearBot v0.7.1

1. Added logging using [`loguru`](https://github.com/Delgan/loguru) module
    - log to console
    - log to file (inside `./logs/`)

# NearBot v0.7

1. Reduced repeating code (try-except's large error embed)
2. Introduced a new way to handle embeds, reducing boilerplate code
3. Send requests asynchronously instead of `requests.get` like a skidder master
4. Give a uniform look to the error embed
5. Removed `bored` command due to [API](http://www.boredapi.com/api/activity) being down.
6. Removed `joke2`. Has only one `joke` command now. it depends on [this api](https://some-random-api.ml/joke)
7. Improved the code of the `/help` function. Made it easily customizable and extendable
8. Remove the country info command (`/countryinfo`). It's API is a joke.
9. Remove covid info command (`/covid`). Feels outdated in  2024.
10. Fixed broken embeds in `/passwordchk` command and made the code much better.
11. Fixed the broken `/lyrics` command
12. Fix the bug where the the `.env` file won't load
13. Other minor bug fixes
14. Removed the `setup.py` file for good. Use the guide in `README.md` to install it without docker. 
15. Update dependencies:
    - discord.py: `v2.3.2`
    - pomice: `v2.9.0`
    - lavalink: `v4.0.5` 

# NearBot v0.6

1. Add slash command support
2. Added interactive help commands
3. Using the latest versions of discord.py, wavelink and Lavalink
4. NOTE: Slash commands work except for music related commands <- This will be fixed in a future update
5. Made the code stable and better
6. Dockerized everything. Thank you `Rex#3572`


# NearBot v0.5

1. Seperate file for token (easy testing for developers, added the `token.txt` to `.gitignore`)
2. Grabify Link Detection
3. Bug fix in the command `--bottoken`
4. Has big issue with connecting to the locally hosted Lavalink server
5. Added steps to run the bot on both ubuntu(or any debian based distro) and arch(or any other arch based distro)

# NearBot v0.4

1. Better code
2. Organized code
3. Lavalink is configured locally in the server
4. Easy install and update scripts
5. Rewrote the `passwordcheck <password>` command and it is stable

# NearBot v0.3

1. Created a easy to develop folder structure
2. Usage of `json` as a database to store Common Values
3. Breaking the commands of `main.py` into seperate cogs in `near.cogs.*.py`

# NearBot v0.2

1. Music Commands with `wavelink` + lavalink (using http://lava.link:80)
2. Fun Commands
3. 100+ New commands to generate Fake Information + Fake Vehicle Info
4. Starting to use cogs for the bot (fakeinfo, music, fun)

# NearBot v0.1

1. The fist version of NearBot built for TeamSDS
