from random import randint, choice
from time import sleep

import util
import gettr

replybot_delay = (120, 800) # 120 800
replybot_output = True

def generate_reply():

    reply = ""
    for i in range( 1, randint(1, 5) ):
        if i % 2 != 0:
            reply += util.generate_text("replies")
        elif randint(0, 1):
            reply += util.generate_texthashtags()

    reply = reply.splitlines()

    for i, line in enumerate(reply):
        reply[i] = line.strip()

    reply = '\n'.join(reply)
    return reply[:777].strip()

def replybot(auth):
    name = auth["name"]
    while True:
        pcid = ""
        if randint(0, 1):
            pcid, _ = gettr.random_post()
        else:
            pcid, _ = gettr.random_comment()
 
        reply = generate_reply()

        resp = gettr.reply(auth, pcid, reply)

        if resp.status_code == 429:
            util.rl(auth, "replybot")
            break

        if resp.status_code == 200 and replybot_output:
            print(f"\n{name} replies to {pcid} with \"{reply}\"\n")

        sleep( randint( replybot_delay[0], replybot_delay[1] ) )

