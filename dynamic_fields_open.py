import copy as c
import csv

# Раскладывает колонки csv файла по переменным без знаниния о том, сколько колонок находится в csv файле
# Если в csv файле 3 колонки то будет возвращен список из 3х списков, где в каждом будут содержаться
# значения из колонок csv файла


class Vars:
    pass


def doc_open(path, v, names, delim, threshold):
    members = [attr for attr in dir(v) if not callable(getattr(v, attr)) and not attr.startswith("__")]
    print(members)
    varss = []
    for i in members:
        varss.append(getattr(v, i))
    print(varss)
    with open(path, 'rt') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=delim)
        for n, i in enumerate(readCSV):
            if names and n == 0:
                continue
            if n < threshold:
                for ii in range(len(i)):
                    varss[ii].append(i[ii])
    return varss


def names_open_hendler(path, names=False, delim=',', threshold=999999):
    """
    Раскладывает колонки csv файла по переменным без знаниния о том, сколько колонок находится в csv файле
    Если в csv файле 3 колонки то будет возвращен список из 3х списков, где в каждом будут содержаться
    значения из колонок csv файла
    :param path: path to csv
    :param names: True if there are names in csv, and their values are not desirreble in output
    :param delim: csv delimiter
    :param threshold: how many rows to exctract
    :return: list of lists. iths item corresponds to iths csv column
    """
    length = 0
    with open(path, 'rt') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=delim)
        for n, i in enumerate(readCSV):
            if names and n == 0:
                continue
            if n < 2:
                length = len(i)
    v = c.deepcopy(Vars)
    for i in range(length):
        setattr(v, 'v{}'.format(i), [])
    docs = doc_open(path, v, names=names, delim=delim, threshold=threshold)
    return docs


names_open_hendler('.csv',
                   threshold=3,
                   names=True,
                   delim=';')
