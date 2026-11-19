
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def create_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=options)


def test_page_load():
    driver = create_driver()
    try:
        driver.get("http://127.0.0.1:8000")
        question = driver.find_element(By.ID, "question")
        assert "Which planet" in question.text
        print("PASS: Quiz page loaded")
    finally:
        driver.quit()


def test_correct_answer():
    driver = create_driver()
    try:
        driver.get("http://127.0.0.1:8000")
        driver.find_element(By.CSS_SELECTOR, 'input[value="Saturn"]').click()
        driver.find_element(By.ID, "submit").click()

        feedback = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "feedback"))
        )
        assert "Correct!" in feedback.text
        print("PASS: Correct answer validation")
    finally:
        driver.quit()


def test_wrong_answer_feedback():
    driver = create_driver()
    try:
        driver.get("http://127.0.0.1:8000")
        answers = driver.find_elements(By.NAME, "answer")

        wrong_answer = next(
            answer for answer in answers
            if answer.get_attribute("value") != "Saturn"
        )
        wrong_answer.click()
        driver.find_element(By.ID, "submit").click()

        feedback = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "feedback"))
        )
        assert feedback.text != ""
        assert "Correct!" not in feedback.text
        print("PASS: Wrong answer feedback")
    finally:
        driver.quit()


def test_next_question():
    driver = create_driver()
    try:
        driver.get("http://127.0.0.1:8000")
        driver.find_element(By.CSS_SELECTOR, 'input[value="Saturn"]').click()
        driver.find_element(By.ID, "submit").click()
        driver.find_element(By.ID, "next").click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, "question"), "three hearts"
            )
        )
        assert "three hearts" in driver.find_element(By.ID, "question").text
        print("PASS: Next question navigation")
    finally:
        driver.quit()


def test_score_tracking():
    # We will add the exact score assertion after checking the app's HTML.
    assert True
    print("PASS: Score test placeholder")
