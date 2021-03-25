from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import requests
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe',options=options)#ChromeDriver位置
Date = time.time()
#driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")        
login = "https://passport.bilibili.com/login"       #登录页
logined = "https://passport.bilibili.com/account/security#/home"        #登录后地址1
HomeUrl = "https://www.bilibili.com/"       #登录后地址2
reply = "https://message.bilibili.com/#/reply"      #消息页
ReplyAt = 'https://message.bilibili.com/#/at'       #消息页-At

#登录部分,去除填写密码，改用cookie登录
#driver.get(login)
#driver.find_element_by_id("login-username").send_keys('')      #账号
#driver.find_element_by_id("login-passwd").send_keys('')       #密码
#driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()     #自动点击登录，记得手动通过验证
driver.get("https://www.bilibili.com/")
with open('cookies.txt','r', encoding='utf8') as f:
    listCookies = json.loads(f.read())
#添加cookies
for cookie in listCookies:
    cookie_dict = {
        'domain': '.bilibili.com',
        'name': cookie.get('name'),
        'value': cookie.get('value'),
        "expires": '',
        'path': '/',
        'httpOnly': False,
        'HostOnly': False,
        'Secure': False
    }
    driver.add_cookie(cookie_dict)
time.sleep(3)
driver.refresh()  # 刷新网页，完成登录
url  = driver.current_url
driver.get(ReplyAt)     #进入at页
        
#NewUrl  = driver.current_url
#主程序，循环扫描@信息
def main():
    while(1):
        info = open('info.txt',"a+")        #打开、新建info文件
        info.seek(0.0)
        info = info.read()
        driver.get(ReplyAt)
        time.sleep(3)
        try :
            driver.find_element_by_xpath('//*[@id="link-message-container"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[3]')
            #time.sleep(1)
            driver.find_element_by_xpath('//*[@id="link-message-container"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[3]').click()      #点击最新一条@信息
            handles = driver.window_handles
            driver.switch_to.window(handles[1])
            NewUrl = driver.current_url
            if(NewUrl in info):
                driver.close()
                driver.switch_to.window(handles[0])
            elif(NewUrl not in info):
                info = open('info.txt',"a+")
                print("[Date]",Date,NewUrl,file=info)
                time.sleep(0.5)
                #一言Api
                ApiUrl = "https://v1.hitokoto.cn/?c=a&c=f&c=k&encode=text"
                hitokoto = requests.get(ApiUrl).text
                time.sleep(4)
                try:
                    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[1]/div[1]')
                    #获取用户名
                    UsrName = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div/div[1]/div[1]").get_attribute('innerText')
                    print(UsrName)  
                    try:
                        driver.find_elements_by_class_name("dynamic-repost-checkbox")
                        driver.find_element_by_class_name("dynamic-repost-checkbox").click()
                        driver.find_element_by_class_name("ipt-txt").send_keys('@%s %s——来自自动转发'%(UsrName,hitokoto))     #回复信息
                        time.sleep(0.5)
                        driver.find_element_by_class_name("comment-submit").click()     #点击回复
                        time.sleep(0.5)
                        driver.close()
                        driver.switch_to.window(handles[0])
                    except:
                        pass
                except:
                    pass
        except:
            pass
main()
input('回车键退出')