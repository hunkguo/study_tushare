# -*- coding:utf-8 -*-
'''
Created on 2019/05/12
@author: Hunk Guo
'''
import datetime,time
import tushare as ts
import numpy as np
import pandas as pd

class stock:
    def __init__ (self):
        #self.pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')
        pass

    def run(self):
        # 初始化
        pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')
        
        # 获取所属行业
        df_stock_in_index_member = pro.index_member(ts_code='600000.SH')
        
        for index_member in df_stock_in_index_member.iterrows():
            #获取分类的成份股
            df_index_member = pro.index_member(index_code='850531.SI', fields='index_code, con_code, in_date')
            print(df_index_member)
        


if __name__ == "__main__":
    
    s = stock()
    s.run()
    #print('开始交易日为：%s ;结束交易日为：%s ' % (start_date_open, end_date_open))
