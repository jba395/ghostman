import pandas as pd
import src.constants as c

class Stat_Calculator:
    def __init__(self):
        self.data = pd.read_csv(c.RAW_STATS_FILE_PATH)

    def show(self):
        print(self.data.to_string())

    def filter_data(self, filters = {}):
        '''
        Specify key:values to filter data for other operations.
        Use csv headers.
        '''
        pass

    def get_batting_average(self, data):
        pass
