
from selenium import webdriver
from time import sleep
import json
if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://passport.bilibili.com/login')
    sleep(50)
    dictCookies = driver.get_cookies()  # 获取list的cookies
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存
    with open('cookies.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')