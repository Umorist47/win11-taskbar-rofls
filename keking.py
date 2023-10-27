#hellniki
import winreg
import time

keyValue = r'Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced'
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER , keyValue, access=winreg.KEY_SET_VALUE)

while True:
    winreg.SetValueEx(key , 'TaskbarAl',0, winreg.REG_DWORD , 0x00000001)
    #winreg.CloseKey(key)
    time.sleep(0.3)
    winreg.SetValueEx(key , 'TaskbarAl',0, winreg.REG_DWORD , 0x00000000)
    #winreg.CloseKey(key)
    time.sleep(0.3)