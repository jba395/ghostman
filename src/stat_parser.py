import pandas as pd
import src.constants as c

class Stat_Parser:
    def __init__(self):
        self.data = pd.read_csv(c.RAW_STATS_FILE_PATH)

    def get_all(self):
        return self.data

    def show(self):
        print(self.data.to_string())

    def filter_data(self, filters = {}):
        '''
        Specify key:values to filter data for other operations.
        Use csv headers.
        '''
        data = self.data
        for filter in filters:
            data = data.loc[data[filter] == filters[filter]]

        return data

    def get_batting_average(self, data):
        pass
