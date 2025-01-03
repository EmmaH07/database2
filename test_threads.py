from adv_db import AdvDB
from threading import Thread


def handle_writing_thread(dict_file_obj, key):
    """

    :param dict_file_obj: an object from the class AdvDb
    :type dict_file_obj: AdvD
    :param key: a fixed key to set
    :type key: str
    :return:
    """
    for i in range(10):
        print(dict_file_obj.set_val(str(key), str(i)))
        print(dict_file_obj.set_val(str(i), str(key)))


def handle_reading_thread(dict_file_obj, key):
    """

    :param dict_file_obj: an object from the class AdvDb
    :type dict_file_obj: AdvDB
    :param key: the wanted key
    :type key: str
    :return:
    """
    for i in range(10):
        print(dict_file_obj.get_val(key))
        print(dict_file_obj.get_val(str(i)))


def handle_deleting_thread(dict_file_obj, key):
    """

    :param dict_file_obj: an object from the class AdvDb
    :type dict_file_obj: AdvDB
    :param key: the wanted key
    :type key: str
    :return:
    """
    for i in range(10):
        print(dict_file_obj.delete_data(str(key)))
        print(dict_file_obj.delete_data(str(i)))


def main():
    dict_file_obj = AdvDB(True)
    key = input('enter key: ')
    for i in range(40):
        t1 = Thread(target=handle_writing_thread, args=(dict_file_obj, i))
        t2 = Thread(target=handle_reading_thread, args=(dict_file_obj, i))
        t3 = Thread(target=handle_deleting_thread, args=(dict_file_obj, i))
        t1.start()
        t2.start()
        t3.start()


if __name__ == '__main__':
    main()
