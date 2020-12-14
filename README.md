# Random Wall

### Simple 30min python project

This script changes your wallpaper randomly


### Run 

Add it on startup 
``
python3 addToStartup.py
``

Run it 

``
python3 changeWallpaper.py
``

### Build 


```bash
pyinstaller --noconfirm --onefile --console --icon "./ico/wallpaper_settings_19647.ico"  "./changeWallpaper.py"
```