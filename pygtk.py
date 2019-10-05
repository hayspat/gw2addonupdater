import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from classupdater import *

class Handler:
    def on_window_destroy(self, *args):
        with open(inipath, 'w') as configfile:
            parser.write(configfile)
        Gtk.main_quit()
        
    def chooser_file_set_cb(self, button):
        gw2path = button.get_filename()
        parser["path"]["gw2path"] = gw2path
 
    def gw2radial_button_clicked_cb(self, button):      
        gw2radial.unpack()
        AddonUpdater.setname()
        AddonUpdater.copy(gw2radial)
        gw2radial.version = gw2radial.latestversion
        parser["gw2radial"]["version"] = "{}".format(gw2radial.latestversion)
        gw2radial_button.hide() 
        
    def gw2radial_switch_activate_cb(self, button):
        pass
    def gw2radial_switch_state_set_cb(self, arg1, arg2):
        if arg2:
            if gw2radial.status == "enabled":
                pass
            else:
                gw2radial.status = "enabled"
                parser["gw2radial"]["status"] = "enabled"
                AddonUpdater.setname()
                AddonUpdater.copy(gw2radial)
                gw2radial.version = gw2radial.latestversion
                parser["gw2radial"]["version"] = "{}".format(gw2radial.latestversion)
        else:
            if gw2radial.status == "disabled":
                pass
            else:
                gw2radial.status = "disabled"
                parser["gw2radial"]["status"] = "disabled"
                AddonUpdater.setname()
                AddonUpdater.copy(gw2radial)
                gw2radial_button.hide()                

    def arcpds_button_clicked_cb (self, button):   
        arcdps.unpack()
        AddonUpdater.setname()
        AddonUpdater.copy(arcdps)
        arcdps.version = arcdps.latestversion
        parser["arcdps"]["version"] = "{}".format(arcdps.latestversion)
        arcdps_button.hide() 
    def arcdps_switch_activate_cb(self, button):
        pass
    def arcdps_switch_state_set_cb(self, arg1, arg2):
        if arg2:
            if arcdps.status == "enabled":
                pass
            else:
                arcdps.status = "enabled"
                parser["arcdps"]["status"] = "enabled"
                AddonUpdater.setname()
                AddonUpdater.copy(arcdps)
                arcdps.version = arcdps.latestversion
                parser["arcdps"]["version"] = "{}".format(arcdps.latestversion)
        else:
            if arcdps.status == "disabled":
                pass
            else:
                arcdps.status = "disabled"
                parser["arcdps"]["status"] = "disabled"
                AddonUpdater.setname()
                AddonUpdater.copy(arcdps)
                arcdps_button.hide()

    def on_d9vk_button_clicked(self, button):      
        d9vk.unpack()
        AddonUpdater.setname()
        AddonUpdater.copy(d9vk)
        d9vk.version = d9vk.latestversion
        parser["d9vk"]["version"] = "{}".format(d9vk.latestversion)
        d9vk_button.hide() 
    def d9vk_switch_activate_cb(self, button):
        pass
    def d9vk_switch_state_set_cb(self, arg1, arg2):
        if arg2:
            if d9vk.status == "enabled":
                pass
            else:
                d9vk.status = "enabled"
                parser["d9vk"]["status"] = "enabled"
                AddonUpdater.setname()
                AddonUpdater.copy(d9vk)
                d9vk.version = d9vk.latestversion
                parser["d9vk"]["version"] = "{}".format(d9vk.latestversion)
        else:
            if d9vk.status == "disabled":
                pass
            else:

                d9vk.status = "disabled"
                parser["d9vk"]["status"] = "disabled"
                AddonUpdater.setname()
                AddonUpdater.copy(d9vk)
                d9vk_button.hide()

builder = Gtk.Builder()
builder.add_from_file("final.glade")
builder.connect_signals(Handler())
window = builder.get_object("window")
window.show_all()


chooser = builder.get_object("chooser")
chooser.set_filename(parser["path"]["gw2path"])

        
d9vk_button = builder.get_object("d9vk_button")
gw2radial_button = builder.get_object("gw2radial_button")
arcdps_button = builder.get_object("arcdps_button")

arcdps_switch = builder.get_object("arcdps_switch")
gw2radial_switch = builder.get_object("gw2radial_switch")
d9vk_switch = builder.get_object("d9vk_switch")

if gw2radial.status == "enabled":
    gw2radial_switch.props.state = True
if arcdps.status == "enabled":
    arcdps_switch.props.state = True
if d9vk.status == "enabled":
    d9vk_switch.props.state = True
    
if d9vk.version == d9vk.latestversion or d9vk.status != "enabled":   
    d9vk_button.hide()
if arcdps.version == arcdps.latestversion or arcdps.status != "enabled":   
    arcdps_button.hide()
if gw2radial.version == gw2radial.latestversion or gw2radial.status != "enabled":   
    gw2radial_button.hide()
    
print(d9vk.version, d9vk.latestversion)
print(gw2radial.version, gw2radial.latestversion)
print(arcdps.version, arcdps.latestversion)



    
Gtk.main()
