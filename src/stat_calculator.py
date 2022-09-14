import src.constants as c
from src.stat_parser import Stat_Parser as sp

class Stat_Calculator:
    def __init__(self):
        parser_client = sp()

    def get_player_stats(self, player):
        pass

    def get_total_outcome(self, data, outcome):
        total = data[c.COLUMN_OUTCOME].str.contains(outcome).sum()
        return total