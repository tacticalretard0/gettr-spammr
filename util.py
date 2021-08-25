import sys

from random import randint, choice

import gettr

# wrapper for gettr.follow, provides output
def follow(auth, user, output=True):
    name = auth["name"]

    resp = gettr.follow(auth, user)
    if resp.status_code == 200 and output:
        #pass
        print(f"{name} follows {user}")

    return resp

def red(text):
    print(f"\033[91m{text}\033[0m")

def green(text):
    print(f"\033[92m{text}\033[0m")

def rl(auth, threadname):
    name = auth["name"]
    red(f"{name}: {threadname} ratelimited, stopping thread")

# replace {?} with a random character
def randchar(string):
    return string.replace("{?}", choice("abcdefghijklmnopqrstuvwxyz"))

def parsefile(fname):
    result = []
    with open(fname, "r") as f:
        for line in f:
            if line != '\n' and line[0] != '#':
                result.append(randchar(line.strip()))
    return result

hashtags = parsefile("hashtags.txt")
trends   = parsefile("trends.txt")

replies  = parsefile("replies.txt")
quotes   = parsefile("quotes.txt")

ats      = parsefile("ats.txt")

def update_resource(resource, data, output):
    arr = []
    if resource == "hashtags.txt":
        arr = hashtags
    if resource == "trends.txt":
        arr = trends
    if resource == "replies.txt":
        arr = replies
    if resource == "quotes.txt":
        arr = quotes

    dif = set(data) - set(arr)

    if output:
        print(f"writing {dif} to {resource}")

        with open(resource, "a") as f:
            for item in dif:
                f.write('\n' + item)
                arr.append(item)

def get_hashtags():
    return hashtags

def get_trends():
    return trends

def get_replies():
    return replies

def get_quotes():
    return quotes

def get_ats():
    return ats

def generate_hashtag():
    return '#' + randchar(choice(hashtags))

def generate_texthashtags():

    res = ""

    if randint(0, 10) == 10:
        res = generate_hashtag() + " "
    else:
        if randint(0, 100) > 97:

            for i in range( randint(0, 100) ):
                end = " "
                if randint(0, 10) > 3:
                    end = '\n'
                res += generate_hashtag() + end
        else:        
            for i in range( randint(0, 5) ):
                end = " "
                if randint(0, 10) > 4:
                    end = '\n'
                res += generate_hashtag() + end

    return res


def generate_text(which):
    resource = []
    if which == "quotes":
        resource = get_quotes()
    elif which == "replies":
        resource = get_replies()

    trends = get_trends()

    res = ""

    if randint(0, 30) > 25:
        if randint(0, 10) > 7:
            res = choice(trends) + " "
        else:
            res = choice(resource) + " "

    else:
        for i in range( randint(1, 10) ):
 
            end = " "
            if randint(0, 10) > 7:
                end = '\n'
            
            if randint(0, 10) > 8:
                res += choice(trends)
            else:
                res += choice(resource)

            if randint(0, 15) > 11:

                punctuation = choice(".,?!")
                if punctuation in ".?!":
                    res += punctuation * randint(0, 5)
                else:
                    res += punctuation

            res += end

    return res

def is_int(val):
    try:
        int(val)
    except ValueError:
        return False
    return True


