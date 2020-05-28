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
        pass

    def run(self):
        # 初始化
        pro = ts.pro_api('***')
        
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


# 根据股票所属行业筛选同行业其他股票
class same_industry_stock:
    def init(self):
        pass
    def run(self):
        # 初始化tushare接口
        pro = ts.pro_api('ee53f45bc754c9f7a79c1f5ba5416c6e9dfe15d554ac570a0731233b')

        # 查询当前所有正常上市交易的股票列表
        all_stocks = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

        #print(all_stocks)
        # 查询股票所属行业
        stock_industry = all_stocks[all_stocks['ts_code']=='600519.SH']
        
        # 筛选同行业股票
        same_industry_stock = all_stocks[all_stocks['industry']==stock_industry['industry'].values[0]]
        #print(same_industry_stock)
        #print(type(stock_industry['industry'].values[0]))
        
        
        # 筛选ROE>10的股票
        same_industry_stock_roe = pd.DataFrame()
        for stock in same_industry_stock.iterrows():
            #print(type(stock[1]["ts_code"]))
            # ROE>10%
            fina_indicator = pro.fina_indicator(ts_code=stock[1]["ts_code"]).head(1)
            
            ts_code = fina_indicator["ts_code"].values[0]
            roe = fina_indicator["roe"].values[0]
            if roe > 10:
                stock = [[ts_code, roe]]
                same_industry_stock_roe = same_industry_stock_roe.append(stock)
        print(same_industry_stock_roe)
        
        

        
if __name__ == "__main__":
    
    s = same_industry_stock()
    s.run()
    #print('开始交易日为：%s ;结束交易日为：%s ' % (start_date_open, end_date_open))

