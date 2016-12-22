from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

start_from = 1
end_at = 10547 #later make it 10546

firefoxProfile = FirefoxProfile()
## Disable CSS
firefoxProfile.set_preference('permissions.default.stylesheet', 2)
firefoxProfile.set_preference('javascript.enabled', False)
firefoxProfile.set_preference("permissions.default.script", 2);
## Disable images
firefoxProfile.set_preference('permissions.default.image', 2)
## Disable Flash
# firefoxProfile.set_preference('accessibility.warn_on_browsewithcaret','false')


f = open('data.csv', 'w')
def search(driver):
	trs = driver.find_elements(By.TAG_NAME, "tr")
	text = ""
	for row in trs:
		tds = row.find_elements(By.TAG_NAME, "td")
		for element in tds:
			# print element.text
			text = text + '"' + element.text.replace('"','\\"') + "\","
		text = text + '\n'

	f.write(text)

driver = webdriver.Firefox(firefoxProfile)

#lets log in
print "opening home page"
driver.get("https://www.zauba.com")
username = driver.find_elements(By.ID,"edit-name")[0]
username.send_keys("l36160@mvrht.com")
password = driver.find_elements(By.ID,"edit-pass")[0]
password.send_keys("l36160@mvrht.com")
login_button = driver.find_elements(By.ID,"edit-submit")[0]
print "logging in...."
login_button.submit()
print "logged in"
def end():
	f.close()
	driver.close()
def start():
	global driver
	f.write('Date,HS Code,Description,Origin Country,Port of Discharge,Unit,Quantity,Value(INR),Per Unit(INR)')
	for i in range(start_from,end_at):
		print 'loading page for ', i
		driver.get("https://www.zauba.com/import-laptop/p-" + str(i) + "-hs-code.html")
		print 'starting search for ', i
		search(driver)
		print 'searched for ', i,"/",end_at

# f.close()
# driver.close()
#username and password for zauba l36160@mvrht.com