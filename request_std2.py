import requests
from bs4 import BeautifulSoup
import re


def query_title(query,page,filter): #짧은시간에 너무 많은 양의 정보를 요청해서 서버에서 차단먹음..
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
    url='https://www.google.com/search'
    query_page=f"?q={query}&start={(page-1)*10}" #10단위로 페이지나오므로 인덱스형식으로 나오므로 -1해준다.
    
    res=requests.get(url+query_page,headers=headers)
    print(res.url) #GET요청이므로 ttps://www.google.com/search?q=requests+%EC%9D%B8%EC%BD%94%EB%94%A9로 퍼센트인코딩해서 나옴 클릭하면 검색된 결과가 나온다.
    # print(res.encoding) 
    '''
    ISO-8859-1로 영문인코딩이므로 다른언어는 깨진다. 
    하지만 구글에서 요청받을때 알아서 인코딩해주는것같아서 굳이 인코딩 바꿔주지 않아도 된다. 
    # '''
    search_title=[]
    soup=BeautifulSoup(res.text,'lxml')
    html_titles=soup.find_all('h3') #h3태그가진 것 html형태로 리스트에 저장
    # search_title=[html_title.text for html_title in html_titles if filter in html_title]
    for html_title in html_titles: #리스트에서 h3가진 html형식하나씩 뽑음
        # print(title.text)
        p=re.search(filter,html_title.text) #한개의 html형식에서 텍스트 추출
        if p:
            search_title.append(html_title.text)
    


        # if m:
        #     return m.string
    return search_title
    

print(query_title('광주광역시',2,'시청'))
