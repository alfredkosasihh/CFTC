import quandl
import pandas as pd
from api.db import database
from utils.config import api_key

data = []

class cot:
    def __init__(self, quandl_key=api_key):
        self.quandl_key = quandl_key
    
    def init_data(self, types, quandl_code=''):
        a = quandl.get(quandl_code, authtoken=self.quandl_key)
        for i in range(1,11):
            long_val = int(a.iloc[-i,1])
            short_val = int(a.iloc[-i,2])
            change_long = int(a.iloc[-i,1]) - int(a.iloc[-(i+1),1]) 
            change_short = int(a.iloc[-i,2]) - int(a.iloc[-(i+1),2]) 
            net = long_val - short_val

            data.clear()
            data.extend((str(a.index[-i]).split(' ')[0], long_val, short_val, change_long, change_short, net))

            database().store(types, data)

            # print(str(a.index[-i]).split(' ')[0], long_val, short_val, change_long, change_short, net)

    def weekly(self, types, quandl_code=''):
        a = quandl.get(quandl_code, authtoken=self.quandl_key)
        long_val = int(a.iloc[-1,1])
        short_val = int(a.iloc[-1,2])
        change_long = int(a.iloc[-1,1]) - int(a.iloc[-(2),1]) 
        change_short = int(a.iloc[-1,2]) - int(a.iloc[-(2),2]) 
        net = long_val - short_val
        
        #store database
        data.clear()
        data.extend((str(a.index[-1]).split(' ')[0], long_val, short_val, change_long, change_short, net))

        database().store(types, data)

        # print(str(a.index[-1]).split(' ')[0], long_val, short_val, change_long, change_short, net)

    
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

# dat = database()
# test = cot()

# # test.test1()
# # print(bc)
# # for types in type:
# #     dat.create(types)

# for types in type:
#     code = type.get(types)       
#     test.init_data(types, code)
#     # test.weekly(types, code)

