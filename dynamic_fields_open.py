import copy as c

class Vars:
    pass

def doc_open(path, v, names, delim, threshold):
    members = [attr for attr in dir(v) if not callable(getattr(v, attr)) and not attr.startswith("__")]
    varss = []
    for i in members:
        varss.append(getattr(v, i))
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


path = '/Users/georgy/theme-classifier/40k_21november.csv'
x = names_open_hendler(path, threshold=3, names=False, delim=',')