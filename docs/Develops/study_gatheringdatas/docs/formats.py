# * 웹 크롤링 동작
from selenium import webdriver

# ChromeDriver 실행
browser = webdriver.Chrome('../chromedriver.exe')

# Chrome WebDriver의 capabilities 속성 사용
# capabilities = browser.capabilities

# # - chrome browser 열기
# browser = webdriver.Chrome() #class의 생성자와 같음/ return하면 class의 모든 자원이 return됨
# # Chrome WebDriver의 capabilities 속성 사용
# capabilities = browser.capabilities

# - 주소 https://www.w3schools.com/ 입력
html_file = browser.get("https://www.w3schools.com/") 

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

# - 정보 획득
pass 
# 브라우저 종료
browser.quit()