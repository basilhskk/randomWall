from win32api import GetSystemMetrics
import ctypes
import requests
import os 


#Constants 
SPI_SETDESKWALLPAPER = 20 
#get width and height
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

dirLocation = os.path.realpath(__file__).replace("\changeWallpaper.py","")
imgLocation = os.path.join(dirLocation, "tmp.jpg")


def download_random():
    
    img = "https://picsum.photos/{0}/{1}".format(width,height)
    
    r = requests.get(img)
    with open(imgLocation ,"wb")as f:
        for chunk in r:
            f.write(chunk)


if __name__ == "__main__":
    download_random()
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, imgLocation, imgLocation , 3) # set last value to 0 if you don't want to make wallpaper permament
    print("Wallpaper Changed!")
    os.remove(imgLocation)