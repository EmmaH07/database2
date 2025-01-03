from dict_db import DictDB
import os
import pickle
import win32file
import win32con

FILE_PATH = 'db.txt'


class FileDB(DictDB):
    def __init__(self, dic={}):
        super().__init__(dic)
        if not os.path.exists(FILE_PATH):
            self.__file_handle__ = win32file.CreateFile(FILE_PATH, win32con.GENERIC_WRITE | win32con.GENERIC_READ,
                                                        win32con.FILE_SHARE_WRITE, None, win32con.CREATE_NEW,
                                                        win32con.FILE_ATTRIBUTE_NORMAL, None)
        else:
            self.__file_handle__ = win32file.CreateFile(FILE_PATH, win32con.GENERIC_WRITE | win32con.GENERIC_READ,
                                                        win32con.FILE_SHARE_WRITE, None, win32con.OPEN_EXISTING,
                                                        win32con.FILE_ATTRIBUTE_NORMAL, None)
        self.file_dump()

    def file_dump(self):
        try:
            object4file = pickle.dumps(self.__dic__)
            win32file.WriteFile(self.__file_handle__, object4file, None)

        except Exception as err:
            print('Got an exception in FileDB - file_dump: ' + str(err))

    def file_load(self):
        try:
            file_size = win32file.GetFileSize(self.__file_handle__)
            if file_size > 0:
                hr, data = win32file.ReadFile(self.__file_handle__, file_size)
                if data != b'':
                    self.__dic__ = pickle.loads(data)

        except Exception as err:
            print('Got an exception in FileDB - file_load: ' + str(err))

    def set_val(self, key, new_val):
        """
        sets a new value for the key. creates a new key-value pair if the key doesn't exist.
        dumps the updated dictionary to a file.
        :param key: the wanted key
        :param new_val: the new value
        :return: True if it worked, False if it didn't.
        """
        self.file_load()
        b = super().set_val(key, new_val)
        self.file_dump()
        return b

    def delete_data(self, key):
        """
        deletes the key-value pair from the dictionary. dumps the updated dictionary to a file.
        :param key: the wanted key
        :return: the value of said key. None if the key doesn't exist.
        """
        self.file_load()
        val = super().delete_data(key)
        self.file_dump()
        return val

    def get_val(self, key):
        """
        fetches the needed value by key
        :param key: the wanted key
        :return: the value of said key. None if the key doesn't exist.
        """
        self.file_load()
        val = super().get_val(key)
        self.file_dump()
        return val


if __name__ == "__main__":
    f_obj = FileDB()
    f_obj.set_val('hi', 'shalom')
    f_obj.get_val('hi')
