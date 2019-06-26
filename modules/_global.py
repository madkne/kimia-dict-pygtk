
from modules import models


VERSION="0.49"
LANG="en"
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

'''
window shortcut:
//ctrl+Escape   : clear the search entry
Escape          : hide main window 
ctrl+k          : exit program
'''