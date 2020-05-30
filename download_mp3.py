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

songNames = []


def create_list(url):
    a = requests.get(url)
    instance = lxml.html.fromstring(a.content)
    for i in range(2, 12):
        songNames.append(instance.xpath(path.replace('[]', f'[{i}]'))[0].values()[2])


def songlist_print():
    for index, name in enumerate(songNames):
        print(index + 1, ') ', name)


def download(title):
    subprocess.call(["youtube-dl", "--extract-audio",
                     "--audio-format mp3", "--output",
                     "%(title)s.%(ext)s", f"ytsearch: '{title}'"])


if __name__ == '__main__':
    for url in [page1, page2, page3, page4]:
        create_list(url)
    for i in songNames:
        download(i)
        print(i, ' has been downloaded.')
    songlist_print()
