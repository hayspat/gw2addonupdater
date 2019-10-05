# GW2 Addon Updater

It uses github rest api to fetch and download latest addon versions.
If there is an update available, update button pops up.
GTK is used for ui.
I only tested on linux, it may work on windows if you have installed gtk.


<img src="https://i.imgur.com/qNI1nrQ.png">


<h1>Dependencies</h1>


<h2>Ubuntu and derivatives</h2>

sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 python3-wget

<h2>Arch and derivatives</h2>

sudo pacman -S python-gobject gtk3 python-pip </br>
sudo pip install wget


<h1>Usage</h1>

chmod +x gw2addonupdater.py </br>
python3 gw2addonupdater.py
