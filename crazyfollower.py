#!/usr/bin/env python3.9

import threading
import sys

import gogettr
import gettr

import util

import followbot


#name = "authorization"
threadcount = 15 # 12

argc = len(sys.argv)

if argc == 1:
    print("must provide name")
    sys.exit()

name = sys.argv[1]

if argc >= 3:
    if util.is_int(sys.argv[2]):
        threadcount = int(sys.argv[2])
    else:
        print(f"invalid threadcount, defaulting to {threadcount}")
else:
    print(f"no threadcount provided, defaulting to {threadcount}")

auth = {"name": name}
try:
    with open(f"tokens/token_{name}.txt", "r") as f:
        auth["token"] = f.read().strip()
except FileNotFoundError:
    print("invalid name")
    sys.exit()

client = gogettr.PublicClient()

# settings
if argc == 4:
    if util.is_int(sys.argv[3]):
        followbot.followbot_output = bool(int(sys.argv[3]))
    else:
        print("invalid output option, defaulting to enabled")
else:
    print("no output option, defaulting to enabled")
    followbot.followbot_output = True

followbot.followbot_delay = (0, 0)

followbot.followbot_maxwidth = 100
followbot.followbot_maxdepth = 100
###-###

threads = []
for i in range(threadcount):
    thr = threading.Thread(target=followbot.followbot, args=(auth, client))
    thr.setDaemon(True)
    threads.append(thr)

for thr in threads:
    thr.start()

for thr in threads:
    thr.join()

