from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
#replace 'laptop' by the search keyword
driver.get("https://www.zauba.com/import-laptop-hs-code.html")   
#driver.get("https://www.zauba.com")
#elem = driver.find_element_by_name("prod_desc")
#elem.clear()
#elem.send_keys("laptop")
#elem.send_keys(Keys.RETURN)
trs = driver.find_elements(By.TAG_NAME, "tr") 
for row in trs:
	tds = row.find_elements(By.TAG_NAME, "td")
	for element in tds:
		print element.text
assert "No results found." not in driver.page_source
driver.close()
