with open("list.txt",'r') as file:
    list=file.read().split("\n")
    for name in list:
        name+=".py"
        open(name,"w")