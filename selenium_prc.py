from selenium import webdriver

driver = webdriver.Chrome('/Users/user/Downloads/chromedriver_win32/Chromedriver.exe')
driver.get('http://zzzscore.com/1to50/')

btn = driver.find_elements_by_xpath('//*[@id="grid"]/div[@*]')

for i in range (1,51):
    for j in btn:
        if j.text == str(i):
            j.click()
            print(str(i)+"click!")
            break