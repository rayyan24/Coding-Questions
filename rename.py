from PIL import Image
import pyautogui as auto
import os 
import time 

# im = Image.open(r"70 Climbing Stairs.png")

# im.show()
# auto.hotkey('alt','f4')
# os.rename("Screenshot 000124.png","13 Roman To Integer.png")
def rename():
    Files=[file for file in os.listdir() if file.startswith("Screenshot")]
    for curImg in Files:
        im = Image.open(curImg)
        im.show()
        newName=input("Enter New Name: ").title()
        newName+=".png"
        try:
            os.rename(curImg,newName)
        except Exception as e:
            print("File Exist")
        auto.hotkey('alt','tab')
        auto.hotkey('alt','f4')
def main():
    rename()
if __name__=="__main__":
    main()
        