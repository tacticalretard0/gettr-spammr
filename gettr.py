import requests
import json

from time import time
from urllib.parse import quote as urlencode

from random import randint, choice

URL = "https://api.gettr.com/u/post"

default = {
    "data": {
        "udate": 0,

        "acl": {"_t": "acl"},

        "_t": None,

        "cdate": 0,

        "uid": None
    },

    "aux": None,
    "serial": None
}

class FakeResp():
    def __init__(self):
        self.status_code = 400
    def json(self):
        return {}

def header(auth):

    return {

        "x-app-auth": json.dumps({
            "user": auth["name"].lower(),
            "token": auth["token"]
        }),

        "x-app-url": "https://gettr.com"
    }

def post(auth, message): 
    unix_time = int(time())

    data = default.copy()

    data["data"]["udate"] = unix_time
    data["data"]["cdate"] = unix_time
    data["data"]["uid"] = auth["name"].lower()
    data["data"]["txt"] = message
    data["data"]["_t"] = "post"
    data["serial"] = "post"

    data = json.dumps(data)

    url = "https://api.gettr.com/u/post"

    return requests.post(url, headers=header(auth), files={
        "content": (None, data)
    })

def like(auth, pid):
    name = auth["name"].lower()

    url = f"https://api.gettr.com/u/user/{urlencode(name)}/likes/post/{urlencode(pid)}"

    # {"content":{"text":""}}
    data = "{\"content\":{\"text\":\"\"}}"

    try:
        return requests.post(url, data=data, headers=header(auth))
    except:
        return FakeResp()

def unlike(auth, pid):
    name = auth["name"].lower()

    url = f"https://api.gettr.com/u/user/{urlencode(name)}/unlike/post/{urlencode(pid)}"

    # {"content":{"text":""}}
    data = "{\"content\":{\"text\":\"\"}}"

    return requests.post(url, data=data, headers=header(auth))

def repost(auth, pid):
    name = auth["name"].lower()

    url = f"https://api.gettr.com/u/user/{urlencode(name)}/shares/post/{urlencode(pid)}"

    # {"content":{"text":""}}
    data = "{\"content\":{\"text\":\"\"}}"

    try:
        return requests.post(url, data=data, headers=header(auth))
    except:
        return FakeResp()

def unrepost(auth, pid):
    name = auth["name"].lower()
    
    url = f"https://api.gettr.com/u/user/{urlencode(name)}/shares/post/{urlencode(pid)}"
    
    # {"content":{}}
    data = "{\"content\":{}}"

    return requests.delete(url, data=data, headers=header(auth))

def quote(auth, pid, message):
    unix_time = int(time())

    data = default.copy()

    data["data"]["udate"] = unix_time
    data["data"]["cdate"] = unix_time
    data["data"]["uid"] = auth["name"].lower()
    data["data"]["txt"] = message

    data["data"]["rpstIds"] = [pid]
    data["data"]["_t"] = "post"
    data["serial"] = "post"

    data = json.dumps(data)

    url = "https://api.gettr.com/u/repost"

    try:
        return requests.post(url, headers=header(auth), files={
            "content": (None, data)
        })
    except:
        return FakeResp()

def reply(auth, pid, message):

    unix_time = int(time())

    data = default.copy()

    data["data"]["udate"] = unix_time
    data["data"]["cdate"] = unix_time
    data["data"]["uid"] = auth["name"].lower()
    data["data"]["txt"] = message
    
    data["data"]["pid"] = pid
    data["data"]["_t"] = "cmt"
    data["serial"] = "cmt"

    data = json.dumps(data)

    url = f"https://api.gettr.com/u/post/{urlencode(pid)}/comment"

    try:
        return requests.post(url, headers=header(auth), files={
            "content": (None, data)
        })
    except:
        return FakeResp()

def follow(auth, user):
    
    name = auth["name"].lower()

    url = f"https://api.gettr.com/u/user/{urlencode(name)}/follows/{urlencode(user)}"


    # {"content":{}}
    data = "{\"content\":{}}"

    try:
        return requests.post(url, data=data, headers=header(auth))
    except:
        return FakeResp()

def unfollow(auth, user):
    
    name = auth["name"].lower()

    url = f"https://api.gettr.com/u/user/{urlencode(name)}/unfollows/{urlencode(user)}"

    # {"content":{}}
    data = "{\"content\":{}}"

    return requests.post(url, data=data, headers=header(auth))

def get_user_posts(user, offset=0, _max=20):
    url = f"https://api.gettr.com/u/user/{urlencode(user)}/posts"

    params = {"offset": offset, "max": _max, "fp": "f_uo"}

    try:
        return requests.get(url, params=params)
    except:
        return FakeResp()

def get_post_info(pid):

    url = f"https://api.gettr.com/u/post/{urlencode(pid)}/?incl=\"poststats|userinfo\""

    try:
        return requests.get(url)
    except:
        return FakeResp()

def get_comment_info(cid):

    url = f"https://api.gettr.com/u/comment/{urlencode(cid)}/?incl=\"commentstats|userinfo|posts|poststats\""

    try:
        return requests.get(url)
    except:
        return FakeResp()

def get_post_html(pid):

    url = f"https://gettr.com/post/{urlencode(pid)}"

    return requests.get(url)

def get_trending(_max=20):

    url = "https://api.gettr.com/s/hashtag/suggest"

    try:
        return requests.get(url, params={"max": _max})
    except:
        return FakeResp()

def signup(email, token):
    url = "https://api.gettr.com/s/verifycode/email"

    header = {
        "x-app-auth":
            json.dumps({
                "user": None,
                "token": None
            })
    }

    data = {
            "email": email,
            "lang": "en",
            "reqtype": "signup",
            "token": token
    }

    return requests.post(url, json=data, headers=header)

def random_pid(minlen=3, maxlen=5):

    pid = "p"

    for c in range( randint(minlen, maxlen) ):
        if randint(0, 1):
            pid += choice("abcdefghijklmnopqrstuvwxyz")
        else:
            pid += choice("123456789")

    return pid

def random_cid(minlen=3, maxlen=5):

    cid = list( random_pid(minlen, maxlen) )
    cid[0] = 'c'
    return "".join(cid)

def post_valid(post_dict):
    data = {}
    try:
        data = post_dict["result"]["data"]

        txt = data["txt"]
        if txt == "Content Not Found":
            return False

        if data is not None and data.get("nfound"):
            return False

    except KeyError:
        return False

    return True

def random_comment(minlen=3, maxlen=5):
    cid = random_cid(minlen, maxlen)

    resp = get_comment_info(cid)

    if post_valid(resp.json()):
        return cid, resp

    while True:
        cid = random_cid()
        resp = get_comment_info(cid)
        if post_valid(resp.json()):
            return cid, resp

def random_post(minlen=3, maxlen=5):
    pid = random_pid(minlen, maxlen)

    resp = get_post_info(pid)

    if post_valid(resp.json()):
        return pid, resp

    while True:
        pid = random_pid()
        resp = get_post_info(pid)
        if post_valid(resp.json()):
            return pid, resp

def get_post_author(post_dict):
    try:
        return post_dict["result"]["data"]["uid"]
    except KeyError:
        return None

def random_user(minlen=3, maxlen=5):
    _, post = random_post(minlen, maxlen)
    return get_post_author(post.json())

def get_post_hashtags(post_dict):
    try:
        return post_dict["result"]["data"]["htgs"]
    except KeyError:
        return None
