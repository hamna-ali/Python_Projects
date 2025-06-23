PLACEHOLDER_NAME = "[name]"
with open("./Input/Names/invited_names.txt") as names:
	invited = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_content:
	content = letter_content.read()
	for name in invited:
		stripped_name = name.strip()
		new_letter = content.replace(PLACEHOLDER_NAME,stripped_name)
		with open(f"./Output/ReadyToSend/invitation_for{stripped_name}.dox",mode="w") as completed_letter:
			completed_letter.write(new_letter)

