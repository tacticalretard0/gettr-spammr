from random import randint
from time import sleep

import util
import gettr

# ----=== likebot ===----
# finds random posts and likes them

likebot_delay = (150, 550) # 100 450
like_amount = 10 # 8
likebot_output = True

def likebot(auth):
    name = auth["name"]
    while True:
        rl = False
        for i in range(like_amount):
            pid, _ = gettr.random_post()

            resp = gettr.like(auth, pid)

            if resp.status_code == 429:
                rl = True
                break
            if resp.status_code != 200:
                continue
            elif likebot_output:
                print(f"{name} likes {pid}")
        if rl:
            util.rl(auth, "likebot")
            break

        if likebot_output:
            util.green(f"{name}: likebot done with cycle")

        sleep( randint( likebot_delay[0], likebot_delay[1] ) )

