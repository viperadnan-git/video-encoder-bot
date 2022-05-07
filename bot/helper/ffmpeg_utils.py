import asyncio
import os
import sys
import json
import time
import ffmpeg
from subprocess import call, check_output
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

def encode(filepath):
    basefilepath, extension = os.path.splitext(filepath)
    output_filepath = basefilepath + '.HEVC' + '.mp4'
    assert(output_filepath != filepath)
    if os.path.isfile(output_filepath):
        print('Skipping "{}": file already exists'.format(output_filepath))
        return None
    print(filepath)
    
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
