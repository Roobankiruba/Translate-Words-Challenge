import pandas

df = pandas.read_csv("./french_dictionary.csv")

with open("./find_words.txt", "r") as f:
    fdata = f.readlines()

# print("above" in df["abide"].tolist())
with open("finalresult.txt", "w+") as f1:
    data = {}
    for item in fdata:
        item = item.replace(" ", "").replace("\n", "")
        if item in df["abide"].tolist():
            index = df["abide"].tolist().index(item)
            data[item] = df["respecter"].tolist()[index]
            f1.write(df["respecter"].tolist()[index])
            f1.write("\n")
