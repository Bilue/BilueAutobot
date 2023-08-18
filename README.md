# Page Object Model (POM) Framework in Python

**Coding Language**: Python

**Author** : Gaurav Purwar

**Date** : March 2023

**Tools**: Appium, PyCharm, Selenium, XCUITest, UIAutomator, WebDriverAgent, Simulator(iOS), Emulator(Android)

**Platform Coverage**: iOS & Android

**Capabilities**: iOS, Android, Windows, macOS

**Supports**: 
* Native Mobile App,
* Hybrid,
* Mobile web,
* Desktop Web,
* API Automation, 
* TV Apps 
* Cross Platform (i.e Anroid, iOS, Apple TV, Android TV, Web)


The Page Object Model (POM) is a design pattern used in test automation that creates an object representation of a web page in a single place, providing a centralized way of accessing its elements. In a POM framework, the web page elements are defined as properties of a class, making the tests more readable, maintainable, and scalable.

## Prerequisites
1. Understanding of Appium:
Ensure you have a basic understanding of how Appium works, including its concepts, architecture, and how it interacts with mobile apps.

2. Familiarity with Mobile Platforms:
Have some familiarity with the mobile platforms (iOS and Android) that you'll be testing. This includes understanding device simulators/emulators and real devices.

3. Programming Knowledge:
A foundation in programming is important, especially in Python, as you'll be using Python to write your automation tests.

### References: 

- https://pypi.org/


- https://github.com/appium/appium-xcuitest-driver/blob/master/docs/real-device-config.md

##  **Installation Guide:** 
- [ ] Install Pycharm from JetBrains Toolbox
- [ ] Install Python
- [ ] Install Appium 
- [ ] Connect with Real Device - any iPhone device
- [ ] Connect with Emulators - Any Android Device
- [ ] Connect with Simulators - For iOS devices
- - [ ] Install and Run Appium Inspector to launch the App on iOS and Android Platform
- [ ] Import the project from https://github.com/Bilue/BilueAutobot/
- [ ] Install below required packages requirement.txt that should install all the python libraries
- [ ] Get ready to run the test health_check using below commands and start automating the test scripts


## Run your tests: 
Use a test runner, such as Pytest, to run your tests.

## Writing the Page Object Class:
The page object class should contain properties that represent the elements on the page
## Setup

# This test requires the following tools to work
- Appium 2 beta (please use https://appium.github.io/appium/docs/en/2.0/) 2.0.0-beta.52
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
### Run Health Check

```
pytest --html=Reports/abc_iview_report.html tests/health_check --log-cli-level=INFO --section_name=iOS-iPhone14Pro-iview
```

### Other Examples:
### Run all tests
```
pytest --html=reports/Automation-Report.html py.test --log-cli-level=INFO
pytest --html=Reports/report.html tests/abc_iview --log-cli-level=INFO --section_name=iOS-iPhone14Pro-iview
```

### Run an arbitrary file
Pytest uses class, module or method names starting with test_ or Test_ to target test for executions.

```
pytest -k 'Test_Iview_Login or Test_video_player or Test_Android_Launch_Uiautomator'
pytest --html=reports/report.html tests/abc_iview/test_login.py --log-cli-level=INFO --section_name=Android-Pixel5-iview
pytest --html=Reports/report.html tests/abc_iview/test_login.py --log-cli-level=INFO --section_name=iOS-iPhone14Pro-iview
```

## TestCase
### unittest based
```
pytest --html=reports/Automation-Report.html tests/abc_iview/test_login.py --log-cli-level=INFO
```
### For ERRORS Only and to be used in CI/CD pipeline
```
pytest --html=reports/Automation-Report.html tests/abc_iview/test_login.py --log-cli-level=INFO
```

### For TV
```
pytest --html=Reports/abc_iview_report.html tests/abc_iview_tv --log-cli-level=INFO --section_name=tvOS-AppleTV4K-iview
```

## Learning and Troubleshooting:

Explore Appium Documentation:
Continuously refer to the official Appium documentation for any guidance on capabilities, methods, and best practices.

Community and Forums:
Engage with the Appium community on forums, such as Stack Overflow or the Appium GitHub repository, to seek help and share experiences.

Debugging and Troubleshooting:
Develop your debugging skills to identify issues in your test scripts, environments, or app configurations.
