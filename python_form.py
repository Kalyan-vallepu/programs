from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Path to the ChromeDriver (ensure it's correctly set up in your PATH or use the full path here)
driver = webdriver.Chrome()

# Open the local HTML file (replace the path with your actual file location)
driver.get("file:///C:/Users/kalyan%20kumar/git_demo/firstrepo/form.html")

# Fill out the form using different locator strategies
driver.find_element(By.ID, "kalyan").send_keys("John Doe")  # Locate by ID
driver.find_element(By.NAME, "email").send_keys("john.doe@example.com")  # Locate by name

# Click the submit button
driver.find_element(By.ID, "submitBtn").click()

# Optional: Pause to see the result, then close the browser
time.sleep(3)
driver.quit()
