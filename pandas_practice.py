#pd.read_html(url)로 해도 없다면(이유:table태그만 불러오거나 다른 request url를 가지고 있음) 네트워크에서 XHR,JS,Doc중에서 찾아볼수 있다.
import pandas as pd
import requests

item_code='352820'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
url=f'https://finance.naver.com/item/sise_day.nhn?code={item_code}&page=1'
# res=requests.get(url,headers=headers)
# tb=res.content.decode('euc-kr')
# table=pd.read_html(tb,header=0)
table=pd.read_html(requests.get(url,headers=headers).text, encoding='cp949')
temp=table[0]

read_html은 url의 table를 가져옴
현 코드는 requests로 url에 있는 text를 사용자인척 가져온 후 기계어 번역 후 read_html로 table를 추출

#에서의 상황은 네이버주식에서 거부한상태여서 컴퓨터인척하고 request후에 그것을 파이썬에 쓸수있도록 내용을 디코드후
그 url에서의 table를 pd.read_html로 읽어들인다
table내에서의 공백과 줄은 NaN표시

# table=pd.read_html(url,encoding='cp949') 
# len(table)
temp.dropna(how='all',axis=0).iloc[:5] #모든 행의 데이터가 결측치인 행 드랍(디폴트값임)
#ETF JSON형식 불러오기 (JSON형식은 딕셔너리 형식으로 표현됨 )
import pandas as pd
import numpy as np
import requests
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
url='https://finance.naver.com/api/sise/etfItemList.nhn?etfType=0&targetColumn=market_sum&sortOrder=desc'
res=requests.get(url,headers=headers)
res
#request의 응답을 json 타입으로 받음
etf_json=res.json() 
#result > etfItemList의 하위 구조로 데이터를 가져옴
etfItemList=etf_json['result']['etfItemList']
len(etfItemList)
json으로 불러오기에는 앞에 callback값이 있기 때문에 url에서 callback값을 지워주면 해결
df=pd.DataFrame(etfItemList)
df.shape #행과 열의 수
df.head()
df.tail()
'''(1) pandas DataFrame의 칼럼 이름 바꾸기
    :  df.columns = ['a', 'b']
    :  df.rename(columns = {'old_nm' : 'new_nm'}, inplace = True)

(2) pandas DataFrame의 인덱스 이름 바꾸기
    : df.index = ['a', 'b']
    : df.rename(index = {'old_nm': 'new_nm'}, inplace = True)
'''
df.columns='종목코드	etfTabCode	종목명	현재가	risefall	등락값	등락률	nav	3개월수익률	거래량	거래대금	시가총액'.split('\t')
df
import datetime

today=datetime.datetime.today()
today=today.strftime('%Y-%m-%d')
today
file_name=f'etf_{today}_raw.csv'
file_name
#CSV형태로 저장하고 index가 저장되지 않도록 한다.
df.to_csv(file_name,index=False)
#저장된 csv파일을 읽어줍니다.file_name
#종목코드의 숫자 앞의 0이 지워진다면 dtype={"종목코드":np.object}로 타입을 지정해 주면 문자형태로 읽어옵니다.
pd.read_csv(file_name,dtype={"종목코드":np.object}) #숫자가 아닌 문자로 불러와라
