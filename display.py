import os
from time import sleep
     
files=os.listdir("/home/pandaprafulla722")
if "chrome-remote-desktop_current_amd64.deb" not in files:
    os.system('''sudo apt update
curl -L -o chrome-remote-desktop_current_amd64.deb \
    https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb''')
    sleep(2)
os.system('''sudo DEBIAN_FRONTEND=noninteractive \
    apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb''')
sleep(2)
os.system('''sudo DEBIAN_FRONTEND=noninteractive \
    apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver''')
sleep(2)
os.system('''sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session''')
os.system('''sudo systemctl disable lightdm.service''')
sleep(2)
x= input("Enter your chrome ssh link :")
os.system('''sudo apt install firefox-esr''')
if(ask:=input("Did you want to download all suits"))=='yes':
    os.system('''sudo apt install --assume-yes task-xfce-desktop''')
else:
    print("Ok,connect to your ssh")
sleep(100)
os.system("clear")
os.system(x)
exit()
