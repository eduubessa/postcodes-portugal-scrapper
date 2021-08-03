import os
from configparser import ConfigParser

class Config:

    __path = os.path.dirname(os.path.realpath(__file__))

    @staticmethod
    def get(variable, default = ""):
        config = ConfigParser()
        config.read(os.path.dirname(os.path.realpath(__file__)) + "/../../config.ini")

        section = variable.split(".")[0]
        field = variable.split(".")[1]

        try:
            if config[section.upper()][field] is not None:
                return config[section.upper()][field]
            else:
                return default
        except:
            return default
