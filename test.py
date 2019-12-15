# -*- coding:utf-8 -*-
'''
Created on 2019/05/12
@author: Hunk Guo
'''
import datetime,time
import tushare as ts
import numpy as np
import pandas as pd


# 以股票找信息
class stock:
    def __init__ (self):
        #self.pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')
        pass

    def run(self):
        # 初始化
        pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')
        
        # 获取所属行业,最后一个
        df_stock_in_index_member = pro.index_member(ts_code='600000.SH').tail(1)
        #print(df_stock_in_index_member.values[0][0])
        
        #获取分类的成份股
        df_index_member = pro.index_member(index_code=df_stock_in_index_member.values[0][0], fields='index_code, con_code, in_date')
        #print(df_index_member)
        
        for index_member_stock in df_index_member.iterrows():
            #balancesheet
            print(index_member_stock[1]['con_code'])
            stock_code = index_member_stock[1]['con_code']
            stock_balancesheet = pro.balancesheet(ts_code=stock_code)
            # 资产总计
            print(stock_balancesheet.head(1)['total_assets'])
            break
        
class index:
    def init(self):
        pass
    
    def run(self):
        # 初始化
        pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')

        # 指数
        # df_index = pro.index_basic(market='CSI', category='主题指数')
        df_index = pro.index_dailybasic(trade_date='20191213', fields='ts_code,trade_date,turnover_rate,pe')
        print(df_index)


if __name__ == "__main__":
    
    s = index()
    s.run()
    #print('开始交易日为：%s ;结束交易日为：%s ' % (start_date_open, end_date_open))
