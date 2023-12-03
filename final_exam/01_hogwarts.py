encrypted_message = input()
decrypted_message = encrypted_message

command = input().split()
while command[0] != "Abracadabra":

    if command[0] == "Abjuration":  # Replace all letters with upper case and print the result
        decrypted_message = decrypted_message.upper()
        print(decrypted_message)

    elif command[0] == "Necromancy":  # Replace all letters with lower case and print the result
        decrypted_message = decrypted_message.lower()
        print(decrypted_message)

    elif command[0] == "Illusion":  # Replace the letter at the index with the given one and print Done

        index, letter = int(command[1]), command[2]

        if 0 <= index < len(decrypted_message):
            decrypted_message = decrypted_message[:index] + letter + decrypted_message[index + 1:]
            print("Done!")
        else:  # If the index is invalid, print "The spell was too weak."
            print("The spell was too weak.")

    elif command[0] == "Divination":  # Replace the first substring(all matches) with the second and print the result.

        first_substring, second_substring = command[1], command[2]

        if first_substring in decrypted_message:
            decrypted_message = decrypted_message.replace(first_substring, second_substring)
            print(decrypted_message)
        else:  # If the string does not exist, skip the command.
            pass

    elif command[0] == "Alteration":  # Remove the substring from the string and print the result.

        substring = command[1]

        if substring in decrypted_message:
            decrypted_message = decrypted_message.replace(substring, "")
            print(decrypted_message)
        else:  # If the substring does not exist, skip the command.
            pass

    else:  # If the input command is invalid, print "The spell did not work!"
        print("The spell did not work!")

    command = input().split()

