#!/usr/bin/env python
# bots/tweet.py


import tweepy
import logging
from source import sourceimg
from config import create_api
import time
import glob
import random
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def postKasumi(api):
    logger.info("Generating image...")
    randomNum = random.randint(0,len(sourceimg)-1)
    logger.info("Uploading image...")
    api.update_status("#P5R " + sourceimg.get(randomNum))
    logger.info("Done!")

def main():
    api = create_api()
    postKasumi(api)
    logger.info("Waiting...")


if __name__ == "__main__":
    main()
