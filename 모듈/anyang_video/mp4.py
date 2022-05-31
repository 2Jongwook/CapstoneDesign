#2022일03월 31일

#셀레니움 라이브러리
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#윈도우 cmd 라이브러리
import os
from tkinter import filedialog
import tkinter
import threading



#크롬 디버깅 모드로 실행
#시작하기전 cmd 창으로 chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeTest" 실행

def chrome_using():
    
    root=tkinter.Tk()
    root.withdraw()
    #chrome_url = filedialog.askdirectory(parent=root,initialdir="C:\\Program Files\\Google\\Chrome\\Application",title='크롬이 설치된 폴더 경로지정')
    os.chdir("C:\\Program Files (x86)\\Google\\Chrome\\Application")
    os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeTest"')


    


def anyang_url():
    #크롬디버깅 모드 멀티스레드
    tread1= threading.Thread(target=chrome_using)
    tread1.start()

    time.sleep(1)
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    #chrome_driver = '.\chromedriver.exe'
    driver = webdriver.Chrome(r"C:\Users\admin\Desktop\졸업프로젝트\graduation-project\모듈\셀레니움_(안양 크롤링)\chromedriver.exe", options= chrome_options)
    driver.get('https://cyber.anyang.ac.kr')
    print("3번을 눌러 강의다운")
    num = int(input())
    if(3==num):
        
        #안양대 사이버 강의실 접속

        
        #강의 보기 new 탭 핸들 선택
        #driver.window_handles[0] 
        driver.switch_to.window(driver.window_handles[1])

        #new 탭의 iframe 선택
        element = driver.find_element_by_tag_name('iframe')
        driver.switch_to.frame(element)
        url = driver.find_element_by_tag_name('video').get_attribute("src") #video scr 추출 
    

        print(url)

        
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        response = requests.get(url)
        with open('다운로드.mp4', 'wb') as f:
            f.write(response.content)

        print("다운로드 완료")


if __name__=='__main__':
    #chrome_using()
    anyang_url()
