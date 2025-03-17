from selenium import webdriver
import mysql.connector
from selenium.webdriver.common.by import By


#driver = webdriver.Safari()  # Ensure Safaridriver/Chrome Driver installed
driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5000/login')

# Interact with the login form
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

username.send_keys('jkaur')
password.send_keys('testdatabase')
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
driver.quit()

# Verify user data in the database
db = mysql.connector.connect(user='root', password='example', host='localhost', database='firstdatabase')
cursor = db.cursor()
cursor.execute("SELECT * FROM users WHERE username = 'jkaur'")
user_data = cursor.fetchone()
print(user_data)

assert user_data[1] == 'jkaur'  # Verify the username in the database matches
db.close()
#driver.quit()

print("Test passed: User data is correct.")

