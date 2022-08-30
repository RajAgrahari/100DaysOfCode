import pandas
data = pandas.read_csv("SquirrelDataNYC.csv")
print(data["Primary Fur Color"].value_counts())
