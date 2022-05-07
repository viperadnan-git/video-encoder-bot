import asyncio
import os
import sys
import json
import anitopy
import time
from bot import ffmpeg
from subprocess import call, check_output
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

async def run_subprocess(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    return await process.communicate()

async def encode(filepath):
    basefilepath, extension = os.path.splitext(filepath)
    eni = filepath.split("/")[-1]
    xnx = eni.split(".")[-1]
    nam = opm
    nam = opm.replace("_", " ")
    nam = opm.replace(".", " ")
    nam = nam + '.mkv'
    new_name = anitopy.parse(nam)
    anime_name = new_name["anime_title"]
    joined_string = f"[{anime_name}]"
    if "anime_season" in new_name.keys():
      animes_season = new_name["anime_season"]
      joined_string = f"{joined_string}" + f" [Season {animes_season}]"
    if "episode_number" in new_name.keys():
      episode_no = new_name["episode_number"]
      joined_string = f"{joined_string}" + f" [Episode {episode_no}]"
    og = joined_string + " [@R136a1Encodes]" + ".mkv"
    output_filepath = og
    ffmpeg_cmd = f"ffmpeg -i {filepath} -map 0 -c:s copy {output_filepath} -y"
    run_subprocess(ffmpeg_cmd)
    os.remove(filepath)
    return output_filepath, og


async def get_thumbnail(filepath):
    screenshot_cmd = f'ffmpeg -i  {filepath} -ss 00:30 -vframes=1 "/bot/thumb.jpg" -y'
    run_subprocess(screenshot_cmd)
  
async def get_duration(filepath):
    metadata = extractMetadata(createParser(filepath))
    if metadata.has("duration"):
      return metadata.get('duration').seconds
    else:
      return 0

async def get_width_height(filepath):
    metadata = extractMetadata(createParser(filepath))
    if metadata.has("width") and metadata.has("height"):
      return metadata.get("width"), metadata.get("height")
    else:
      return 1280, 720
