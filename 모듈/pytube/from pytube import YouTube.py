import os
from pytube import YouTube

DOWNLOAD_FOLDER = os.chdir(os.path.dirname(os.path.abspath(__file__)))
print('다운로드할 Youtube url을 복사해서 적어주세요.')
url = input()
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)
print("다운로드 완료")