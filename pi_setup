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