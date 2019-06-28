# -*- coding: utf-8 -*-
from gi.repository import Gtk, Gdk
from modules import _global as glob
import gi
gi.require_version('Gtk', '3.0')
from modules import models
# -----------------------------------------
# =>global vars
SearchTxt = Gtk.Entry()
SearchBtn = None
content = None

# =>a class for handling input and button
# class SearchBox_handler():
# -----------------------------------------
# =>main search box class


class SearchBox(Gtk.Box):
    #=>public vars
    SearchValue = ''
    # ---------------------------------------------------
    def __init__(self):
        Gtk.Box.__init__(self)
        #=>define a entry textbox properties
        SearchTxt.set_activates_default(True)
        SearchTxt.set_placeholder_text("Search any Word/Term...")
        # SearchTxt.set_active(True)
        #=>handle 'key_release' event of button
        SearchTxt.connect('key_release_event',
                          self.searchtxt__KeyRelease__event)
        #=>define a button
        SearchBtn = Gtk.Button("Search")
        #=>handle 'clicked' event of button
        SearchBtn.connect('clicked', self.searchbtn__clicked__event)
        #=>add button to end of box layout
        self.pack_end(SearchBtn, False, False, 2)
        #=>add entry to start of box layout
        self.pack_start(SearchTxt, True, True, 2)
    # ---------------------------------------------------
    # =>KeyRelease event for searchtxt
    def searchtxt__KeyRelease__event(self, widget, event):
        # print('search entry...'+widget.get_text() +'...'+str(event.hardware_keycode))
        self.SearchValue = widget.get_text()
        if event.hardware_keycode == 36:  # ENTER press key
            self.search(widget.get_text())
    # ---------------------------------------------------
    # =>clicked event for searchbtn
    def searchbtn__clicked__event(self, event):
        print('search button...')
        self.search(self.SearchValue)
    # ---------------------------------------------------
    # =>main search function
    @staticmethod
    def search(text:str,isnew:bool=True):
        #=>define vars
        results = [] #=>define results list for show
        dict_count=0 #=>count of found result dicts
        #=>convert text to trim and lowercase
        text = text.strip().lower()
        print('search:'+text+'$')
        #append to WORDB
        if isnew:
            glob.WORDB,glob.WORDBPOS=models.wordb.append(glob.WORDB,text,glob.WORDBPOS)
        #=>if text be null or '', then return Nothing!
        if len(text) == 0:
            return
        #=>remove all segments on content
        for con in content.get_children():
            content.remove(con)
        #=>search into databases
        for dic in glob.DICTIONARIES:
            res = search.SearchDB().search_in_databases(dic.name, text, glob.LANG, dic.count)
            # print('res('+dic.name+')::'+str(res))
            #=>if result of 'search_in_databases' be empty
            if res.dict_type == '':
                print('not exist db...')
                continue
            print('searched in database:'+dic.name)
            #=>append result to 'results' list
            results.append(res)
            #=>if found anything!
            if len(res.result_values)>0:
                #=>set search results in content
                frame = content.create_frame(res)
                #delete res object
                del(res)
                #=>append created frame to box layout
                content.pack_start(frame, True, True, 0)
                #count dict found
                dict_count+=1
            #=>if not found, ignore it!
            else : continue
        #=>if not found any result on all dicts
        if dict_count==0:
            content.pack_start(content.create_notfound(), True, True, 0)
        # =>update box layout
        content.show_all()


# -----------------------------------------
# =>main content panel class
from designs import content
# -----------------------------------------
content = content.MainContent()
# -----------------------------------------
#=> search in database class
from modules import search

