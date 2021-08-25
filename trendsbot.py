from time import sleep
from random import randint
from threading import Lock

import util
import gettr


# ----=== trendsbot ===----
# checks for new trending things
# finds random posts and saves their hashtags
# updates trends.txt and hashtags.txt with the data

trendsbot_delay = (10, 60) # 60 120
trendsbot_postcount = 10
trendsbot_output = True

def trendsbot():
    while True:
        trends = gettr.get_trending().json()

        trends = trends["result"]["data"]["list"]

        hashtags_to_save = []
        trends_to_save = []
        for trend in trends:
            if " " in trend:
                trends_to_save.append(trend.strip())
            else:
                hashtags_to_save.append(trend.strip())

        for i in range(trendsbot_postcount):
            _, resp = gettr.random_post()
            post_hashtags = gettr.get_post_hashtags(resp.json())
            if post_hashtags is not None:
                for h in post_hashtags:
                    hashtags_to_save.append(h.strip())

        print()
        util.update_resource("hashtags.txt", hashtags_to_save, trendsbot_output)
        util.update_resource("trends.txt", trends_to_save, trendsbot_output)
        print()

        sleep( randint( trendsbot_delay[0], trendsbot_delay[1] ) )

