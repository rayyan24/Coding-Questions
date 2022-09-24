import os
files=[file for file in os.listdir() if file.endswith(".png")]
with open("list.txt","w") as file:
    for i in files:
        i=i.removesuffix(".png")
        file.write(f"{i}\n")