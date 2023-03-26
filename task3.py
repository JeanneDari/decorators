from tools import logger


list_of_lists = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
path = 'log.txt'


@logger
def flat_generator(list_of_lists):

    for el in list_of_lists:
        for i in el:
            yield i

print(flat_generator(list_of_lists))