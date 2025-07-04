import pandas as pd


def l_15_panda():
    forum_users = {
        "User ID": [1, 2, 3, 4],
        "Username": ["alice", "bob", "charlie", "dave"],
        "Age": [25, 30, 22, 35],
        "Joined Date": ["2020-01-01", "2019-05-15", "2021-03-10", "2018-07-20"],
        "Total posts": [100, 150, 200, 50],
        "Reputation": [500, 300, 400, 600],
    }

    df = pd.DataFrame(forum_users)
    print(f"df: {df}")
    print(df.shape)
