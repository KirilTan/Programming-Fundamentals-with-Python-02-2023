path_to_file = input()

parts = path_to_file.split("\\")
part_needed = parts[-1]

file_name, file_extension = part_needed.split(".")

print(f"File name: {file_name}\n"
      f"File extension: {file_extension}")
