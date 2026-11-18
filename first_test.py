
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Safari
driver = webdriver.Safari()

try:
    print("Opening Curiosity Quiz in Safari...")

    driver.get("http://127.0.0.1:8000")

    # Test 1: Website title
    assert driver.title == "Curiosity Quiz"
    print("PASS: Website title verified")

    # Test 2: Main heading
    heading = driver.find_element(By.TAG_NAME, "h1")
    assert heading.text == "Test your curiosity."
    print("PASS: Main heading verified")

    # Test 3: First question
    question = driver.find_element(By.ID, "question")
    assert "Which planet" in question.text
    print("PASS: First question verified")

    print("ALL TESTS PASSED!")

finally:
    driver.quit()

