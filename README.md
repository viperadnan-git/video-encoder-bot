# Video Encoder Bot
A Telegram bot to convert videos into x265/x264 format via ffmpeg.

### Configuration
Add values in environment variables or add them in [config.env.template](./config.env.template) and rename file to `config.env`.
- `API_ID` - Get it by creating an app on [https://my.telegram.org](https://my.telegram.org)
- `API_HASH` - Get it by creating an app on [https://my.telegram.org](https://my.telegram.org)
- `BOT_TOKEN` - Get it by creating a bot on [https://t.me/BotFather](https://t.me/BotFather)
- `SUDO_USERS` - Chat identifier of the sudo user. For multiple users use space as seperator.
- `DOWNLOAD_DIR` - (Optional) Temporary download directory to keep downloaded files.

### Configuring Encoding Format
To change the ffmpeg profile edit them in [ffmpeg_utils.py](/bot/helper/ffmpeg_utils.py)

### Installing Requirements
Install the required Python Modules in your machine.
```sh
apt-get -qq install ffmpeg
pip3 install -r requirements.txt
```
### Deployment
With python3.7 or later.
```sh
python3 -m bot
```

### Credits
*Thanks to [ShannonScott](https://gist.github.com/ShannonScott) for [transcode_h265.py](https://gist.github.com/ShannonScott/6d807fc59bfa0356eee64fad66f9d9a8)*

### Copyright & License
- Copyright &copy; 2021 &mdash; [Adnan Ahmad](https://github.com/viperadnan-git)
- Licensed under the terms of the [GNU General Public License Version 3 &dash; 29 June 2007](./LICENSE)
