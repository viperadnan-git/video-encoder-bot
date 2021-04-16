from pyrogram import filters
from bot import app, data, sudo_users
from bot.helper.utils import add_task

@app.on_message(filters.incoming & filters.command(['start', 'help']))
def help_message(app, message):
    message.reply_text(f"Hi {message.from_user.mention()}\nI can encode Telegram files in x265, just send me a video.")

@app.on_message(filters.user(sudo_users) & filters.incoming & filters.video)
def encode_video(app, message):
    message.reply_text("```Added to queue...```")
    data.append(message)
    if len(data) == 1:
      add_task(message)

app.run()