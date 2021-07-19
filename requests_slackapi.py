# from slacker import Slacker

# slack=Slacker('xoxb-2309182764752-2282474884965-yxSzBxkebXFKw1XQJDqhX9lS')

# # Send a message to #general channel
# slack.chat.post_message('#stock', 'Hello fellow slackers!')
'''slacker라이브러리 사용금지됨'''
#-OAuth: https://opentutorials.org/module/3668/22008
import requests
 
#이거 말고 다양한 api메서드가 있으며 사용법은 slack에서 제공해준다.
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage", 
#-여기서 method url(메서드는chat.postMessage)이 쓰인다.post요청은 양식에서 데이터를 제출하거나 파일을 업로드할때 사용
        headers={"Authorization": "Bearer "+token,
            'Content-type': 'application/x-www-form-urlencoded'}, #-'헤더(header)'는 데이터 파일에서 여러 가지 값들이 어떤 의미를 갖는지 표시한 행
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2309182764752-2284865086149-i0bIl33tZSkKIojnonnb3qlD"
 
post_message(myToken,"#stock","이게 될까?")
