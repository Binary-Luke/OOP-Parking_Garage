# from main import Car

class Garage():
    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5, 6, 7]
        self.payment = 0
        self.space = []
        self.currentTicket = {'paid': False}


    def takeTicket(self):
        print("Take your ticket here. ")
        self.space.append(self.tickets[0])
        print(f"You have been added to the lot! Your space is # {self.space[0]} ")

    def loiter(self):
        action = input("Would you like to leave the garage [exit]\nWould you like to pay for parking? [pay] ")
        if action == 'exit':
            self.leaveGarage()
        elif action == 'pay':
            self.payForParking()
            next = input("Are you ready to leave the garage? ")
            if next == 'yes':
                self.leaveGarage()
            else:
                print("Fine. Take your time.")
                self.loiter()
        else:
            print("Invalid Input")

        

    def payForParking(self):
        while True:
            paid = int(input("Pay $5 to park here. "))
            self.payment += paid
            if paid >= 5:
                self.currentTicket['paid'] = True
                print("Thank you, you have 15 minutes to leave the lot.")
                break
            else:
                print("Transaction not approved")
    
    def leaveGarage(self):
        print("Thanks for parking with us today. May I have your ticket")
        if self.currentTicket['paid'] == True:
            print("Thank you have a wonderful day!")
        else:
            self.payForParking()


# my_car = Garage()
# my_car.takeTicket()
# # # print(my_car.currentTicket)
# # # my_car.payForParking()
# # # print(my_car.currentTicket)
# my_car.leaveGarage()

while True:
    welcome = input("Would you like to park here? ")
    if welcome == 'yes':
        new_car = Garage()
        new_car.takeTicket()
        new_car.loiter()
    else:
        print("Okay... Have a nice day!")
        break


