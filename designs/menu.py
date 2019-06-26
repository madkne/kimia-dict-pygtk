# import __global
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gdk
from modules import _global as glob


class ToolBar(Gtk.Toolbar):
    def __init__(self):
        Gtk.Toolbar.__init__(self)
        # self.set_active(False)
        # self.insert(Gtk.ToolButton("Hello"),0)
        newbtn = Gtk.ToolButton(Gtk.STOCK_NEW)
        sep = Gtk.SeparatorToolItem()
        self.insert(newbtn,0)
        self.insert(sep,1)

# *****************************************************
class TryIcon(Gtk.StatusIcon):
    mainWin=None
    # ---------------------------------------------------
    def __init__(self,mainWin:Gtk.Window):
        self.mainWin=mainWin
        Gtk.StatusIcon.__init__(self,tooltip_text='Kimia-Dict (V '+glob.VERSION+')')
        self.set_from_file('./assets/img/logo.png')
        self.set_has_tooltip(True)
        self.set_visible(True)
        self.connect("activate", self.on_click)
    # ---------------------------------------------------
    def on_click(self,data): #data1 and data2 received by the connect action line 23
        # print ('self :', self)
        # print('data1 :',data)
        event=Gtk.get_current_event()
        # print('event :',event)
        btn=event.button #this gets the button value of gtk event.
        # print('event.button :',btn)
        time=Gtk.get_current_event_time() # required by the popup. No time - no popup.
        # print ('time:', time)

        menu = Gtk.Menu()

        menu_item1 = Gtk.MenuItem("Display Window")
        menu.append(menu_item1)
        menu_item1.connect("activate",self.mainWin.show_window) #added by gv - it had nothing before

        menu_item2 = Gtk.MenuItem("Quit")
        menu.append(menu_item2)
        menu_item2.connect("activate", Gtk.main_quit)

        menu.show_all()
        menu.popup(None, None, None, btn, time,time) #button can be hardcoded (i.e 1) but time must be correct.
    
