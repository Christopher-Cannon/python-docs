user_input = ""

print("\nOptions: distance - velocity - time")
print("Enter quit to exit")
user_input = input(" -> ")

if(user_input == "distance"):
    velocity = int(input("Velocity? -> "))
    time = int(input("Time? -> "))

    print("Distance is {}".format(velocity * time))
elif(user_input == "velocity"):
    distance = int(input("Distance? -> "))
    time = int(input("Time? -> "))

    print("Velocity is {}".format(distance / time))
elif(user_input == "time"):
    distance = int(input("Distance? -> "))
    velocity = int(input("Velocity? -> "))

    print("Time is {}".format(distance / velocity))
else:
    print("Invalid option")
