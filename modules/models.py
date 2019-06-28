# -*- coding: utf-8 -*-
from enum import Enum
import random
# *****************ENUMS*********************
# *******************************************


class alignment(Enum):
    LEFT = 0
    RIGHT = 1
    CENTER = 2
    FA = 1
    EN = 0
# *************INTERFACES********************
# *******************************************


class dictionaries:
    name = ''
    count = 0

    def __init__(self, name: str, count: int):
        self.name = name
        self.count = count
# *******************************************


class lblstruct:
    align = alignment.LEFT
    text = ''

    def __init__(self, text, align):
        self.text = text
        self.align = align
    def __str__(self):
        return "(lblstruct)[name:{0},align:{1}]".format(self.text,str(self.align))

# *******************************************
class wordb:
    words=[]
    cur_pos=0
    @staticmethod
    def append(words,word:str,cur_pos:int):
        if cur_pos>=0: words=words[0:cur_pos+1]
        lenw=len(words)
        if lenw==0 or words[lenw-1]!=word: words.append(word)
        return words,cur_pos+1
    @staticmethod
    def back(words:[],cur_pos:int):
        if cur_pos>0: cur_pos-=1
        word=''
        if len(words)>0: word=words[cur_pos]
        return word,cur_pos
    @staticmethod
    def forward(words:[],cur_pos:int):
        if cur_pos<len(words)-1:cur_pos+=1
        word=''
        if len(words)>0: word=words[cur_pos]
        return word,cur_pos
    def info(self):
        return "count:{0},current:{1}\nwords:{2}".format(len(self.words),self.cur_pos,str(self.words))
# *******************************************
class dbresult:
    id=0
    dict_name = ''
    dict_type = 'simple'
    searched_lang = 'en'
    searched_text = ''
    result_multi = False
    result_keys = []  # lblstruct
    result_values = []  # lblstruct

    def __init__(self,search:str=''):
        self.searched_text=search
        self.id=random.randint(0, 1000) 
    def __str__(self):
        res_keys=''
        res_vals=''
        if len(self.result_keys)>0 :
            for i in range(0,len(self.result_keys),1):
                res_keys+=str(self.result_keys[i])
                if i+1<len(self.result_keys): res_keys+=' ,'
            res_keys='['+res_keys+']'
        if len(self.result_values)>0 :
            for i in range(0,len(self.result_values),1):
                res_vals+=str(self.result_values[i])
                if i+1<len(self.result_values): res_vals+=' ,'
            res_vals='['+res_vals+']'
        return "(dbresult)[id:{7},dict_name:{0},dict_type:{1},searched_lang:{2},searched_text:{3},result_multi:{4},result_keys:{5},result_values:{6}]".format(self.dict_name,self.dict_type,self.searched_lang,self.searched_text,str(self.result_multi),res_keys,res_vals,self.id)
