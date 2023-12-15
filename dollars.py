yes_no = input("Do you need help with converting dollars to euros ")
while yes_no == "Yes":
    print("alright lets get started! ")
    number_of_euros = 1.9454
    number_of_dollars = float(input("How much money do you have usd "))
    num_of_dollars = number_of_dollars * int(number_of_euros)
    print("if you have " + str(number_of_dollars))
    print("This is your dollars converted to euros " + str(number_of_euros * number_of_dollars))
    yes_no = input("Do you need anything else?")
    while yes_no == "No":
        print("Have A Good Day!")
        break