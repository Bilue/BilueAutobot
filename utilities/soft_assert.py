from utilities.custom_logger import LogGen


class SoftAssert:
    logger = LogGen.loggen()

    def __init__(self):
        self.errors = []

    def __call__(self, condition, msg=None):
        try:
            assert condition, msg
            self.logger.info(str(msg) + ": Assertion Performed!***")
        except AssertionError as e:
            self.errors.append(str(e))

    def assert_true(self, expr, msg=None):
        self(expr, msg)
        self.logger.info(str(msg)+": Assert True Performed!***")

    def assert_false(self, expr, msg=None):
        self(not expr, msg)
        self.logger.info(str(msg) + ": Assert False Performed!***")

    def assert_equal(self, actual, expected, msg=None):
        self(actual == expected, msg)
        self.logger.info(str(msg) + ": Assert Equal Performed!***")

    def assert_all(self):
        if len(self.errors) > 0:
            message = '\n'.join(self.errors)
            raise AssertionError(message)
