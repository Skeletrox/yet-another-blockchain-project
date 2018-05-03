from blockchainunit import BlockChainUnit
import hashlib
from common import serialize


class BlockChainCluster:
    def __init__(self):
        self.__blockChainUnits = [BlockChainUnit("init")]
        self.__ultimateHash = None

    def __populate(self):
        basicString = ''
        for unit in self.__blockChainUnits:
            basicString += unit.get_value()
        self.__ultimateHash = hashlib.sha256(basicString.encode()).hexdigest()

    def __validate(self):
        basicString = ''
        for unit in self.__blockChainUnits:
            basicString += unit.get_value()
        new_val = hashlib.sha256(basicString.encode()).hexdigest()
        if self.__ultimateHash != new_val:
            print ("Integrity of units in this cluster has been compromised!")

    def add_blockchain_unit(self, record):
        unit = BlockChainUnit(record)
        unit.add_previous_hash(serialize(self.__blockChainUnits[-1]))
        self.__blockChainUnits.append(unit)
        self.__populate()

    def retrieve_units(self):
        self.__validate()
        for unit in self.__blockChainUnits:
            print (unit.get_data())
