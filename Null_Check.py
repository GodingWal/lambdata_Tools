# Function to to check null in dataset


def null_check(df):
    for _ in df:
        if None in df.isnull():
            print("No Error")
        else:
            print("Error")
