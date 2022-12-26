class ExposeObject:
    def __init__(self, data: dict):
        self.__dict__.update(data)
