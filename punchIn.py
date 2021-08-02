from selenium import webdriver

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome('./chromedriver',options=op)


url = 'https://qnaire.ab1.auo.com/node/4169'
driver.get(url)

user =  driver.find_element_by_name('name')
pwd =  driver.find_element_by_name('pass')

user.send_keys("jameschlee")
pwd.send_keys("Auo2008111")

login = driver.find_element_by_name('op')
login.click()

punchIn = driver.find_element_by_id('edit-submitted-sign-1')
punchIn.click()

#punchOut = driver.find_element_by_id('edit-submitted-sign-2')
#punchOut.click()
#punchOutNote = driver.find_element_by_id('edit-submitted-note')
#punchOutNote.send_keys("Note Test")

submit = driver.find_element_by_name('op')
submit.click()

driver.close()