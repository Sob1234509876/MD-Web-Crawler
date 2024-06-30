from random import random, randint
import time as t
import json
import requests as r

api_format = "https://api.bilibili.com/x/web-interface/search/all?keyword=%E6%97%A0%E6%9C%BA%E6%9D%80%E6%89%8B&search_type=video&page={:d}"
aids = []

with open("heads/2.json", "r") as f:
    head = json.load(f)

tmp = r.get(api_format.format(1), headers=head)
tmp.encoding = "utf-8"
lenth = json.loads(tmp.text)["data"]["numPages"]

print(lenth)

for i in range(1, lenth + 1):
    req = r.get(api_format.format(i), headers=head)
    req.encoding = "utf-8"

    try:
        vdos = json.loads(req.text)["data"]["result"]["video"]
        for v in vdos:
            aids.append(v["mid"])
    except Exception as e:
        print(e)

    t.sleep(random()/5)
    print(i)

aids = list(set(aids))
t = ""

for i in aids:
    print(i)
    t += str(i) + "\n"


with open("list.txt", "w") as f:
    f.write(t)

print("\n", len(aids))