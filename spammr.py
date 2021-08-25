import gogettr

import threading

from glob import iglob

import gettr

import followbot
import likebot
import trendsbot
import replybot
import quotebot

auths = []
for f in iglob("tokens/token_*.txt"):
    name = f.split("_")[1].replace(".txt", "")
    auth = {"name": name}
    with open(f, "r") as f2:
        auth["token"] = f2.read().strip()
    auths.append(auth)
"""
users = []
with open("ats.txt", "r") as f:
    for line in f:
        users.append(line.strip())
"""

client = gogettr.PublicClient()

threads = []
for auth in auths:

    t_followbot = threading.Thread(target=followbot.followbot, args=(auth, client))
    t_followbot.setDaemon(True)
    threads.append(t_followbot)

    t_likebot = threading.Thread(target=likebot.likebot, args=(auth,))
    t_likebot.setDaemon(True)
    threads.append(t_likebot)

    t_replybot = threading.Thread(target=replybot.replybot, args=(auth,))
    t_replybot.setDaemon(True)
    threads.append(t_replybot)

    t_quotebot = threading.Thread(target=quotebot.quotebot, args=(auth,))
    t_quotebot.setDaemon(True)
    threads.append(t_quotebot)

t_trendsbot = threading.Thread(target=trendsbot.trendsbot)
t_trendsbot.setDaemon(True)
threads.append(t_trendsbot)

for thr in threads:
    thr.start()
for thr in threads:
    thr.join()

