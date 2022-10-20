import os 
files=os.listdir()
emptyFiles=[]
for file in files:
    with open(file,"r") as currentFile:
        if currentFile.read()=="":
            emptyFiles.append(file)
emptyFiles.sort()
with open("EmptyFiles.txt","w") as file:
    for i in emptyFiles:
        name=str(i).removesuffix('.py')
        file.write(f'{name}\n')