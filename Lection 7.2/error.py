class MyError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def text_error(self):
        if self.message:
            return self.message
        else:
            return "Error"


class WrongPath(MyError):
    def text_error(self):
        if self.message:
            return "WrongPath, {0} ".format(self.message)
        else:
            return "WrongPath"


class NameNotFound(MyError):
    def text_error(self):
        if self.message:
            return "NameNotFound, {0} ".format(self.message)
        else:
            return "NameNotFound"


class StudentError(MyError):
    def text_error(self):
        return self.message
