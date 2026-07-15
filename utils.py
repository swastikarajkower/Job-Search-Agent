import pandas as pd

def remove_duplicates(df):

    return df.drop_duplicates(
        subset=["title","url"]
    )

def save(df):

    df.to_csv(
        "jobs.csv",
        index=False
    )
