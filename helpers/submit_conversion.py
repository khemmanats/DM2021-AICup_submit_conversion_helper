import pandas as pd

'''
Helper function for migrated AI Cup: Agriculture Articles Label Classification
ISA 5810 Data Mining (2021 Fall Semester)
'''

def convert(df):
    template = pd.read_csv("helpers/sample_BOOL.csv", index_col=0)
    df1 = df
    df1['Relation'] = df['Test'].astype(str) + '-' + df['Reference'].astype(str)
    for index, row in df1.iterrows():
        template.loc[row['Relation']] = 1
    return template