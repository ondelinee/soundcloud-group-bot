# SoundCloud Group Bot

![logo](https://raw.githubusercontent.com/Monsterovich/soundcloud-group-bot/master/scgb.png)

# Project branches

- `stable` - tested and working version of the bot (recommended)
- `master` - beta and lastest version

# What you need:
- [Python 3.5](https://www.python.org/downloads/)
- open admin terminal (Windows: right click cmd.exe -> "Run as administrator")
- type the command `pip3 install requests`

# How to set up your own group:

- Create an account that will be your group page.
- Upload an empty soundtrack where users can post their links.
- Get an API key (http://soundcloud.com/you/apps/new).
- Edit these lines in `config.py`:

```Python
client_id='id_from_api_page'
client_secret='secret_code_from_api_page'
username='account_name'
password='account_password'
```

Run `script.cmd` (windows) or `script.sh` (linux). 

Example group: https://soundcloud.com/losttalentgroup
