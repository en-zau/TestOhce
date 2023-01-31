import locale

from src.langue.LangueAnglaise import LangueAnglaise
from src.langue.LangueFrancaise import LangueFrancaise
from src.Ohce import Ohce
from src.Periodes import Periodes


class SystemLangAdapter():
    def __init__(self):
        langue_systeme = locale.getdefaultlocale()[0]
        self.__langue = LangueAnglaise() \
            if langue_systeme == "en_GB" \
            else LangueFrancaise()


if __name__ == '__main__':
    ohce = Ohce(SystemLangAdapter(), Periodes.NUIT)