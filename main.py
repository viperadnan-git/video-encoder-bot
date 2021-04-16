import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from ffmpeg_utils import encode, get_thumbnail, get_duration

if os.path.exists('config.env'):
  load_dotenv('config.env')

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
sudo_users = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)

@app.on_message(filters.user(sudo_users) & filters.incoming & filters.video)
def encode_video(app, message):
    try:
      msg = message.reply_text("```Downloading video...```", True)
      filepath = message.download(file_name=download_dir)
      msg.edit("```Encoding video...```")
      new_file = encode(filepath)
      msg.edit("```Uploading video...```")
      duration = get_duration(new_file)
      thumb = get_thumbnail(new_file, download_dir, duration / 4)
      message.reply_video(new_file, supports_streaming=True, thumb=thumb, duration=message.video.duration, width=message.video.width, height=message.video.height)
      msg.edit("```Video Encoded to x265```")
    except Exception as e:
      msg.edit(f"```{e}```")
    finally:
      try:
        if os.path.exists(filepath):
          os.remove(filepath)
        if os.path.exists(file_name):
          os.remove(new_file)
        if os.path.exists(thumb):
          os.remove(thumb)
      except:
        pass

app.run()