import math

Operation = input("please select input")

while (Operation != "exit"):


    if Operation == "+":
        var = input("Please enter first number: ")
        var2 = input("Please enter second number: ")
        print("Result: " + str(float(var) + float(var2)))-
        result = str(float(var) + float(var2))

    if Operation == "-":
        var = input("Please enter first number: ")
        var2 = input("Please enter second number: ")
        print("Result: " + str(float(var) - float(var2)))
        result = str(float(var) - float(var2))

    if Operation == "/":
        var = input("Please enter first number: ")
        var2 = input("Please enter second number: ")
        print("Result: " + str(float(var) / float(var2)))
        result = str(float(var) / float(var2))

    if Operation == "*":
        var = input("Please enter first number: ")
        var2 = input("Please enter second number: ")
        print("Result: " + str(float(var) * float(var2)))
        result = str(float(var) * float(var2))

    if Operation == "X":
        var = input("Please enter first number: ")
        var2 = input("Please enter second number: ")
        result = str(float(var) * float(var2))
        print("Result: " + result)

    if ((Operation == "") or (Operation == "u")):
        Operation0 = input("please select input")
        if Operation0 == "X":
            var3 = input("Please enter second number: ")
            print("Result: " + str(float(result) * float(var3)))
            result = str(float(result) * float(var3))


        if Operation0 == "+":
            var3 = input("Please enter second number: ")
            print("Result: " + str(float(result) + float(var3)))
            result = str(float(result) + float(var3))


        if Operation0 == "-":
            var3 = input("Please enter second number: ")
            print("Result: " + str(float(result) - float(var3)))
            result = str(float(result) - float(var3))

        if Operation0 == "*":
            var3 = input("Please enter second number: ")
            print("Result: " + str(float(result) * float(var3)))
            result = str(float(result) * float(var3))

        if Operation0 == "/":
            var3 = input("Please enter second number: ")
            print("Result: " + str(float(result) / float(var3)))
            result = str(float(result) / float(var3))

    Operation = input("please select input (or press Enter to continue, or write exit to close)")


