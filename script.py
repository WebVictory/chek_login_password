from selenium import webdriver
import csv
import time
from selenium.webdriver.common.keys import Keys

with open('mail.csv', newline='') as File:
    reader = csv.reader(File,delimiter=';')
    mail_dict = {}
    for row in reader:
        k, v = row
        mail_dict[k] = v

driver = webdriver.Firefox(executable_path='C:/webdriver/geckodriver.exe')
for acc_mail, password in mail_dict.items():
    driver.get('https://mail.ru/')

    elem = driver.find_element_by_class_name("email-input.svelte-1eyrl7y")
    elem.send_keys(acc_mail)
    driver.find_element_by_class_name("svelte-1eyrl7y").click()
    time.sleep(3)
    pass_input = driver.find_element_by_class_name("password-input.svelte-1eyrl7y")

    if pass_input :
        print('акк существует')
    else: print('акка не существует')

    pass_input.send_keys(password)
    driver.find_element_by_class_name("second-button.svelte-1eyrl7y").click()
    time.sleep(3)
    try:
        pass_input = driver.find_element_by_class_name("error.svelte-1eyrl7y")
        if pass_input:
            print("неправильный пароль")
    except:
        pass









