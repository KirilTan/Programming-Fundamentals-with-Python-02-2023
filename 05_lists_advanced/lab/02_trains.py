starting_train = [0] * int(input())

end_train = starting_train.copy()

while True:
    command = input().split()

    if command[0] == "End":
        break

    elif command[0] == "add":
        people = int(command[1])
        end_train[-1] += people

    elif command[0] == "insert":
        people = int(command[2])
        index = int(command[1])
        end_train[index] += people

    elif command[0] == "leave":
        people = int(command[2])
        index = int(command[1])
        end_train[index] -= people

print(end_train)
