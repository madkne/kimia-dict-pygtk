# -*- coding: utf-8 -*-

from gi.repository import Gtk, Gdk
from modules import models
import gi
gi.require_version('Gtk', '3.0')
# =>global vars
# =>main content panel class


class MainContent(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self,
                         spacing=20,
                         orientation=Gtk.Orientation.VERTICAL
                         )
    # -----------------------------------------
    # =>create a frame by gtk

    def create_frame(self, db: models.dbresult):
        # =>create a gtk frame
        frame = Gtk.Frame()
        # =>set label for frame
        frame.set_label(db.dict_name)
        frame.set_label_align(0.05, 0.5)
        frame.set_shadow_type(Gtk.ShadowType.ETCHED_OUT)
        # =>create a box layout for set contents of frame
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        # =>check if result is multi line
        if db.result_multi:
            # =>in loop,create labels for keys,values
            for i in range(0, len(db.result_values), 1):
                # print('LIST({0}):[key:{1},value:{2}]'.format(i,db.result_keys[i].text,db.result_values[i].text))
                # =>append a label for key
                box.pack_start(Gtk.Label(
                    db.result_keys[i].text, selectable=False,
                                     single_line_mode=False,lines=4,wrap=True), False, True, 10)
                # =>append a label for value
                box.pack_start(Gtk.Label(
                    db.result_values[i].text, selectable=True,
                                     single_line_mode=False,lines=4,wrap=True), True, True, 10)
                # =>append a horiz separator to box layout
                box.pack_start(Gtk.HSeparator(), True, False, 5)
        # =>if result not multi line
        else:
            # =>join all result values to a string
            val = ''
            for j in range(0, len(db.result_values), 1):
                val += db.result_values[j].text
                if j+1 < len(db.result_values):
                    val += ' ,'
            # val = ' ,'.join()
            # =>append a label for searched text
            box.pack_start(Gtk.Label(db.searched_text, selectable=True,
                                     single_line_mode=True), True, True, 10)
            # =>append a label for all values
            box.pack_start(Gtk.Label(val, selectable=True,
                                     single_line_mode=False,lines=4,wrap=True), True, True, 10)
        # box.pack_start(Gtk.Label(key['name'], selectable=False,
        #                          single_line_mode=True, justify=(0 if key['align'

        # =>add box layout to frame
        frame.add(box)
        # =>return frame
        return frame
    # -----------------------------------------
    # =>create a not found page by gtk

    def create_notfound(self):
        # =>create a box layout for set contents of frame
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        # =>append image to box layout
        box.pack_start(
            Gtk.Image(file='./assets/img/notfound.png'), True, True, 0)
        # =>append a label for notfound message
        box.pack_start(Gtk.Label("SORRY! Not Found into any Dictionaries...",
                                 selectable=False), True, True, 5)
        # =>return box layout
        return box
