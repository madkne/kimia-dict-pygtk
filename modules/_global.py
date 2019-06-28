
from modules import models


VERSION="0.64"
LANG="en"
APPNAME="KimiaDict"
PROGRAMMER="madkne"
STARTED="2019.6.24"
VERSION1="0.48-2019.6.26"
KEYDISPLAY="<Ctrl>G"
DICTIONARIES=[
    models.dictionaries('word_dict', 0),
    models.dictionaries('proverb_dict', 0),
    models.dictionaries('it_dict', 0),
    models.dictionaries('math_dict', 0),
    models.dictionaries('terms_dict', 0),
    models.dictionaries('medical_dict', 0)
]

WORDB=[]
WORDBPOS=-1

'''
window shortcut:
//ctrl+Escape   : clear the search entry
Escape          : hide main window 
ctrl+k          : exit program
'''