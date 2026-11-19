
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_quiz_application():

    driver = webdriver.Safari()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("http://127.0.0.1:8000")

        # Test 1: Verify first question
        question = driver.find_element(By.ID, "question")
        assert "Which planet" in question.text
        print("PASS: First question displayed")

        # Test 2: Select correct answer
        answer = driver.find_element(
            By.CSS_SELECTOR, 'input[value="Saturn"]'
        )
        answer.click()
        print("PASS: Answer selected")

        # Test 3: Submit answer
        driver.find_element(By.ID, "submit").click()

        feedback = wait.until(
            EC.visibility_of_element_located((By.ID, "feedback"))
        )
        assert "Correct!" in feedback.text
        print("PASS: Correct answer validation")

        # Test 4: Move to next question
        driver.find_element(By.ID, "next").click()

        question = wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "question"), "three hearts"
            )
        )
        assert question
        print("PASS: Next question navigation")

        print("ALL FUNCTIONAL TESTS PASSED!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_quiz_application()



def test_wrong_answer_feedback():
    driver = webdriver.Chrome()
    try:
        url = "http://127.0.0.1:8000"
        driver.get(url)
        count = len(driver.find_elements(By.NAME, "answer"))
        texts = []
        for i in range(count):
            driver.get(url)
            driver.find_elements(By.NAME, "answer")[i].click()
            driver.find_element(By.ID, "submit").click()
            texts.append(driver.find_element(By.ID, "feedback").text)
        assert sum(t.startswith("Correct!") for t in texts) == 1
        assert all(t != "" for t in texts)
    finally:
        driver.quit()
