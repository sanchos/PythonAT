# Simple framework for UI automated testing

Based on Pytest, Selenium Webdriver

Installation:
```
cd **to your path**
git clone https://github.com/sanchos/PythonAT.git
pip install -r requirements.txt

#run tests
pytest

#run tests with Allure
pytest --alluredir allure-results
```

Settings file location: config/config.py

To run your tests in Selenide cloud change:
BROWSER_TYPE to 'cloud'

SELENIDE_SERVER to URL of your selenide server in format "http://0.0.0.0:4444/wd/hub"
