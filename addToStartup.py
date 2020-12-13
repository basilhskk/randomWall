import os 
import getpass



def add_to_startup(file_path):
    USER_NAME = getpass.getuser()
   
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "randomWall.bat", "w+") as bat_file:
        bat_file.write(r'start python %s' % file_path)

if __name__ == "__main__":
    scriptLocation = os.path.realpath(__file__).replace("addToStartup.py","changeWallpaper.py")
    add_to_startup(scriptLocation)