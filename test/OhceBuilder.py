from src.Ohce import Ohce


class OhceBuilder:
    def __init__(self):
        self.__langue = ""
        self.__periode = Periodes.DEFAULT

    def build(self):
        return Ohce(self.__langue, self.__periode)

    @staticmethod
    def default():
        return OhceBuilder().build()

    def langue(self, langue):
        self.__langue = langue
        return self

    def periode(self, periode):
        self.__periode = periode
        return self