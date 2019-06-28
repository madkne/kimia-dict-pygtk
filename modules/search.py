
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from modules import _global as glob, models
from gi.repository import Gtk, Gdk
import gi
import traceback
gi.require_version('Gtk', '3.0')


class SearchDB():
    # ---------------------------------------------------
    # =>get name of a database and by its type,search it and return result
    def search_in_databases(self, name: str, text: str, lang: str, count: int):
        # print('search in database:'+name+','+text+','+lang)
        result = models.dbresult(text)
        # print('RESULT:',id(result), str(result))
        try:
            with open('./db/'+name+'.bnu', encoding='utf-8') as f:
                for line in f:
                    line = line.lower().strip()
                    if len(line) < 3 or (line[0] == '/'and line[1] == '/'):
                        continue
                    # print('line:',line[0],line,'   spacious   '.strip(),type(line))
                    if line[0] == '#':
                        # print('#shrp:'+line)
                        sp = line[1:].strip().split(';')
                        # =>get dictionary name
                        if sp[0] == 'name':
                            pre = sp[1].split('$$')
                            result.dict_name = (
                                pre[0] if lang == 'en' else pre[1])
                        # =>get type
                        elif sp[0] == 'type':
                            result.dict_type = sp[1]
                    else:
                        break
            # ---------------------------reaset result
            result.searched_lang = ''
            result.result_keys = []
            result.result_values = []
            # ---------------------------simple type
            if result.dict_type == 'simple':
                result = self.search_in_simple_dict(name, text, result)
                result.result_multi = False
            # ---------------------------list type
            elif result.dict_type == 'list':
                result = self.search_in_list_dict(name, text, result)
                result.result_multi = True

        except Exception as e:
            print("(1)error message=> "+e)
        return result
    # ---------------------------------------------------
    # =>search in 'simple' type databases

    def search_in_simple_dict(self, name: str, text: str, result: models.dbresult):
        try:
            with open('./db/'+name+'.bnu', encoding='utf-8') as f:
                for line in f:
                    line = line.lower().strip()
                    sp = line.split('@')
                    if len(line) < 3 or (line[0] == '/'and line[1] == '/') or line[0] == '#' or len(sp)!=2:
                        continue
                    
                    if (result.searched_lang == ''or result.searched_lang == 'en')and sp[0] == text:
                        result.searched_lang = 'en'
                        result.result_keys.append(
                            models.lblstruct(text, models.alignment.EN))
                        result.result_values.append(
                            models.lblstruct(sp[1], models.alignment.FA))
                    elif (result.searched_lang == ''or result.searched_lang == 'fa') and sp[1].replace("ي", "ی") == text.replace("ي", "ی"):
                        # print('######:', sp[1], text, sp[1] == text)
                        result.searched_lang = 'fa'
                        result.result_keys.append(
                            models.lblstruct(text, models.alignment.FA))
                        result.result_values.append(
                            models.lblstruct(sp[0], models.alignment.EN))

        except Exception as ex:
            print('(3)error message =>'+traceback.format_exc())
        return result
    # ---------------------------------------------------
    # =>search in 'list' type databases

    def search_in_list_dict(self, name: str, text: str, result: models.dbresult):
        try:
            with open('./db/'+name+'.bnu', encoding='utf-8') as f:
                for line in f:
                    line = line.lower().strip()
                    if len(line) < 3 or (line[0] == '/'and line[1] == '/') or line[0] == '#':
                        continue
                    sp = line.split('@')
                    if (result.searched_lang == ''or result.searched_lang == 'en')and text in sp[0]:
                        result.searched_lang = 'en'
                        result.result_keys.append(
                            models.lblstruct(sp[0], models.alignment.EN))
                        result.result_values.append(
                            models.lblstruct(sp[1], models.alignment.FA))
                    elif (result.searched_lang == ''or result.searched_lang == 'fa')and text.replace("ي", "ی") in sp[1].replace("ي", "ی"):
                        result.searched_lang = 'fa'
                        result.result_keys.append(
                            models.lblstruct(sp[1], models.alignment.FA))
                        result.result_values.append(
                            models.lblstruct(sp[0], models.alignment.EN))

        except Exception as ex:
            print('(4)error message =>'+traceback.format_exc())
        return result
