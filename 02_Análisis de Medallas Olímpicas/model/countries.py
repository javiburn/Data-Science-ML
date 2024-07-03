import pandas as pd

class Golden:
    def __init__(self, df):
        self.more_gold(df)

    def more_gold(self, df):
        self.gold = df.sort_values(by='Oro', ascending=False).head(3)

class Medals:
    def __init__(self, df):
        filter = df['Total'] > 10
        self.medals = df[filter].sort_values(by='Total', ascending=False)