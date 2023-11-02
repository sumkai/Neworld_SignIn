from selenium import webdriver
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from notify import send
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# 配置Chrome选项
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 创建Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# 从环境变量中读取用户名和密码
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")

print(username)

if not username or not password:
    print("请设置USERNAME和PASSWORD环境变量。")
    driver.quit()
    exit(1)

# 导航到登录页面
driver.get("https://neworld.tv/auth/login")

# 输入用户名和密码
driver.find_element(By.ID, 'email').clear()
driver.find_element(By.ID, 'email').send_keys(username)
driver.find_element(By.ID, 'passwd').clear()
driver.find_element(By.ID, 'passwd').send_keys(password)

# 点击登录按钮
driver.find_element(By.ID, 'login-dashboard').click()

# 等待页面加载
time.sleep(10)

check_in_button = driver.find_element(By.ID, 'check-in')
driver.execute_script("arguments[0].click();", check_in_button)

# 获取"Check-In"按钮的文本
check_in_text = driver.find_element(By.CSS_SELECTOR, '[id*=check-in]').text

# 查找包含特定文本的元素
used = driver.find_element(By.XPATH, '//span[contains(text(),"过去")]')
today = driver.find_element(By.XPATH, '//span[contains(text(),"今日")]')
rest = driver.find_element(By.XPATH, '//span[contains(text(),"剩余")]')
timerest = driver.find_element(By.XPATH,  '//*[contains(text(),"到期")]')

# 提取文本内容并去除空格和换行符
used_text = used.text.strip()
today_text = today.text.strip()
rest_text = rest.text.strip()
timerest_text = timerest.text.strip()

# 合并文本内容为一个多行字符串
content = f"{check_in_text}\n{used_text}\n{today_text}\n{rest_text}\n{timerest_text}"

print(content)

# 在这里添加通知的代码
send ("新界"+check_in_text,content)


# 退出浏览器
driver.quit()
