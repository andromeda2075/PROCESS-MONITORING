import pandas as pd
import json
import sqlite3

file='config.json'

f = open(file, "r")
data = json.load(f)
db_file=data['db_file']


conn = sqlite3.connect(db_file, isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)

db_df = pd.read_sql_query("SELECT rowid, * FROM monitored", conn)
db_df.to_csv('database.csv', index=False)
