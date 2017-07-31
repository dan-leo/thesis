###############################################################
Enable hostname on windows
###############################################################

$ sudo apt-get update

On the Raspberry Pi you need to install samba and winbind
$ sudo apt-get install samba
$ sudo apt-get install winbind

Edit /etc/nsswitch.conf to enable wins
change 'hosts: files dns' TO 'hosts: files wins dns'

To change the hostname
edit /etc/hostname

FYI 'raspberrypi' works just fine as a host name

$ sudo reboot

###############################################################
Setup arducopter for quad
###############################################################

$ sudo update-alternatives --config arducopter
15

$ sudo nano /etc/default/arducopter 
127.0.0.1 -> 10.0.0.95

$ sudo systemctl daemon-reload

sudo systemctl start arducopter

sudo systemctl enable arducopter

###############################################################
Setup Samba for network drive share
###############################################################

sudo smbpasswd -a pi
sudo smbpasswd -a root
sudo nano /etc/samba/smb.conf

[root_fs]
path = /
valid users = root
read only = no

[pi_fs]
path = /home/pi
valid users = pi
read only = no

sudo service smbd restart

# in windows, win key + R, \\navio


###############################################################
Dronekit setup
###############################################################

pip install dronekit
pip install dronekit-sitl


###############################################################
MAVProxy
###############################################################
sudo apt-get install python-dev python-opencv python-wxgtk3.0 python-pip python-matplotlib python-pygame python-lxml
pip install MAVProxy

# in /etc/rc.local
echo "Starting MAVproxy."
mavproxy.py --out DESKTOP-ROD693A:14550 --master localhost:14550 --out localhost:14850 &






git remote set-url origin --push --add https://daniel_robinson@bitbucket.org/falkonapps/blue-image-processing.git