import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phoenetic():
	name = input("Enter your name: ").upper()
	try:
		new_list = [data_dict[letter] for letter in name]
	except KeyError:
		print("Sorry! only alphabets allowed")
		generate_phoenetic()
	else:
		print(new_list)

generate_phoenetic()