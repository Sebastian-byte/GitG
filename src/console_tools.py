class ColorText():
    """Permite cambiar de color el texto mostrado en consola"""
    __OKPINK = '\033[95m'
    __OKBLUE = '\033[94m'
    __OKGREEN = '\033[92m'
    __OKCYAN = '\033[96m'
    __OKYELLOW = '\u001b[33m'
    __OKWHITE = '\u001b[37m'
    __OKBWHITE = '\u001b[37;1m'
    __OKBBLUE = '\u001b[34;1m'
    __OKBOLD = '\u001b[1m'
    __WARNING = '\033[93m'
    __FAIL = '\033[91m'
    __ENDC = '\033[0m'
    __text = ""

    def red(self, arg):
        """ Texto en color rojo """
        return self.__FAIL + arg + self.__ENDC

    def blue(self, arg):
        """ Texto en color azul """
        return self.__OKBLUE + arg + self.__ENDC

    def green(self, arg):
        """ Texto en color verde """
        return self.__OKGREEN + arg + self.__ENDC

    def pink(self, arg):
        """ Texto en color rosado """
        return self.__OKPINK + arg + self.__ENDC

    def white(self, arg):
        """ Texto en color blanco """
        return self.__OKWHITE + arg + self.__ENDC

    def cyan(self, arg):
        """ Texto en color azul claro """
        return self.__OKCYAN + arg + self.__ENDC

    def yellow(self, arg):
        """ Texto en color amarillo """
        return self.__OKYELLOW + arg + self.__ENDC

    def bblue(self, arg):
        """ Texto en color azul fuerte """
        return self.__OKBBLUE + arg + self.__ENDC

    def bwhite(self, arg):
        """ Texto en color blanco fuerte """
        return self.__OKBWHITE + arg + self.__ENDC

    def bold(self, arg):
        """ Texto bold """
        return self.__OKBOLD + arg + self.__ENDC