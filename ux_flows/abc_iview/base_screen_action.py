from datetime import datetime

from utilities.main_driver import MainDriver


class BaseScreenAction:

    def __init__(self, app: MainDriver):
        self.app = app

