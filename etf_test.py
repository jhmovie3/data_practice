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
from selenium import webdriver
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

LOGIN_INFO={
    'id':'jhmovie3',
    'pw':'Wogh0902!@#'
}
with requests.Session() as s:
    login_req=s.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com",params=LOGIN_INFO)
    print(login_req.text)