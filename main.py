#!/usr/bin/python
# -*- coding: utf-8 -*-
# import files and libraries
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Keybinder', '3.0')
# ----------------------------------------
from gi.repository import Gtk, Gdk, Keybinder
from designs import menu, search
from modules import _global as glob
# from memory_profiler import profile


# =>global vars
MainBox = None
MainToolbar = None
MainSearch = None
# =>main window shown class
class MainWindow(Gtk.Window):

    def __init__(self):
        # =>public window props
        Gtk.Window.__init__(self,
                            title="Kimia-Dict (V "+glob.VERSION+")"
                            # type_hint=Gdk.WindowTypeHint.TOOLBAR
                            )
        self.set_default_size(800, 500)
        self.set_icon_from_file("./assets/img/logo.png")
        self.set_position(Gtk.WindowPosition.CENTER)
        #=>connect to destory main window
        # self.connect("destroy", self.on_destroy)
        self.connect("delete_event", self.on_delete)
        #=>connect to key events of main window
        self.connect("key-press-event",self.on_key_press_event)
        # =>set toolbar
        MainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        MainToolbar = menu.ToolBar()
        MainBox.pack_start(MainToolbar, False, False, 0)
        # =>set search box
        MainSearch = search.SearchBox()
        MainBox.pack_start(MainSearch, False, False, 10)
        # =>set content
        sw = Gtk.ScrolledWindow()
        mcontent = search.content
        sw.add_with_viewport(mcontent)
        MainBox.pack_start(sw, True, True, 0)
        # =>add MainBox to main window
        self.add(MainBox)
        # =>init keybinder
        Keybinder.init()
        # =>handle global shortuct by 'shortcut_callback'
        Keybinder.bind(glob.KEYDISPLAY, self.show_shortcut_callback,
                       "keystring %s (user data)" % glob.KEYDISPLAY)
        # =>show all widgets and window
        self.show_all()
        # self.add(sw)
    # ---------------------------------------------------
    def on_delete(self, widget=None, *data):
        print('Hide main Window')
        self.hide()
        return True
    # ---------------------------------------------------
    # def show_window(self, data=None):
    #     print('Show again main window')
    #     self.show_all()
    #     return True
    # ---------------------------------------------------
    def show_shortcut_callback(self, keystr, user_data):
        print('Show again main window')
        print("Handling", user_data)
        print("Event time:", Keybinder.get_current_event_time())
        self.show_all()
        # print('childs:',self.get_children()[0].get_children()[1].get_children()[0])
        self.get_children()[0].get_children()[1].get_children()[0].activate()
        return True
    # ---------------------------------------------------
    def on_key_press_event(self,widget,event):
        keyval = event.keyval
        keyval_name = Gdk.keyval_name(keyval)
        state = event.state
        ctrl = (state & Gdk.ModifierType.CONTROL_MASK)
        alt=(state & Gdk.ModifierType.MOD1_MASK)
        print('Key pressed:keyval:{0},ctrl:{1},alt:{2}'.format(keyval_name,ctrl,alt))
        # print(self.get_children()[0].get_children()[1].get_children()[0])
        if keyval_name == "Escape":
            self.on_delete()
        elif ctrl and keyval_name=='k':
            Gtk.main_quit()
            # self.get_children()[0].get_children()[1].get_children()[0].set_text('')
        else : return False
        return True

# ---------------------------------------------------
# =>main function
# @profile
def main():
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    # init main window and show it!
    window = MainWindow()
    # =>set try icon
    tray = menu.TryIcon(window)

    Gtk.main()
# ---------------------------------------------------
if __name__ == '__main__': main()
    
