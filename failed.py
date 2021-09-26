class Backtesting(StockDB):

    #RuntimeWarning: invalid value encountered in double_scalars 연평균수익률=(기간수익률**(1/N))-1 #보통 0이 분모에 들어가는 등 계산 불능일 때 뜬다.
    def breakthrough_ETF(self,k,start): #etf는 index와 달리 거래가 거의 안이뤄지는 etf종목이 있으므로 그 etf를 제외한 분석을 하자
            HPR=[]
            CAGR=[]
            cursor=self.conn.cursor(pymysql.cursors.DictCursor)
            ETFtickers=stock.get_etf_ticker_list(str(datetime.date.today()).replace('-',''))
            # cursor.execute('select avg(거래량) from kr_etf')
            # result = cursor.fetchone()
            # vol_avg=result[0]
            for etf_id in ETFtickers:
                cursor.execute("select * from kr_etf where etf_id=%s and 날짜>date(%s) order by 날짜 asc",[etf_id,start])
                rows=cursor.fetchall()
                df=pd.DataFrame(rows)
                # print(df.dtypes)
                if df['거래량'].mean()>1000: # 값이 올라도 팔수 있기 위해 그리고 거래량은 시장의 관심을 나타내는 것이므로 그래서 평균거래량을 기준으로 K값을 선별한다.
                    print('거래가 거의 없는 종목')
                    continue
                elif len(df)<2:
                    print('신규 상장 ETF')
                    continue  #거래량이 0이라면 시가 고가 저가 값이 모두 0으로 저장됨
                
                print('b')
                df.set_index('날짜',inplace=True)
                df['변동폭']=df['고가']-df['저가'] #거래량이 0일경우 변동폭은 0
                df['목표가']=df['시가']+df['변동폭'].shift(1)*k #목표가는 다음날도 거래량 없다면 전날 변동폭*k또는 거래량 있으면 시가
                df['다음날시가']=df['시가'].shift(-1) 
                df.dropna(inplace=True) #당일은 다음날시가를 모르므로 NaN이 뜨기 때문
                cond=df['고가']>df['목표가'] #거래량 0으로 데이터가 없을 때가 반복되면 고가와 목표가가 0으로 같아지므로 무조건 수익내는 이상한 결과가 나오기때문에 고가보다 작은걸로 적자
                print('c')
                수익률=df.loc[cond,'다음날시가']/df.loc[cond,'목표가']
                if 수익률.empty: #밑의 k상수 구문에서 너무큰 상수라 매수매도가 1번도 안일어날 경우를 대비해 수익률변수가 비어있으면 1를 리턴
                    print('d')
                    return 1
                수익률=수익률-0.002 #수수료계산
                기간수익률=수익률.cumprod().iloc[-1]
                if 기간수익률==0:
                    continue
                N=(df.index[-1]-df.index[0]).days/365
                print(N)
                연평균수익률=(기간수익률**(1/N))-1
                print(N)
                # HPR.append(기간수익률.item())
                CAGR.append(연평균수익률)

            return CAGR
