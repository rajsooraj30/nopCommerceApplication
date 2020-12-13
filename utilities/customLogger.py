import logging

class LogGen():
    @staticmethod
    def test_loggen():

        for handler in logging.root.handlers[:]:
             logging.root.removeHandler(handler)
        logging.basicConfig(filename="C:\\Users\\rajso\\PycharmProjects\\nopCommerceApplication\\Logs\\test.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger



