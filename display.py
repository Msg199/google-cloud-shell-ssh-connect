import os
from time import sleep

user = input("Enter your user name : ")
files = os.listdir(f"/home/{user}/google-cloud-shell-ssh-connect")
if "chrome-remote-desktop_current_amd64.deb" not in files:
	os.system('''sudo apt update
curl -L -o chrome-remote-desktop_current_amd64.deb \
    https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb
		sudo DEBIAN_FRONTEND=noninteractive \
    apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb''')
	# to download the chrome remote desktop extension
	sleep(2)
else:
	# If extension was downloaded then run it
	os.system('''sudo apt update
sudo DEBIAN_FRONTEND=noninteractive \
    apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb''')
	sleep(2)

# To install xface4 screen envirement
os.system('''sudo DEBIAN_FRONTEND=noninteractive \
    apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver''')
sleep(2)
os.system(
 '''sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session'''
)
os.system('''sudo systemctl disable lightdm.service''')
sleep(2)

# to enter the remote desktop ssh link for linux
ssh = input("Enter your chrome ssh link :")
os.system(ssh)
browser = input(
 "What type of browser you like to install\n1.firefox\n2.chrome\n")
if (browser == "1"):
	os.system('''sudo apt install firefox-esr''')
elif (browser == "2"):
	os.system('''sudo apt install chromium''')
if (suit := input("Did you want to download all suits[y/n] \n")) == 'y':
	os.system('''sudo apt install --assume-yes task-xfce-desktop''')
else:
	print("Ok,connect to your ssh")
sleep(10)
os.system("clear")
print("All Done".center(50, "/"))
