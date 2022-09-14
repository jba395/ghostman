import src.constants as c
from src.stat_parser import Stat_Parser as sp

class Player:
    def __init__(self, name):
        self.stat_parser = sp()
        self.batting_data = sp.filter_data(self.stat_parser.data, {c.COLUMN_BATTER: name})
        self.pitching_data = sp.filter_data(self.stat_parser.data, {c.COLUMN_PITCHER: name})

        # get numbers for each outcome
        self.batting_aggregate = {}
        self.pitching_aggregate = {}

        for outcome in c.OUTCOMES_PLATE_APPEARANCE:
            self.batting_aggregate[outcome] = len(sp.filter_data(self.batting_data, {c.COLUMN_OUTCOME: outcome}))
            self.pitching_aggregate[outcome] = len(sp.filter_data(self.pitching_data, {c.COLUMN_OUTCOME: outcome}))

    def show(self):
        print(self.batting_aggregate)
        print(self.pitching_aggregate)
