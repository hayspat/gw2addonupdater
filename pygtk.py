import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from classupdater import *
from arcdps import *


class Handler:
    def on_window_destroy(self, *args):
        Gtk.main_quit()
        
    def chooser_file_set_cb(self, button):
        print("selected: %s"%button.get_filename())
        AddonUpdater.gw2path = button.get_filename()
        print(AddonUpdater.gw2path)        
    def gw2radial_button_clicked_cb(self, button):
        pass
    def gw2radial_activate_cb(self, button):
        pass
    def gw2radial_state_set_cb(self, arg1, arg2):
        if arg2:
            gw2radial.status = "enabled"
            AddonUpdater.setname()
            print("Gw2Radial: {}\nArcdps: {}\nD9VK: {}\n".format(gw2radial.fn, arcdps.fn, d9vk.fn))
            print("Gw2Radial: {}\nArcdps: {}\nD9VK: {}\n".format(gw2radial.status, arcdps.status, d9vk.status))

        else:
            gw2radial.status = "disabled"
            AddonUpdater.setname()
            print("Gw2Radial: {}\nArcdps: {}\nD9VK: {}\n".format(gw2radial.fn, arcdps.fn, d9vk.fn))
            print("Gw2Radial: {}\nArcdps: {}\nD9VK: {}\n".format(gw2radial.status, arcdps.status, d9vk.status))

    def arcpds_button_clicked_cb (self, button):
        pass
    def arcdps_switch_activate_cb(self, button):
        print("DEneme")
    def arcdps_switch_state_set_cb(self, arg1, arg2):
        if arg2:
            arcdps.status = "enabled"
            AddonUpdater.setname()
            print("Gw2Radial: {}\nArcdps: {}\nD9VK: {}\n".format(gw2radial.fn, arcdps.fn, d9vk.fn))
            print("Gw2Radial: {}\nArcdps: {}\nD9VK: {}\n".format(gw2radial.status, arcdps.status, d9vk.status))
        else:
            arcdps.status = "disabled"
            AddonUpdater.setname()
            print("Gw2Radial: {}\nArcdps: {}\nD9VK: {}\n".format(gw2radial.fn, arcdps.fn, d9vk.fn))
            print("Gw2Radial: {}\nArcdps: {}\nD9VK: {}\n".format(gw2radial.status, arcdps.status, d9vk.status))
            

    def on_d9vk_button_clicked(self, button):
        print(d9vk.getversion())
    def d9vk_switch_activate_cb(self, button):
        pass
    def d9vk_switch_state_set_cb(self, arg1, arg2):
        if arg2:
            d9vk.status = "enabled"
            AddonUpdater.setname()
            print("Gw2Radial: {}\nArcdps: {}\nD9VK: {}\n".format(gw2radial.fn, arcdps.fn, d9vk.fn))
            print("Gw2Radial: {}\nArcdps: {}\nD9VK: {}\n".format(gw2radial.status, arcdps.status, d9vk.status))

        else:
            d9vk.status = "disabled"
            AddonUpdater.setname()
            print("Gw2Radial: {}\nArcdps: {}\nD9VK: {}\n".format(gw2radial.fn, arcdps.fn, d9vk.fn))
            print("Gw2Radial: {}\nArcdps: {}\nD9VK: {}\n".format(gw2radial.status, arcdps.status, d9vk.status))



builder = Gtk.Builder()
builder.add_from_file("final.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
window.show_all()

Gtk.main()
