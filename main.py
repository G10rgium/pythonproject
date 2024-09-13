import pandas


data = [
    ["zura", 23],
    ["giorgi", 24]
]


# df = pandas.DataFrame(data, columns=["name", "age"])
# df.to_csv("person.csv")
#
# df.to_excel("person.xlsx")

results_csv = pandas.read_csv("person.csv")
results_excel = pandas.read_excel("person.xlsx")
print(results_csv)
print(results_excel)