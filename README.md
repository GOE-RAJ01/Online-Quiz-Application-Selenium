# Online Quiz Application Testing Using Selenium with Python

## Project Team

| Name | Student ID |
|---|---|
| Pushparaj | 20231ISE0001 |
| Nishanth | 20231ISE0020 |

## 1. Project Overview

The Online Quiz Application is a browser-based multiple-choice quiz developed using HTML, CSS and JavaScript.

This project demonstrates automated functional testing using Selenium WebDriver with Python. The application is tested using the Safari browser.

## 2. Objectives

- Develop a simple interactive online quiz.
- Automate browser interactions using Selenium.
- Verify application functionality using automated tests.
- Execute tests and analyse results using pytest.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| HTML | Webpage structure |
| CSS | Application design |
| JavaScript | Quiz functionality |
| Python | Test automation |
| Selenium WebDriver | Browser automation |
| pytest | Test execution |
| Safari | Testing browser |

## 4. Application Features

- Five multiple-choice questions.
- Answer selection and submission.
- Correct-answer feedback.
- Navigation between questions.
- Final score and restart functionality.

## 5. Project Structure

```text
Online-Quiz-Application/
├── app/
│   └── index.html
├── first_test.py
├── test_quiz.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 6. Installation and Execution

### Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the application

```bash
python3 -m http.server 8000 --directory app
```

Open Safari and visit:

`http://127.0.0.1:8000`

### Run automated tests

Open another Terminal window, navigate to the project folder, activate the virtual environment and execute:

```bash
python3 -m pytest -v
```

## 7. Testing Approach

Selenium WebDriver is used to automate browser interactions.

The current automated checks include:

1. Website title verification.
2. Main heading verification.
3. First question verification.
4. Answer selection.
5. Correct-answer feedback verification.
6. Navigation to the next question.

pytest executes the test functions and reports their results.

## 8. Test Results

The initial Selenium test and functional test were successfully executed.

The functional test includes multiple assertions within one test function. Therefore, pytest may count these checks as one test item.

## 9. Conclusion

This project demonstrates how Selenium WebDriver and Python can be used to automate functional testing of a web application.

The project provides practical experience in browser automation, element identification, assertions and automated test execution.

## 10. Future Enhancements

- Add more independent test cases.
- Test incorrect answers and empty submissions.
- Verify score calculation and restart functionality.
- Expand the quiz question bank.
- Generate detailed automated test reports.

## GitHub Repository

https://github.com/GOE-RAJ01/Online-Quiz-Application-Selenium

