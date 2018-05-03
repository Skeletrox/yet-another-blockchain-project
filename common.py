import hashlib
import pickle


def serialize(unit):
    value = pickle.dumps(unit)
    result = hashlib.sha256(value).hexdigest()
    return result
