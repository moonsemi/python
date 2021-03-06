import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
for i in range(1,5):
    data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200128&hh=21&rtm=N&pg='+str(i), headers=headers)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(data.text, 'html.parser')

    # select를 이용해서, tr들을 불러오기
    musics = soup.select('.music-list-wrap > .list-wrap > tbody > .list')

    # musics (tr들) 의 반복문을 돌리기
    for music in musics:
        rank = music.select_one('td.number').text.split(' ')[0].strip()
        title = music.select_one('td.info > a.title').text.strip()
        artist = music.select_one('td.info > a.artist ').text.strip()
        print(rank, title, artist)
