import configparser
import os
from pathlib import Path

import pytest
from py._xmlgen import html
from platform import python_version
from utilities.custom_logger import LogGen
from tests.abc_iview.base_tests import ScreenshotManager

logger = LogGen.loggen()

@pytest.fixture(scope='session')
def mobile_devices():
    path = Path(__file__)
    ROOT_DIR = path.parent.absolute().parent.absolute().parent
    config_path = os.path.join(ROOT_DIR, "Configs/config.ini")
    config = configparser.ConfigParser()
    config.read(config_path)
    devices = [section for section in config.sections() if "iOS" in section]
    logger.info(f"Config path: {config_path}")
    logger.info(f"Sections in config file: {config.sections()}")
    logger.info(f"iOS devices: {devices}")
    return devices


def pytest_addoption(parser):
    parser.addoption(
        "--device",
        action="store",
        help="section name in config file"
    )


def pytest_configure(config):
    py_version = python_version()
    config.pluginmanager.register(MyCustomHook(), 'my_custom_hook')
    # overwriting old parameters with new parameters
    config._metadata = {
        "User Name": "Gaurav Purwar",
        "Python Version": py_version,
        "Project Name": "ABC iView App"
    }

class MyCustomHook:
    @staticmethod
    def pytest_html_results_summary(prefix, summary, postfix):
        prefix.extend([html.h1("Project Name: ABC - iView App")])
        summary.extend([html.h2("Description: iView App for iOS and Android Smoke Test Suite")])
        postfix.extend([html.h2("Status : Completed")])

    # TODO If HTML needs to be in table format
    # @staticmethod
    # def pytest_html_results_table_header(cells):
    #     ''' meta programming to modify header of the result'''
    #
    #     from py.xml import html
    #     # removing old table headers
    #     del cells[1]
    #     # adding new headers
    #     cells.insert(0, html.th('Time', class_='sortable time', col='time'))
    #     cells.insert(1, html.th('Tag'))
    #     cells.insert(2, html.th('Testcase'))
    #     cells.insert(3, html.th('Screenshots'))
    #     cells.pop()

    # @staticmethod
    # def pytest_html_results_table_row(report, cells):
    # from py.xml import html
    # # Add values for the new headers
    # # cells.insert(0, html.td(str(report.duration)))
    # # cells.insert(1, html.td(str(report.keywords)))
    # if report.outcome == 'failed':
    #     #screenshot_filepath = ScreenshotManager.scr
    #     screenshot_index = len(ScreenshotManager.scr) - 1
    #     screenshot_filepath = ScreenshotManager.scr[screenshot_index]
    #     print("screenshot_Gaurav: "+str(ScreenshotManager.scr))
    #     if screenshot_filepath is not None:
    #         cells.insert(5, html.td(html.img(src=screenshot_filepath, width=300, height=500)))
    #
    # cells.insert(6, html.td(str(report.nodeid)))



    # def pytest_configure(config):
    #     ''' modifying the table pytest environment'''
    #
    #     getting user name
    #     from pwd import getpwuid
    #     from os import getuid
    #
    #     username = getpwuid(getuid())[0]
    #
    #     # getting python version
    #     from platform import python_version
    #     py_version = python_version()

    #     # overwriting old parameters with new parameters
    #     config._metadata = {
    #         "user_name": "Gaurav Purwar",
    #         "python_version": py_version,
    #     }


    @staticmethod
    def pytest_html_results_table_row(report, cells):
        from py.xml import html

        class_and_method = report.nodeid.split("::")[-1]
        print("class_and_method: " + class_and_method)

        tcName = class_and_method
        # Add values for the new headers
        # cells.insert(0, html.td(str(report.duration)))
        # cells.insert(1, html.td(str(report.keywords)))
        if report.outcome == 'failed':
            for screenshot_index in range(len(ScreenshotManager.scr)):
                screenshot_filepath = ScreenshotManager.scr[screenshot_index]
                if tcName in screenshot_filepath:
                    cells.insert(5, html.td(html.img(src=screenshot_filepath, width=300, height=500)))

        cells.insert(6, html.td(str(report.nodeid)))
