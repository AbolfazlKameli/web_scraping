import requests
from bs4 import BeautifulSoup
import re

qualities = {
    '144': 0,
    '240': 1,
    '360': 2,
    '480': 3,
    '720': 4,
    '1080': 5,
}


class VideoDownloadException(Exception):
    ...


class QualityError(VideoDownloadException):
    ...


class Scraper:
    def __init__(self, url, quality):
        self.url = url
        self.quality = quality

    def get_link(self):
        links = self.get_all_links()
        available_qualities = self.get_qualities()
        if self.quality not in available_qualities:
            raise QualityError(f'This quality is not available \navailable qualities: {available_qualities}')
        link = links[qualities[self.quality]]
        return link

    def get_all_links(self):
        result = requests.get(self.url)
        content = BeautifulSoup(result.text, features='html.parser')
        video_links = content.find_all('a', href=re.compile(r'^(https:\/\/www\.namasha\.com\/videos\/dl)(\S+).mp4$'))
        links = [link['href'] for link in video_links]
        links.reverse()
        return links

    def get_qualities(self):
        links = self.get_all_links()
        qua = list(qualities.keys())
        available_qualities = [qua[i] for i in range(len(links))]
        return available_qualities


class Main:
    def __init__(self, url, quality):
        self.url = url
        self.quality = quality
        self.scraper = Scraper(self.url, self.quality)

    def download(self):
        video_url = self.scraper.get_link()
        with open('video.mp4', 'wb') as f:
            print('Downloading...')
            result = requests.get(video_url, stream=True)
            total = result.headers.get('content-length')
            if total is None:
                f.write(result.content)
            else:
                download = 0
                total = int(total)
                for data in result.iter_content(chunk_size=4096):
                    f.write(data)
                    download += len(data)
                    done = int(100 * (download / total))
                    print('\r[{}:{}{}]'.format(done, '=' * done, ' ' * (100 - done)), end='')
        print('\nvideo downloaded.')


a = Main(url='https://www.namasha.com/v/h7zIlio2', quality='144')
a.download()
