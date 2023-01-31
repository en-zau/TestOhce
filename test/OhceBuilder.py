from src.Ohce import Ohce


class OhceBuilder:
    def __init__(self):
        self.__langue = ""

    def build(self):
        return Ohce(self.__langue)

    @staticmethod
    def default():
        return OhceBuilder().build()

    def langue(self, langue):
        self.__langue = langue
        return self