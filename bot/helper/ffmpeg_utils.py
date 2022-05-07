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

eni = basefilepath.split("/")[-1]
xnx = eni.split(".")[-1]
nam = opm.replace("_", " ")
nam = opm.replace(".", " ")

anitopy_options = {'allowed_delimiters': ' '}
aysnc def encode(filepath):
    basefilepath, extension = os.path.splitext(filepath)
    output_filepath = basefilepath + '.mkv'
    
def get_duration(filepath):
    metadata = extractMetadata(createParser(filepath))
    if metadata.has("duration"):
      return metadata.get('duration').seconds
    else:
      return 0

def get_width_height(filepath):
    metadata = extractMetadata(createParser(filepath))
    if metadata.has("width") and metadata.has("height"):
      return metadata.get("width"), metadata.get("height")
    else:
      return 1280, 720
