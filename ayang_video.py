#2022일03월 24일

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#시작하기전 cmd 창으로 chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeTest" 실행

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

s=Service('.\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)

#안양대 사이버 강의실 접속

#강의 보기 new 탭 핸들 선택
driver.window_handles[0] 
driver.switch_to.window(driver.window_handles[0])

#new 탭의 iframe 선택
element = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(element)
t2 = driver.find_element_by_tag_name('video').get_attribute("src") #video scr 추출


print(t2)