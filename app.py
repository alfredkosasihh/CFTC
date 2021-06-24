import sys
from api.db import database, initialize
from api.data import cot

type = {
            'gold':'CFTC/088691_F_L_ALL',
            'aud':'CFTC/232741_F_L_ALL',
            'cad':'CFTC/090741_F_L_ALL',
            'cbp':'CFTC/096742_F_L_ALL',
            'nasdaq_100':'CFTC/209742_F_L_ALL',
            'snp_100':'CFTC/13874A_FO_L_ALL',
            'xag':'CFTC/084691_F_L_ALL',
            'chf':'CFTC/092741_F_L_ALL',
            'crl':'CFTC/102741_F_L_ALL',
            'jpy':'CFTC/097741_F_L_ALL',
            'nzd':'CFTC/112741_F_L_ALL',
            'rub':'CFTC/089741_F_L_ALL',
            'eur':'CFTC/099741_F_L_ALL'}   

def init():
    initialize()

def migrate():
    for types in type:
        database().create(types)

def weekly():
    for types in type:
        code = type.get(types)       
        cot().weekly(types, code)

def initdata():
    for types in type:
        code = type.get(types)       
        cot().init_data(types, code)

def main():
    if(len(sys.argv)!=2):
        print('-->python app.py db')
        print('-->python app.py migrate')
        print('-->python app.py weekly')
        print('-->python app.py initdata')
    else:
        if(str(sys.argv[1])=='db'):
            initialize()
        elif(str(sys.argv[1])=='migrate'):
            migrate()
        elif(str(sys.argv[1])=='weekly'):
            weekly()
        elif(str(sys.argv[1])=='initdata'):
            initdata()
        else:
            print('-->python app.py db')
            print('-->python app.py migrate')
            print('-->python app.py weekly')
            print('-->python app.py initdata')

if (__name__ == "__main__"):
    main()



