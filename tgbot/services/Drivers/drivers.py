class Drivers:
    NAME = None

    @staticmethod
    def name():
        global NAME
        return NAME
    @staticmethod
    def set_name(name):
        global NAME
        NAME = name


