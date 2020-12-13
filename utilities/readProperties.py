import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\rajso\\PycharmProjects\\nopCommerceApplication\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod      #this makes the method static so that there will be no need of making object of the class
    def getApplicationURL():
        url = config.get('common','baseURL')
        return url
    @staticmethod
    def getUsername():
        username= config.get('common','username')
        return username
    @staticmethod
    def getPassword():
        password = config.get('common','password')
        return password

