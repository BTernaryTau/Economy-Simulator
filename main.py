import os
from bot import run
from keepalive import keep_alive

def loop():
    try:
        run()
    except:
        loop()

keep_alive()

loop()