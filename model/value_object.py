import pandas as pd

# use to pass data from the service to the data layer.

class Valueobj:

    def __init__(self, num1, num2, num3):
        self.series = pd.Series([num1, num2, num3])

    def addservice(self):
        return self.series.sum()