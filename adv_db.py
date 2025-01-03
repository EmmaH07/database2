from file_db import FileDB
import win32event


class AdvDB(FileDB):
    def __init__(self, is_it_threads, dic={}):
        super().__init__(dic)
        self.read_lock = win32event.CreateSemaphore(None, 10, 10, 'read_semaphore')
        self.write_lock = win32event.CreateMutex(None, False, 'write_mutex')

    def set_val(self, key, new_val):
        """
        sets a new value for the key. creates a new key-value pair if the key doesn't exist.
        uses lock and semaphore for synchronization.
        :param key: the wanted key
        :param new_val: the new value
        :return: True if it worked, False if it didn't.
        """
        win32event.WaitForSingleObject(self.write_lock, -1)
        for i in range(10):
            win32event.WaitForSingleObject(self.read_lock, -1)
        b = super().set_val(key, new_val)
        for i in range(10):
            win32event.ReleaseSemaphore(self.read_lock, 1)
        win32event.ReleaseMutex(self.write_lock)
        return b

    def delete_data(self, key):
        """
        deletes the key-value pair from the dictionary. uses lock and semaphore for synchronization.
        :param key: the wanted key
        :return: the value of said key. None if the key doesn't exist.
        """
        win32event.WaitForSingleObject(self.write_lock, -1)
        for i in range(10):
            win32event.WaitForSingleObject(self.read_lock, -1)
        obj = super().delete_data(key)
        for i in range(10):
            win32event.ReleaseSemaphore(self.read_lock, 1)
        win32event.ReleaseMutex(self.write_lock)
        return obj

    def get_val(self, key):
        """
        uses lock and semaphore for synchronization.
        :param key: the wanted key
        :return: the value of said key. None if the key doesn't exist.
        """
        win32event.WaitForSingleObject(self.read_lock, -1)
        obj = super().get_val(key)
        win32event.ReleaseSemaphore(self.read_lock, 1)
        return obj
