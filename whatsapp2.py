from selenium import webdriver

driver = webdriver.Chrome("/Users/user/Downloads/chromedriver_win32/chromedriver")
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name = input("Enter name or group name:")
msg = input("Enter message:")
count = int(input("Enter count:"))

input("Enter anything after scan OR code")

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

for index in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
print("success")



