class SoftAssert:
    def __init__(self):
        self.errors = []

    def assert_true(self, expr, msg=None):
        try:
            assert expr, msg
        except AssertionError as e:
            self.errors.append(str(e))

    def assert_equal(self, first, second, msg=None):
        try:
            assert first == second, msg
        except AssertionError as e:
            self.errors.append(str(e))

    def assert_all(self):
        if len(self.errors) > 0:
            message = '\n'.join(self.errors)
            raise AssertionError(message)