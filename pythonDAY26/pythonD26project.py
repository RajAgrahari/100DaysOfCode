# NATO PHONOTIC CODING
import pandas

nato_data = pandas.read_csv("natoPhonoticData.csv")
nato_dataframe = pandas.DataFrame(nato_data)
# print(nato_dataframe)
nato_dict = {row.letter.strip(): row.code for (index, row) in nato_dataframe.iterrows()}
# print(nato_dict)
name = input("ENTER YOUR NAME :").upper()
all_code = [nato_dict[items] for items in name]
print(all_code)
