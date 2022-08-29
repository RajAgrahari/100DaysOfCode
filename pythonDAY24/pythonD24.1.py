with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()
with open("Input/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()
    for n in names:
        new_name = n.strip()
        new_letter = letter.replace("[name]", new_name)
        with open(f"Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as f:
            f.write(new_letter)
