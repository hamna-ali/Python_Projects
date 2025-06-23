import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    student_dict = {key: value for (key, value) in student_dict.items()}

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # print(index)
    # print(row)
    # Access row.student or row.score
    # print(row.student)
    # print(row.score)
    pass


# Keyword Method with iterrows()
# new_dict = {row.student: row.score for (index, row) in student_data_frame.iterrows()}
# print(new_dict)

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv('nato_phonetic_alphabet.csv')
#print(data)
#print(data.to_dict())
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(data_dict)
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Enter your name: ").upper()
new_list = [data_dict[letter] for letter in name]
#last_dict = {letter: data_dict[letter] for letter in name}
print(new_list)
#print(last_dict)