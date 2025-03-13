import webbrowser
from vars import *

with open(f"{data_dir}user_to_sort.json","r") as f:
    lines = [line.rstrip() for line in f]


for link in lines:
        webbrowser.open(link)
        print(link)
        ans = input("Gut?: ")

        if ans == "y":
            chapter = input("Chapter: ")
            with open("sorted.txt","a") as file:
                file.write(f"{chapter}:{link}\n")

open(f"{data_dir}user_to_sort.json","w").close()
