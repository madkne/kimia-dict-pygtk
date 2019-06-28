
from gi.repository import Gtk, Gdk, GdkPixbuf
from modules import _global as glob,models
from designs import search
import gi
gi.require_version('Gtk', '3.0')


class ToolBar(Gtk.Toolbar):
    def __init__(self):
        Gtk.Toolbar.__init__(self)
        # =>back & forward buttons for get back & next words searched
        back_btn = Gtk.ToolButton(Gtk.STOCK_GO_BACK)
        back_btn.set_label('back')
        forward_btn = Gtk.ToolButton(Gtk.STOCK_GO_FORWARD)
        forward_btn.set_label('forward')
        back_btn.connect('clicked',self.back_forward_click_event)
        forward_btn.connect('clicked',self.back_forward_click_event)
        # =>about us and kimia dict button
        about_btn = Gtk.ToolButton(Gtk.STOCK_ABOUT)
        about_btn.set_label('About')
        about_btn.connect('clicked', self.about_click_event)
        # =>quit button for complete quit from kimia dict
        quit_btn = Gtk.ToolButton(Gtk.STOCK_QUIT)
        quit_btn.connect("clicked", Gtk.main_quit)
        # =>insert all buttons to toolbar
        self.insert(back_btn, 0)
        self.insert(forward_btn, 1)
        self.insert(Gtk.SeparatorToolItem(), 2)  # =>insert a separator
        self.insert(about_btn, -1)
        self.insert(quit_btn, -1)

    # ---------------------------------------------------

    def back_forward_click_event(self, widget):
        # print(str(widget),widget.get_label())
        widtype=widget.get_label()
        word='NOTFOUND'
        if widtype=='back':
            word,glob.WORDBPOS=models.wordb.back(glob.WORDB,glob.WORDBPOS)
        elif widtype=='forward':
            word,glob.WORDBPOS=models.wordb.forward(glob.WORDB,glob.WORDBPOS)
        print(widtype,word,glob.WORDB,glob.WORDBPOS)
        search.SearchTxt.set_text(word)
        search.SearchBox.search(word,False)

    # ---------------------------------------------------
    def about_click_event(self, widget):
        print('about us...')
        about = Gtk.AboutDialog()
        about.set_authors([glob.PROGRAMMER])
        about.set_program_name(glob.APPNAME)
        about.set_version(glob.VERSION)
        about.set_copyright("(c) OpenSource Community")
        about.set_comments(
            "Kimia-Dict is a persian-english dictionary for linux LOVERS;)")
        about.set_license_type(Gtk.License.MIT_X11)
        about.set_logo(GdkPixbuf.Pixbuf().new_from_file(
            "./assets/img/logo_large.png"))
        about.run()
        about.destroy()

# *****************************************************


class TryIcon(Gtk.StatusIcon):
    mainWin = None
    # ---------------------------------------------------

    def __init__(self, mainWin: Gtk.Window):
        self.mainWin = mainWin
        Gtk.StatusIcon.__init__(
            self, tooltip_text='Kimia-Dict (V '+glob.VERSION+')')
        self.set_from_file('./assets/img/logo.png')
        self.set_has_tooltip(True)
        self.set_visible(True)
        self.connect("activate", self.on_click)
    # ---------------------------------------------------

    def on_click(self, data):  # data1 and data2 received by the connect action line 23
        # print ('self :', self)
        # print('data1 :',data)
        event = Gtk.get_current_event()
        # print('event :',event)
        btn = event.button  # this gets the button value of gtk event.
        # print('event.button :',btn)
        # required by the popup. No time - no popup.
        time = Gtk.get_current_event_time()
        # print ('time:', time)

        menu = Gtk.Menu()

        menu_item1 = Gtk.MenuItem("Display Window")
        menu.append(menu_item1)
        # added by gv - it had nothing before
        menu_item1.connect("activate", self.mainWin.show_window)

        menu_item2 = Gtk.MenuItem("Quit")
        menu.append(menu_item2)
        menu_item2.connect("activate", Gtk.main_quit)

        menu.show_all()
        # button can be hardcoded (i.e 1) but time must be correct.
        menu.popup(None, None, None, btn, time, time)
