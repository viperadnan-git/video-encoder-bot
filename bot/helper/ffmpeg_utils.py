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

aysnc def encode(filepath):
    basefilepath, extension = os.path.splitext(filepath)
    eni = filepath.split("/")[-1]
    xnx = eni.split(".")[-1]
    nam = opm
    nam = opm.replace("_", " ")
    nam = opm.replace(".", " ")
    nam = nam + '.mkv'
    
    
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
