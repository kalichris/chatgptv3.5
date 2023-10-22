import requests
import urllib.parse
import re 
from bs4 import BeautifulSoup
import json 

class MainPost():
    def __init__(self,text):
        self.text=text
        self.filterDataSession()
        self.sendReqestes()
    def encodeTextUrl(self,text_url):
        urlEncode=urllib.parse.quote(text_url)
        return urlEncode

    def getCookies(self):
        cookies = {
            '_ga': 'GA1.1.1561920294.1697905578',
            'session-fetch-id': '3epucx81apzg',
            'session-accept-id': 'Mm2VL1OrDFOhcHpnOzIwMjMtMTAtMjEgMTc6NTE6MjU=',
            '_ga_6DK6S98B8Q': 'GS1.1.1697916921.2.1.1697916948.0.0.0',
            '__gads': 'ID=51f3de8ae9893201:T=1697905576:RT=1697916950:S=ALNI_MZTRrfwCQ-YrWIkiwxrk-QjjNkNSA',
            '__gpi': 'UID=00000cbe2157d82d:T=1697905576:RT=1697916950:S=ALNI_Mbkv7zKL5pdUkcUmrpGGRJCyOyKqw',
            'FCNEC': '%5B%5B%22AKsRol-rQpt1K4KIHNt5zBsDZAPhKchGgc2mN4714_rissbbMsH5LVdjosoOR_m_YjW67J5huia6ErylLovwFrI_JNoyrUm9gg8OaRTmBQqL4ilG0ho6FCqs9yjvonUEjjiVX7Zc9SMFvRS0u6bKn7Lz6MeqJuFpOg%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
        }

        headers = {
            'authority': 'chatgpt1s.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': '_ga=GA1.1.1561920294.1697905578; session-fetch-id=3epucx81apzg; session-accept-id=Mm2VL1OrDFOhcHpnOzIwMjMtMTAtMjEgMTc6NTE6MjU=; _ga_6DK6S98B8Q=GS1.1.1697916921.2.1.1697916948.0.0.0; __gads=ID=51f3de8ae9893201:T=1697905576:RT=1697916950:S=ALNI_MZTRrfwCQ-YrWIkiwxrk-QjjNkNSA; __gpi=UID=00000cbe2157d82d:T=1697905576:RT=1697916950:S=ALNI_Mbkv7zKL5pdUkcUmrpGGRJCyOyKqw; FCNEC=%5B%5B%22AKsRol-rQpt1K4KIHNt5zBsDZAPhKchGgc2mN4714_rissbbMsH5LVdjosoOR_m_YjW67J5huia6ErylLovwFrI_JNoyrUm9gg8OaRTmBQqL4ilG0ho6FCqs9yjvonUEjjiVX7Zc9SMFvRS0u6bKn7Lz6MeqJuFpOg%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
            'referer': 'https://chatgpt1s.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'session-fetch-id': 'mg0khsei9',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        response = requests.get('https://chatgpt1s.com/genkey', cookies=cookies, headers=headers)
        response_data=response.text
        session_cookies=response.cookies
        return response_data, session_cookies

    def filterDataSession(self):
        data_respone,cookie=self.getCookies()
        filter_data=json.loads(data_respone)['data']
        filter_cookies=str(cookie)
        filter_cookies =filter_cookies.replace("<RequestsCookieJar[", "").replace("]>", "").replace('<Cookie',"").replace("/>","").replace(" for chatgpt1s.com","")
        cookies_f={}
        for cookie in filter_cookies.split(","):
            name, value = cookie.strip().split("=")
            cookies_f[name] = value
        cookies_j = json.dumps(cookies_f)
        XSRF_TOKEN_cookie=json.loads(cookies_j)['XSRF-TOKEN']
        tool_chatgpt1s_session_cookie=json.loads(cookies_j)['tool_chatgpt1s_session']
        return XSRF_TOKEN_cookie,tool_chatgpt1s_session_cookie,filter_data
    def sendReqestes(self):
        xsre,toolChat,token=self.filterDataSession()
        cookies = {
            '_ga': 'GA1.1.1561920294.1697905578',
            '__gads': 'ID=51f3de8ae9893201:T=1697905576:RT=1697905576:S=ALNI_MZTRrfwCQ-YrWIkiwxrk-QjjNkNSA',
            '__gpi': 'UID=00000cbe2157d82d:T=1697905576:RT=1697905576:S=ALNI_Mbkv7zKL5pdUkcUmrpGGRJCyOyKqw',
            'FCNEC': '%5B%5B%22AKsRol9G9QEM4ILuBhZ1taZw3vmy_JuULsNqpDGNlwOefyuma6RqWv1KOiG3nocS8u6leqk1HfrGSzxpYnrbWRANoMY_G1Haoa1-3lEvs6i5a6phySqBKD1f-mia9xqYck90a0d7emufXFqyPH1bir4Yu9gZ71mxHQ%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
            '_ga_6DK6S98B8Q': 'GS1.1.1697905578.1.1.1697905620.0.0.0',
            #'XSRF-TOKEN':xsre,
            'XSRF-TOKEN':'eyJpdiI6Imc2TXVua290NHJ2L2kybXorWHZCUEE9PSIsInZhbHVlIjoiaC9kNlc1NE9QTHdDRDRwRWRXWWdobzZ4Tk1zaW9DWStwNGdQekFvZHUwQ0JMODdKcG4yd2JYaEdxKzQzaUJmSmNja0VjNkoxZlBxTm52NWJyWDduaFZ0K1ZWZVlxYm41a0VodWlXN2dHajRxQVgvbDc1ZEVLbVZBSCtqdFJIc1oiLCJtYWMiOiIxMWI3YWJkZmExMTgwYzc2M2YyMWI0YmEwZTAwMWE3M2NjNjdmYzhhYTg0MGY2MTY0ZTI0MDliOGY4OWVkMTdkIiwidGFnIjoiIn0',
            #'tool_chatgpt1s_session':toolChat,
             'tool_chatgpt1s_session':'eyJpdiI6Ik5hcUhNVlAwelo2VlF0ZjQ2NEN0eVE9PSIsInZhbHVlIjoiMzVPZ0Z6SXF0cFdzMmxKdGJvUG4xZTd2S0VmQ0llTWlDQ2YyeWgwVmVWbkRrSWV1MStVVHZnRGRRNHdKU0lPejR1YkxzWFNoU3d2aURBdlg4QzU2Mjh3SnBZNkJRQUJBU3dPZUJ2WUc0em5UajYxZWFwVk1XWFdFVzloTFR0YWgiLCJtYWMiOiIyM2YzYzZhZDgzYzBjZWVkY2Y4YTAzYjlmMjA5MzU1NTIxYzM2YTQyMmZjMGIwNzgyZDRkNTE0ZjU3YjNlMGUxIiwidGFnIjoiIn0',
            #'session-fetch-id': 'fe577bm0jgp2;',
            'session-fetch-id': 'ejomkgx5q9cb',
            #'session-accept-id': token,
            'session-accept-id': 'ZsWpFte2DV7xOWNiOzIwMjMtMTAtMjIgMTU6MTA6NDE',
        }

        headers = {
            'authority': 'chatgpt1s.com',
            'accept': 'text/event-stream',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'referer': 'https://chatgpt1s.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }
        textSend=self.encodeTextUrl(self.text)
        url="https://chatgpt1s.com/ask?question="+textSend
        response = requests.get(
             url,
            cookies=cookies,
            headers=headers,
        )
        textUn=response.text
        filter_text= re.findall(r'event: update\ndata: (.*?)\n', textUn) 
        text = "".join(filter_text)
        print(text)



MainPost("what is python")


