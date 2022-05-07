import os
from bot import data, download_dir
import asyncio
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import MessageNotModified
from .ffmpeg_utils import encode, get_thumbnail

def on_task_complete():
    del data[0]
    if len(data) > 0:
      add_task(data[0])

def add_task(message: Message):
    try:
      msg = message.reply_text("```Downloading video...```", quote=True)
      filepath = message.download(file_name=download_dir)
      msg.edit("```Encoding video...```")
      new_file, og = encode(filepath)
      if new_file:
        msg.edit("```Video Encoded, getting metadata...```")
        thumb = get_thumbnail(filepath)
        msg.edit("```Uploading video...```")
        message.reply_document(new_file, quote=True, force_document=True, thumb="/bot/thumb.jpg", caption=og)
        os.remove(new_file)
        os.remove("/bot/thumb.jpg")
        msg.edit("```Video Encoded```")
      else:
        msg.edit("```Something wents wrong while encoding your file.```")
        os.remove(filepath)
    except MessageNotModified:
      pass
    except Exception:
        pass
    on_task_complete()
