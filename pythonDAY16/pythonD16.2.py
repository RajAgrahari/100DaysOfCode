from prettytable import PrettyTable
table = PrettyTable()
table.add_column("City Name", ["Lucknow", "Prayagraj", "Mirzapur", "Kanpur", "Varanasi"])
table.add_column("Location", ["Middle-UP", "South-east-UP", "East-UP", "South-west-UP", "East-UP"])
table.add_row(["Agra", "West"])
table.align = "l"
print(table)
