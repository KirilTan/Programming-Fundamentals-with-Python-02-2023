encrypted_message = input()

decrypted_message = encrypted_message

command = input().split("|")
while command[0] != "Decode":

    if command[0] == "Move":  # Move command[1] amount of letters to the back of the string
        number_of_letter_to_move = int(command[1])
        decrypted_message = decrypted_message[number_of_letter_to_move:] + decrypted_message[:number_of_letter_to_move]

    elif command[0] == "Insert":  # Insert the given value before the given index in the string
        index, value = int(command[1]), command[2]
        decrypted_message = decrypted_message[:index] + value + decrypted_message[index:]

    elif command[0] == "ChangeAll":  # Change all occurrences of the given substring with the replacement text
        substring, replacement_text = command[1], command[2]
        decrypted_message = decrypted_message.replace(substring, replacement_text)

    command = input().split("|")

print(f"The decrypted message is: {decrypted_message}")
