class StockDB():
    #__init__으로 객체의 초기값을 정해준다. 가장 우선적임.
    def __init__(self, password):
        index_tickers_kospi=stock.get_index_ticker_list()
        index_tickers_kosdaq=stock.get_index_ticker_list(market='KOSDAQ')
        self.index_tickers=index_tickers_kospi+index_tickers_kosdaq
        self.engine = create_engine("mysql+pymysql://root:"+password+"@127.0.0.1:3306/etf_stock", encoding='utf-8')
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password=password, db='etf_stock', charset='utf8')
        self.cursor = self.conn.cursor()

    def insert_chart(self,data,table_name):
        data.to_sql(name=table_name, con=self.engine, if_exists='append')
        self.conn.commit()

    def updateETF1(self,start): 
        ETFtickers=stock.get_etf_ticker_list(str(datetime.date.today()).replace('-',''))
        df=pd.DataFrame(columns=['날짜','NAV','시가','고가','저가','종가','거래량','거래대금','기초지수']) 
        df.set_index('날짜',inplace=True) 
        for ticker in ETFtickers[:250]:
            df1=stock.get_etf_ohlcv_by_date(start,str(datetime.date.today()).replace('-',''),ticker)
            if df1.empty: # (df1.index[-1] != '2021-09-17')는 애초에 오늘기준으로 존재하는 etf중에서 df만드는 것이므로 의미가 없다.
                continue
            else:
                df1['etf_id']=ticker
                df1['etf_name']=stock.get_etf_ticker_name(ticker) #map은 하나하나 value에 접근하여 실행하기 때문에 수십만건의 mapping을 동시에 실행하면 차단먹는다.
                df=pd.concat([df,df1])   
                time.sleep(0.5)
        self.insert_chart(df,'kr_etf')

    def updateETF2(self,start): # ETFtickers[360]에서 오류가 난다.. 난다요~
        ETFtickers=stock.get_etf_ticker_list(str(datetime.date.today()).replace('-',''))
        df=pd.DataFrame(columns=['날짜','NAV','시가','고가','저가','종가','거래량','거래대금','기초지수']) 
        df.set_index('날짜',inplace=True) 
        for ticker in ETFtickers[250:400]:
            df1=stock.get_etf_ohlcv_by_date(start,str(datetime.date.today()).replace('-',''),ticker)
            if df1.empty: # (df1.index[-1] != '2021-09-17')는 애초에 오늘기준으로 존재하는 etf중에서 df만드는 것이므로 의미가 없다.
                continue
            else:
                # df1.apply(lambda x: x.astype(str).str.strip("\'"), axis=1)
                # df1=df1.apply(pd.to_numeric,errors='coerce',axis=1).dropna()
                df1['etf_id']=ticker
                df1['etf_name']=stock.get_etf_ticker_name(ticker) #map은 하나하나 value에 접근하여 실행하기 때문에 수십만건의 mapping을 동시에 실행하면 차단먹는다.
                df=pd.concat([df,df1])   
                time.sleep(0.5)
        # df['NAV']=pd.to_numeric(df['NAV'],error='coerce',downcast='float')            
        # df['기초지수']=pd.to_numeric(df['기초지수'],error='coerce',downcast='float')
        # df['시가']=pd.to_numeric(df['시가'],error='coerce',downcast='integer')
        # df['고가']=pd.to_numeric(df['고가'],error='coerce',downcast='integer')
        # df['저가']=pd.to_numeric(df['저가'],error='coerce',downcast='integer')
        # df['종가']=pd.to_numeric(df['종가'],error='coerce',downcast='integer')
        # df['거래량']=pd.to_numeric(df['거래량'],error='coerce',downcast='integer')
        # df['거래대금']=pd.to_numeric(df['거래대금'],error='coerce',downcast='integer')
        # df=df.apply(pd.to_numeric,errors='coerce',downcast='float')
        self.insert_chart(df,'kr_etf')

    def updateETF3(self,start): 
        time.sleep(60)
        ETFtickers=stock.get_etf_ticker_list(str(datetime.date.today()).replace('-',''))
        df=pd.DataFrame(columns=['날짜','NAV','시가','고가','저가','종가','거래량','거래대금','기초지수']) 
        df.set_index('날짜',inplace=True) 
        for ticker in ETFtickers[400:]:
            df1=stock.get_etf_ohlcv_by_date(start,str(datetime.date.today()).replace('-',''),ticker)
            if df1.empty: # (df1.index[-1] != '2021-09-17')는 애초에 오늘기준으로 존재하는 etf중에서 df만드는 것이므로 의미가 없다.
                continue
            else:
                df1['etf_id']=ticker
                df1['etf_name']=stock.get_etf_ticker_name(ticker) #map은 하나하나 value에 접근하여 실행하기 때문에 수십만건의 mapping을 동시에 실행하면 차단먹는다.
                df=pd.concat([df,df1])   
                time.sleep(0.5)
        self.insert_chart(df,'kr_etf')


a=StockDB('password')
# df=a.updateETF1('20000101')
# df1=a.updateETF2('20000101')
df=a.updateETF2('20000101')
