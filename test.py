import json

while True:
    
    f = input("File : ")

    with open(f, "r", encoding="utf-8") as file:
        t  = json.load(file)
    
    for i in range(len(t) - 1):
        t[i] += "\n"

    with open("tmp.list", "w", encoding="utf-8") as file:
        file.writelines(t)