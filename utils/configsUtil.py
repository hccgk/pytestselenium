from configparser import ConfigParser

class configer(object):

    def __int__(self):
        pass

    @staticmethod
    def nameAndThings(name,thing):
        conf = ConfigParser()
        conf.read(r"C:\Users\HE\PycharmProjects\pythonProject\configs\config.ini")
        return conf[name][thing]
