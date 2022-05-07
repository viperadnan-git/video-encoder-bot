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
      msg = message.reply_text("⬇️ **Downloading Video** ⬇️", quote=True)
      filepath = message.download(file_name=download_dir)
      msg.edit(f"**Encoding The Given File\n-->** ```{filepath}```")
      new_file, og = encode(filepath)
      if new_file:
        msg.edit("**⬆️ Video Encoded Starting To Upload ⬆️**")
        msg.edit("**⬆️ Uploading Video ⬆️**")
        message.reply_document(new_file, file_name=og, quote=True, force_document=True, caption=og)
        os.remove(new_file)
        msg.edit("**File Encoded**")
      else:
        msg.edit("**Error Contact @NIRUSAKIMARVALE**")
        os.remove(filepath)
    except MessageNotModified:
      pass
    except Exception as e:
      msg.edit(f"```{e}```")
    on_task_complete()
