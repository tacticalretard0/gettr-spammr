from random import randint, choice
from time import sleep

import util
import gettr

quotebot_delay = (120, 800)
quotebot_output = True

def generate_quote():

    quote = ""
    for i in range( 1, randint(1, 5) ):
        if i % 2 != 0:
            quote += util.generate_text("quotes")
        elif randint(0, 1):
            quote += util.generate_texthashtags()

    quote = quote.splitlines()

    for i, line in enumerate(quote):
        quote[i] = line.strip()

    quote = '\n'.join(quote)
    return quote[:777].strip()

def quotebot(auth):
    name = auth["name"]
    while True:
        pid, _ = gettr.random_post()
 
        quote = generate_quote()

        resp = gettr.quote(auth, pid, quote)

        if resp.status_code == 429:
            util.rl(auth, "quotebot")
            break

        if resp.status_code == 200 and quotebot_output:
            print(f"\n{name} quotes {pid} with \"{quote}\"\n")

        sleep( randint( quotebot_delay[0], quotebot_delay[1] ) )

