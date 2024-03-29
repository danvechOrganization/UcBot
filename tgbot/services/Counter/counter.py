class Counter:

    COUNTER = 0

    @classmethod
    def add_counter(cls):
        cls.COUNTER += 1

        if(cls.COUNTER > 29):
            cls.COUNTER = 0
