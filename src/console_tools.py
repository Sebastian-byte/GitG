class ColorText():
    """Permite cambiar de color el texto mostrado en consola"""
    __PINK = '\033[95m'
    __OKBLUE = '\033[94m'
    __OKGREEN = '\033[92m'
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

    def PINK(self, arg):
        """ Texto en color rosado """
        return self.__PINK + arg + self.__ENDC
