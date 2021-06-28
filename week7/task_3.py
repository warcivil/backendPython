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

    def __repr__(self) -> str:
        return "WriteFileCommand(file_name, write_str, timer=1)"

class ReadFileCommand(object):
    def __init__(self, file_name, timer=1):
        self.__file_name = file_name
        self.timer = timer

    def execute(self):
        with open(self.__file_name, mode='r') as file_read:
            print(file_read.read())

    def pre_execute(self):
        schedule.every(self.timer).minutes.do(self.execute())

    def __repr__(self) -> str:
        return "ReadFileCommand(file_name, timer=1)"


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

    def __repr__(self) -> str:
        return "DeleteFileCommand(file_name)"


class RightsChange(object):
    def __init__(self, file_name, chmod):
        self.__file_name = file_name
        self.__chmod = chmod

    def execute(self):
        os.chmod(self.__file_name, self.__chmod)

    def __repr__(self) -> str:
        return "RightsChange(file_name, chmod)"


class History(object):
    def __init__(self):
        self._commands = list()

    def execute(self, command, next_command=False):
        if(not next_command):
            self._commands.append(command)
            command.execute()
        else:
            self._commands.append(command)
            self._commands.append(next_command)
            for item in self._commands:
                item.execute()
            

    def undo(self, command):
        command.undo()

    def log(self):
        return self._commands


if __name__ == '__main__':
    history = History()
    history.execute(WriteFileCommand("2.str", "blah blah"), ReadFileCommand("2.str"))
    print(history.log())