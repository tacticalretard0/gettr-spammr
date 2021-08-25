
from random import randint
from time import sleep

import util
import gettr

# ----=== followbot ===----
# follows a random user, then recursively follows users who they are following / follows them

followbot_output = True

followbot_maxdepth = 25  # 25
followbot_maxwidth = 15  # 15

followbot_delay  = (400, 900) # 400 900

def followbot_pathint_to_path(pathint):
    if pathint:
        return "following"
    else:
        return "followers"

def followbot_search(auth, client, user, visited, depth=0):

    if depth == followbot_maxdepth:
        return

    name = auth["name"]

    pathint = randint(0, 1)

    try:
        for related in client.user_relationships(user, max=followbot_maxwidth, type=followbot_pathint_to_path(pathint) ):
            related = related["username"]

            if (related, pathint) not in visited and related != name.lower():
                visited.add( (related, pathint) )
                resp = util.follow(auth, related, followbot_output)

                if resp.status_code == 429:
                    return "rl"

                return followbot_search(auth, client, user, visited, depth+1)

    except: pass

    return "win"


def followbot(auth, client):
    name = auth["name"]
    while True:
        user = gettr.random_user()
 
        result = followbot_search(auth, client, user, set())

        delay = randint(followbot_delay[0], followbot_delay[1])
        
        if result == "rl":
            util.rl(auth, "followbot")
            break
        elif result == "win" and followbot_output:
            util.green(f"{name}: followbot done with search")

        sleep(delay)


