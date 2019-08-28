import requests
import lxml.html
import youtube_dl
import subprocess

page1 = 'https://www.numberone.com.tr/muzik/number-one-top-40/'
page2 = page1 + 'page/2/'
page3 = page1 + 'page/3/'
page4 = page1 + 'page/4/'

# opt = ['--extract-audio', '--audio-format', 'mp3', '--output', '%(title)s.%(ext)s']

path = '/html/body/div[2]/div/div[1]/div[]/div/div[3]/h2/a[2]'

song_names = []


def create_list(url):
    a = requests.get(url)
    instance = lxml.html.fromstring(a.content)
    for i in range(2, 12):
        song_names.append(instance.xpath(path.replace('[]', f'[{i}]'))[0].values()[2])


def songlist_print():
    for i in range(len(song_names)):
        print(i + 1, ') ', song_names[i])


def download(title):
    subprocess.call(["youtube-dl", "--extract-audio",
                     "--audio-format mp3", "--output",
                     "%(title)s.%(ext)s", f"ytsearch: '{title}'"])


if __name__ == '__main__':
    create_list(page1)
    create_list(page2)
    create_list(page3)
    create_list(page4)
    for i in song_names:
        download(i)
        print(i, ' has been downloaded.')
    songlist_print()
