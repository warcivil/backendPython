import os
import schedule


class WriteFileCommand(object):
    def __init__(self, file_name, write_str, timer=1):
        self.__file_name = file_name
        self.__write_str = write_str
        self.__timer = timer

    def execute(self):
        with open(self.__file_name, mode='w') as file_write:
            file_write.write(self.__write_str)

    def pre_execute(self):
        schedule.every(self.__timer).minutes.do(self.execute())


class ReadFileCommand(object):
    def __init__(self, file_name, timer=1):
        self.__file_name = file_name
        self.timer = timer

    def execute(self):
        with open(self.__file_name, mode='r') as file_read:
            print(file_read.read())

    def pre_execute(self):
        schedule.every(self.timer).minutes.do(self.execute())


class DeleteFileCommand(object):
    def __init__(self, file_name):
        self.__file_name = file_name

    def execute(self):
        with open(self.__file_name, mode="r") as handle:
            self.save_param = handle.read()
        os.remove(self.__file_name)

    def undo(self):
        try:
            with open(self.__file_name, mode="w") as handle:
                handle.write(self.save_param)
        except Exception as e:
            print(e)


class RightsChange(object):
    def __init__(self, file_name, chmod):
        self.__file_name = file_name
        self.__chmod = chmod

    def execute(self):
        os.chmod(self.__file_name, self.__chmod)


class History(object):
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()

    def undo(self, command):
        command.undo()

    def log(self):
        return self._commands


if __name__ == '__main__':
    history = History()
    r = DeleteFileCommand(os.getcwd() + "/" + "2.txt")
    history.execute(r)
