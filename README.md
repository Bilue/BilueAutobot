# Automation Framework: Page Object Model

# Page Object Model (POM) Framework in Python
The Page Object Model (POM) is a design pattern used in test automation that creates an object representation of a web page in a single place, providing a centralized way of accessing its elements. In a POM framework, the web page elements are defined as properties of a class, making the tests more readable, maintainable, and scalable.


 Coding Language: Python

 Author : Gaurav Purwar

 Tools: Appium, PyCharm, Selenium, XCUITest, UIAutomator, WebDriverAgent, Simulator(iOS), Emulator(Android)

 Platform Coverage: iOS & Android 
 
 Capabilities: iOS, Android, Windows, macOS
 
 Supports: Native, hybrid, mobile web, Desktop Web, API Automation



## Getting started with POM in Python
Here are the steps to set up a POM framework in Python:

## Install required packages:
You need to have the following packages installed: selenium, unittest, and pytest.

## Create a directory for your project: 
Choose a location for your project and create a directory for it.

## Create a Python file for your page object class: 
This file will define the page object class and its properties, representing the elements on the page.

## Create a Python file for your tests: 
This file will contain the tests that will interact with the page object class, performing actions on the elements and asserting the results.

## Run your tests: 
Use a test runner, such as Pytest, to run your tests.

## Writing the Page Object Class:
The page object class should contain properties that represent the elements on the page
## Setup

# This test requires the following tools to work
- Appium 2 beta (please use https://appium.github.io/appium/docs/en/2.0/)
- Xcode and simulators 
- Android studio and emulators
- xcuitest - an Appium iOS automator
- uiautomator2 - an Appium Android automator
- Python 3.11 
- All external reqs in the requirements.txt

```
pip install -r requirements.txt
```

## Run tests
### Run all tests
```
pytest --html=Reports/report.html tests/abc_iview --log-cli-level=INFO --device=iOS-iPhone14Pro
```

### Run an arbitrary file
Pytest uses class, module or method names starting with test_ or Test_ to target test for executions.

```
pytest -k 'Test_Iview_Login or Test_video_player or Test_Android_Launch_Uiautomator'
pytest --html=Reports/report.html tests/abc_iview/test_viewing_history.py --log-cli-level=INFO --device=Android-Pixel5
```

## TestCase
### unittest based
```
pytest --html=Reports/report.html tests/abc_iview/test_viewing_history.py --log-cli-level=INFO --device=iOS-iPhone14Pro
```
### For ERRORS Only and to be used in CI/CD pipeline
```
pytest --html=Reports/report.html tests/abc_iview/test_viewing_history.py --log-cli-level=INFO --device=iOS-iPhone14Pro
```


