from common import serialize


class BlockChainUnit:
    def __init__(self, data):
        self.__data = data
        self.value = serialize(self.__data)

    def get_value(self):
        return self.value

    def add_previous_hash(self, unitHash):
        self.previous = unitHash

    def verify_legitimacy(self):
        if self.value == serialize(self.__data):
            return True
        return False

    def get_data(self):
        if self.verify_legitimacy():
            return self.__data
        else:
            return None
