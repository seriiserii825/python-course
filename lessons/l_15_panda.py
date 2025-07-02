import pandas as pd

def l_15_panda():
    # Create a DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)

    # Display the DataFrame
    print("DataFrame:")
    print(df)

    # Access a column
    print("\nAccessing the 'Name' column:")
    print(df['Name'])

    # Filter rows
    print("\nFiltering rows where Age > 28:")
    print(df[df['Age'] > 28])
