class Counter:
    """"""

    def __init__(self):
        """"""
        self.__count = 0

    def add(self):
        """"""
        self.__count += 1

    def is_full(self):
        """"""
        return self.__count >= 3
