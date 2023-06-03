import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
import time


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import undetected_chromedriver as uc

from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

s = Service(executable_path=r'driver\chromedriver1.exe')
url_steam = 'https://store.steampowered.com/join'
options = webdriver.ChromeOptions()
# options.headless = True
user_agent_string = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
options.add_argument(f'user-agent={user_agent_string}')
options.add_argument("--disable-blink-features=AutomationControlled")
caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  complete
caps["pageLoadStrategy"] = "eager"  #  interactive
# caps["pageLoadStrategy"] = "none"   #  undefined
driver = uc.Chrome(desired_capabilities=caps, service=s, options=options)

file1 = open('accs.txt', 'r')
lines = file1.readlines()

count = 0
for line in lines:
    count += 1
    parse_array = line.strip().split(':')

    acc_login = parse_array[0]
    acc_password = parse_array[1]

    # print(acc_login, acc_password)

    driver.get("https://steamcommunity.com/login/home/?goto=")

    print(driver.title)

    login_classname = 'newlogindialog_TextInput'
    password_classname = 'newlogindialog_TextInput'
    button_login_classname = 'newlogindialog_SubmitButton'

    time.sleep(5)

    login_input = driver.find_elements(By.XPATH, "//*[contains(@class, '" + login_classname + "')]")[0]
    login_input.send_keys(acc_login)
    time.sleep(1)

    password_input = driver.find_elements(By.XPATH, "//*[contains(@class, '" + password_classname + "')]")[1]
    password_input.send_keys(acc_password)
    time.sleep(1)
    button = driver.find_element(By.CSS_SELECTOR, "div[class*='newlogindialog_SignInButtonContainer_'] button").click()
    time.sleep(1)

    # check if auth
    time.sleep(5)

    for i in range(12):
        if(driver.find_elements(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/form/div/div[1]/div[2]')):
            time.sleep(5)
        if(driver.title!='Войти'):
            break

    print(f'acc{count} logined succesfully!')

    driver.get('https://steamcommunity.com/profiles/76561198173734874')

    time.sleep(5)

    dropdown = driver.find_element(By.ID, 'profile_action_dropdown_link').click()

    report_button = driver.find_elements(By.CLASS_NAME, 'popup_menu_item')[56].click()

    time.sleep(1)

    scam_element1 = driver.find_elements(By.CLASS_NAME, "action_btn_ctn")[4].click()
    time.sleep(1)

    scam_element2 = driver.find_elements(By.CLASS_NAME, "action_btn_ctn")[1].click()
    time.sleep(1)
    scam_element3 = driver.find_elements(By.CLASS_NAME, "action_btn_ctn")[0].click()
    time.sleep(1)

    report_input = driver.find_element(By.ID, 'report_txt_input').send_keys('Украл ключи из игры team Fortress 2')
    time.sleep(1)
    report_button_commit = driver.find_element(By.ID, 'btn_submit_report').click()
    time.sleep(10)
    print(f'acc{count} sent report successfully')
    driver.quit()

