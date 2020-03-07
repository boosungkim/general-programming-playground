def collatz():
    while True:
        try:
            print("Please input an integer")
            number = int(input())
            while True:
                if number == 1:
                    print("done")
                    break
                elif number%2 == 0:
                    number = number//2
                    print(number)
                else:
                    number = number*3 + 1
                    print(number)
        except:
            print("I said integer you fucking idiot!")
            continue
collatz()
