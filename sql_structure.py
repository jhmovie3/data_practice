import pymysql
import numpy as np

'''

'''
a=[None]
print(a[0])
# None


print(type(pymysql.NULL))
# str

print(type(np.nan))
# float

print(type(None))
# NoneType
      
def updatestock(self,start,indexTicker): #indexTicker에 기본값으로 1002을 집어넣으면 unboundlocalerror: 발생
        stock_tickers=stock.get_index_portfolio_deposit_file(indexTicker)

        try: #table에 해당하는 index_id가 없으면 오류 발생
            sql='select max(날짜) from kr_stock where index_id=%s'
            self.cursor.execute(sql,indexTicker) 
            result=self.cursor.fetchone()
            updateStock=result[0]    #(None,)이라면 None반환 밑코드에서 오류뜸(None은 연산이 안되므로)
            stock_table=stock.get_market_ohlcv_by_date(str(updateStock+datetime.timedelta(days=1)).replace('-',''),str(datetime.date.today()).replace('-',''),stock_tickers[0])
            
            stock_table['stock_id']=stock_tickers[0]

            for i,ticker in enumerate(stock_tickers):
                if i>0:
                    df=stock.get_market_ohlcv_by_date(str(updateStock+datetime.timedelta(days=1)).replace('-',''),str(datetime.date.today()).replace('-',''),ticker)
                    df['stock_id']=ticker
                    stock_table=pd.concat([stock_table,df])
                    time.sleep(0.25)

        except:
            for i,ticker in enumerate(stock_tickers):
                if i==0:
                    stock_table=stock.get_market_ohlcv_by_date(start,str(datetime.date.today()).replace('-',''),ticker)
                    stock_table['stock_id']=ticker
                else:
                    df=stock.get_market_ohlcv_by_date(start,str(datetime.date.today()).replace('-',''),ticker)
                    df['stock_id']=ticker
                    stock_table = pd.concat([stock_table,df])
                    time.sleep(0.25)
            stock_table['index_id']=indexTicker
            print(stock_table)
        # else: #이 부분은 어떠한 오류나 예외가 발생하지 않았을 경우 실행
            self.insert_chart(stock_table,'kr_stock')
