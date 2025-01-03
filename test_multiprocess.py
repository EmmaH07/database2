from adv_db import AdvDB
import multiprocessing


def handle_writing_process(dict_file_obj, key):
    """

    :param dict_file_obj: an object from the class AdvDb
    :type dict_file_obj: AdvD
    :param key: a fixed key to set
    :type key: str
    :return:
    """
    for i in range(100):
        print(dict_file_obj.set_val(str(key), str(i)))
        print(dict_file_obj.set_val(str(i), str(key)))


def handle_reading_process(dict_file_obj, key):
    """

    :param dict_file_obj: an object from the class AdvDb
    :type dict_file_obj: AdvDB
    :param key: the wanted key
    :type key: str
    :return:
    """
    for i in range(100):
        print(dict_file_obj.get_val(key))
        print(dict_file_obj.get_val(str(i)))


def handle_deleting_process(dict_file_obj, key):
    """

    :param dict_file_obj: an object from the class AdvDb
    :type dict_file_obj: AdvDB
    :param key: the wanted key
    :type key: str
    :return:
    """
    for i in range(100):
        print(dict_file_obj.delete_data(str(key)))
        print(dict_file_obj.delete_data(str(i)))


def main():
    dict_file_obj = AdvDB(False)
    key = input('enter key: ')
    for i in range(40):
        p1 = multiprocessing.Process(target=handle_writing_process(dict_file_obj, key))
        p2 = multiprocessing.Process(target=handle_reading_process(dict_file_obj, key))
        p3 = multiprocessing.Process(target=handle_deleting_process(dict_file_obj, key))
        p1.start()
        p2.start()
        p3.start()


if __name__ == '__main__':
    main()
