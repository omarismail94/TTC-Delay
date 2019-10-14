import config
import argparse

parser = argparse.ArgumentParser(description='Query Postgres Database')
parser.add_argument("command", type=str, help="command", default="SELECT * FROM subwaydelays")
args = parser.parse_args()

if __name__ == "__main__":
    data = config.query(args.command)
    print(data)
    
