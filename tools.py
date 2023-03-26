import datetime


def logger(old_function):

    def new_function(*args, **kwargs):
        start = datetime.datetime.now()
        print(f'вызвана функция {old_function}')
        value = old_function(*args, **kwargs)
        print('Действие ПОСЛЕ')
        print('время вызова функции', start)
        print(*args)
        with open("main.log", "a") as file:
            file.write(f'datetime: {start} \n')
            file.write(f'function name: {old_function} \n')
            file.write(f'value: {value} \n')
            for i in args:
                file.write(f'args: {i} ')
            file.write(str(kwargs))
        return value
    return new_function


def logger2(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            time_ = datetime.datetime.now()
            value = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'{time_} | {old_function.__name__} | {args=} | {kwargs=} | {value}\n')
            return value
        return new_function
    return __logger