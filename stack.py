import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://stackoverflow.com/questions/tagged/python',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, 질문 list 불러오기

stacks = soup.select('#questions > .question-summary > .summary')

# stacks (list들) 의 반복문을 돌리기
for stack in stacks:
    title = stack.select_one('h3 > .question-hyperlink')
    print(title.text)
    print('http://stackoverflow.com' + title.get('href'))

