class MyError(Exception):
    pass

    def text_error(self):
        if self.args[0]:
            return args[0]
        else:
            return "Error"


class WrongPath(MyError):
    def text_error(self):
        if self.args[0]:
            return "WrongPath, {0} ".format(self.args[0])
        else:
            return "WrongPath"


class NameNotFound(MyError):
    def text_error(self):
        if self.args[0]:
            return "NameNotFound, {0} ".format(self.args[0])
        else:
            return "NameNotFound"


class StudentError(MyError):
    def text_error(self):
        return self.args[0]
