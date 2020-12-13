import os 
import getpass


def add_to_startup(file_path=""):
    USER_NAME = getpass.getuser()
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "randomWall.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

if __name__ == "__main__":
    add_to_startup()