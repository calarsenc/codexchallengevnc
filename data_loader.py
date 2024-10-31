import pandas as pd
import gzip

def read_csv_gzip(file_path):
    with gzip.open(file_path, 'rt') as f:
        df = pd.read_csv(f)
    return df

def load_edges(file_path):
    df = read_csv_gzip(file_path)
    edges = {}
    for idx, row in df.iterrows():
        source = str(row[0])
        target = str(row[1])
        weight = int(row[2])
        edges[(source, target)] = weight
    return edges

def load_matching(file_path):
    df = read_csv_gzip(file_path)
    matching = {}
    for idx, row in df.iterrows():
        male_node = str(row[0])
        female_node = str(row[1])
        matching[male_node] = female_node
    return matching
