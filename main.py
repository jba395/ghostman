from src.stat_parser import Stat_Parser as sp

def main():
    parser_client = sp()
    data = parser_client.filter_data({
        'Pitcher': 'Brewer',
        'Outcome': 'HR'
    })

    print(data.to_string())

if __name__ == '__main__':
    main()