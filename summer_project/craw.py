import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music.settings")
django.setup()
from demo.models import Singers, Songs
import requests
from bs4 import BeautifulSoup



header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "67.0.3396.99 Safari/537.36"}

singers = Singers.objects.all()[30012:]
for singer in singers:
    id = singer.singerid
    song_list = list()
    url = f"https://music.163.com/artist?id={id}"
    html = requests.get(url=url, headers=header).text
    soup = BeautifulSoup(html, 'lxml')

    id_list = soup.find('textarea').get_text()
    if len(id_list) == 1:
        continue
    singer_name = soup.find_all('meta')[5]['content']
    null = "null"
    false = "false"
    try:
        id_list = eval(id_list)
    except:
        continue
    for i in id_list:
        music_name = i['name']
        music_id = i['id']
        song_url = f'https://music.163.com/song?id={music_id}'
        song_list.append(Songs(songid=music_id, name=music_name, singer=singer, song_url=song_url))
    Songs.objects.bulk_create(song_list)
    print(str(round(((singer.id-1196023)/30149)*100, 5))+"%" + f"              {singer.id-1196023}")
