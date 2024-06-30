from random import random
import time as t
import json
import requests as r

from os import system

api_format = "https://api.bilibili.com/x/relation/followers?vmid={:d}"
fans = []
count = 0

with open("heads/1.json", "r") as f:
    head1 = json.load(f)

with open("list.txt", "r") as f:
    ups = f.read().split("\n")

with open("tmp.list", "r", encoding="utf-8") as f:
    fans = f.read().split("\n")

with open("tmp.list2", "r") as f:
    pointer = int(f.read())

lenth = len(ups)

#Inits

for i in range(pointer, lenth):

    try:
        print(ups[i])
        req = r.get(api_format.format(int(ups[i])), headers=head1)
        m = json.loads(req.text)

        for j in m["data"]["list"]:
            fans.append(j["uname"])
        
        #Normal

    except Exception as e:
        if m == {'code': -352, 'message': '-352', 'ttl': 1}:

            with open("tmp.list", "w", encoding="utf-8") as f:
                t = ""
                fans = list(set(fans))
                for j in fans[:-1]:
                    t += j + "\n"
                t += fans[-1]
                f.write(t)

            with open("tmp.list2", "w") as f:
                f.write(str(i))

            system("pause")
            exit(1)

        else:
            print(m)
        pass

    count += 1
    t.sleep(random()/3)
    #break


count += len(set(fans))
print()
fans = list(fans)
for f in fans:
    print(f)

print("\n共计", count, "人")

system("pause")