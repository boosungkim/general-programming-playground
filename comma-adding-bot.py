print("Hello! Welcome to Commas Are Necessary!")
print("Here at C.A.N, we make sure your lists of words have the appropriate comma and \"and\" usage!")
print("Please enter the words you wish to list one by one. Type one word, hit enter, and then write the next one:")

first = input()
list = [first]
while True:
    print("Please enter your next word. Please type \"Finished CAN\" to indicate that you have finished.")
    ha = input()
    if ha == "Finished CAN":
        break
    else:
        list.append(ha)


if len(list) == 1:
    print(list[0])
elif len(list) == 2:
    print(list[0] + " and " + list[1])
else:
    for i in range(0, len(list) - 1):
        print(list[i] + ", ", end = "")
    print("and " + list[len(list) - 1])

print("Thank you for using C.A.N! Feel free to restart for a whole new list. Also, please be sure to cite this program"
      " on your English paper.")
