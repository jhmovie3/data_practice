'''requests.get의 params이란? 튜플(tuple), 딕셔너리(dict)형식으로 매개변수에 넣으면 양식이 URL 인코딩이 되어 URL에 추가
   ex) requests.get(http://httpbin.org/get,params={'firstName':'John','lastName':'Smith'})
   = http://httpbin.org/get?firstName=John&lastName=Smith에서 Parameter Names는 firstName,lastName이고 value는 John,Smith이다.'''

'''requests.post의 data란? 튜플(tuple), 딕셔너리(dict)형식으로 매개변수에 넣으면 양식이 인코딩되어 요청 본문에 추가됨
   ex) requests.post('http://httpbin.org/post',data={'firstName':'John','lastName':'Smith'})
   http post프로토콜을 사용할때 get과 다르게 매개변수가 url로 인코딩되지 않고 사전형식으로 전달한다.'''

'''encoding이란? 정보를 암호화 시킨다라는뜻
각 언어별로 번호 체계가 다르다. 
한글 윈도우의 메모장으로는 "한글 완성형 텍스트 파일"을 읽을 수 있지만 "일본어 Shift-JIS 텍스트"는 읽을 수가 없다. 
메모장이 일본어 인코딩을 인식하지 못하기 때문'''

#-requests 분석참고 'https://me2nuk.com/Python-requests-module-example/'
import requests
from bs4 import BeautifulSoup
import re

# res=requests.post('http://httpbin.org/post',data={'sibal':'John','tlqkf':'Smith'})
# print(res.text) #form에 data가 저장

# res=requests.get('http://httpbin.org/get?',params={'sibal':'John','tlqkf':'Smith'})
# print(res.text) #args에 params이 저장

# res=requests.post('https://www.naver.com/',data={'korea':'hip'})
# print(res.url)
# #여기서 q는 검색어 입력 키이므로 이 url클릭하면 value가 담긴 검색창이 뜬다.
# res=requests.get('https://www.google.com/',params={'q':'python'})
# print(res.url)

# options=webdriver.ChromeOptions()
# options.add_argument('window-size=1920,1080')

# driver=webdriver.Chrome('chromedriver.exe',options=options)

def query_title(query,page,filter): #짧은시간에 너무 많은 양의 정보를 요청해서 서버에서 차단먹음..
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
    url='https://www.google.com/search'
    query_page=f"?q=query&start={(page-1)*10}" #10단위로 페이지나오므로 인덱스형식으로 나오므로 -1해준다.
    
    res=requests.get(url+query_page,headers=headers)
    print(res.url) #GET요청이므로 ttps://www.google.com/search?q=requests+%EC%9D%B8%EC%BD%94%EB%94%A9로 퍼센트인코딩해서 나옴 클릭하면 검색된 결과가 나온다.
    # print(res.encoding) 
    '''
    ISO-8859-1로 영문인코딩이므로 다른언어는 깨진다. 
    하지만 구글에서 요청받을때 알아서 인코딩해주는것같아서 굳이 인코딩 바꿔주지 않아도 된다. 
    # '''
    
    soup=BeautifulSoup(res.text,'lxml')
    titles=soup.find_all('h3') #h3태그가진 것 html형태로 리스트에 저장
    print(titles)
    search_title=[title.text for title in titles if filter in title]
    # for title in titles: #리스트에서 h3가진 html형식하나씩 뽑음
    #     # print(title.text)
    #     p=re.search(filter,title.text) #한개의 html형식에서 텍스트 추출
    #     if p==-1:
    #         print('\n\n')
    #     else:
    #         search_title.append(title.text)
    


        # if m:
        #     return m.string
    return search_title
    
    '''page가 바뀔때마다 어떤 요소가 규칙적으로
    바뀌는지 확인해보니 start=0,10,20,30...
    라는것이 변하고 있었으므로 url에 start라는 변수를 넣어주었더니 페이지가 바뀐다.'''
    # q: d
    # ei: d_HzYPnLJ4OK-Qbt9ruABA
    # start: 20
    # sa: N
    # ved: 2ahUKEwi54_-5pOzxAhUDRd4KHW37DkA4ChDy0wN6BAgBEDw
    # cshid: 1626599892848027
    # biw: 310
    # bih: 670

    # q: d
    # ei: 5fHzYLrzJJiC1e8Po5if0AM
    # start: 30
    # sa: N
    # ved: 2ahUKEwj6-bbupOzxAhUYQfUHHSPMBzo4FBDy0wN6BAgBED4
    # biw: 310
    # bih: 670
    # dpr: 1.25


query_title('광주광역시',2,'광주')

# page=1 

# while page<14:
#     print(query_title('광주',page,'광주'))
#     page+=1






