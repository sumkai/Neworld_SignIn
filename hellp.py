from selenium import webdriver
import time
import json
import os
import subprocess
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from notify import send

# 虚拟出Chrome界面
chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# action  linux服务器驱动地址
driver = webdriver.Chrome(options=chrome_options)  
# windows 系统驱动路径
# driver = webdriver.Chrome(executable_path='D:\Downloads\chromedriver_win32\chromedriver.exe')    # Chrome浏览器

# 环境变量中读取数据，包含账号密码，和登陆页面测试
u = os.environ["USERNAME"]
p = os.environ["PASSWORD"]

print('u',u)
print('p',p)
driver.get("https://neworld.tv/auth/login") 
#  获取cookies 
time.sleep(5)
# 账号密码登录版本
driver.find_element(By.ID, value='email').clear()
driver.find_element(By.ID, value="email").send_keys(u)
driver.find_element(By.ID, value='passwd').clear()
driver.find_element(By.ID, value="passwd").send_keys(p)
#driver.find_element_by_id('email').clear()
#driver.find_element_by_id("email").send_keys(u)
#driver.find_element_by_id('passwd').clear()
#driver.find_element_by_id("passwd").send_keys(p)
time.sleep(1)
driver.find_element(By.ID, value="login-dashboard").click()
driver.refresh()#刷新页面 
driver.refresh()#刷新页面 
time.sleep(2)


# 设置固定延迟为2秒
delay = 2

# 使用 CSS_SELECTOR 和包含 "check-in" 字符串的属性选择器
button = driver.find_element(By.CSS_SELECTOR, '[id*=check-in]')

# 添加固定延迟
time.sleep(delay)

# 执行点击操作
driver.execute_script("arguments[0].click()", button)

#driver.execute_script("(arguments[0]).click()",button)
text = button.text

print(text)

# 查找包含特定文本的元素
used = driver.find_element(By.XPATH, '//span[contains(text(),"过去")]')
today = driver.find_element(By.XPATH, '//span[contains(text(),"今日")]')
rest = driver.find_element(By.XPATH, '//span[contains(text(),"剩余")]')
timerest = driver.find_element(By.XPATH,  '//*[contains(text(),"到期")]')

# 提取文本内容并去除空格和换行符
usedtext = used.text.strip()
todaytext = today.text.strip()
resttext = rest.text.strip()
timeresttext = timerest.text.strip()

# 合并文本内容为一个多行字符串
content = f"{usedtext}\n{todaytext}\n{resttext}\n{timeresttext}"

print(content)

send ("新界"+text,content)

driver.quit()
