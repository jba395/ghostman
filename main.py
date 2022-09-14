from src.stat_parser import Stat_Parser as sp
from src.stat_calculator import Stat_Calculator as sc
import src.constants as c

def main():
    parser_client = sp()
    data = parser_client.filter_data({
        'Pitcher': 'Brewer',
        'Outcome': 'HR'
    })

    calc_client = sc()
    total = calc_client.get_total_outcome(parser_client.data, c.OUTCOME_OUTSIDE_PARK_HOMERUN)

    print(data.to_string())
    print(total)

if __name__ == '__main__':
    main()