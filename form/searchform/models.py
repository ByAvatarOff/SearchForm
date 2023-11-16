from tinydb import TinyDB


class TinyDbManager:
    """
    Class for load and init database TinyDB
    """
    def __init__(self):
        self.db = TinyDB('db.json')