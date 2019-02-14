import random

print("\n")
print("Airline Booking System\n")


class Person:   # base class #1 Person ==> Passenger and Employee Class will inherit from Person

    def __init__(self, first, last):    # example of use of self.
        self.first = first
        self.last = last

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


class Passenger(Person):    # class #2 Passenger. Inherits from Person class

    def __init__(self, first, last, passport, choice):
        super().__init__(first, last)   # super call
        self.passport = passport
        self.choice = choice


class Employee(Person): # class #3 Employee. Inherits from Person class

    def __init__(self, first, last, job_title):
        super().__init__(first, last)   # super call
        self.job_title = job_title


class Destination: # class #4 base class; used for displaying flight options
    def __init__(self, location):
        self.location = location

    def display_location(self):
        print("List of current available flights:")
        print("-----------------------------------")
        for flights in self.location:
            print(flights)


class Airline: # class #5 base class; generates random number for flight and gate number
    def __init__(self, flight_number = random.randint(100,700), gate_number = random.randint(1,40)):
        self.flight_number = flight_number
        self.gate_number = gate_number

    def plane_info(self):
        print("Flight number:", self.flight_number, "Gate number:", self.gate_number)


class Payment(Passenger): # class #6, example of multiple inheritance, inherits from Passenger that inherits from Person
    def __init__(self, first, last, passport, choice, card):
        super().__init__(first, last, passport, choice)
        self.__card = card  # private data member


def main():


    flights = Destination([("Select 1:", "NRT", 1800), ("Select 2:", "LAX", 550), ("Select 3:", "MCI", 300)])
    # instance of Destination; class will display different flight options

    plane1 = Airline() # instance of Airline, will RNG flight number and gate number for plane


    done = False    # allows for users who choose option one to be able to opt into option 2

    while done is False:

        print("\n")
        print("Options Menu")
        print("1: Display available flights")
        print("2: Book a flight")

        option = int(input("Select option: "))

        if option == 1:
            print("\n")
            flights.display_location()  # display flight options

        if option == 2:

            booking_choice = int(input("To book as a passenger, enter 1. to book as an employee, enter 2. "))
            # book as a passenger or employee

            if booking_choice == 1:

                # instance of Passenger; user inputs needed information for class
                per1 = Passenger(input("First name: "), input("Last name: "), input("Passport information: "),
                                 int(input("Flight Choice: ")))

                if per1.choice == 1:

                    # instance of Payment; overrides per1 and allows to enter credit card information
                    per1 = Payment(per1.first, per1.last, per1.passport, per1.choice,
                                   int(input("Enter Card Information:")))

                    print("PRINTING TICKET:\n")
                    print(per1.fullname())
                    plane1.plane_info()
                    print("Flight Destination: NRT. Total Cost = $1800.00")
                    input()
                    done = True

                elif per1.choice == 2:

                    # instance of Payment; overrides per1 and allows to enter credit card information
                    per1 = Payment(per1.first, per1.last, per1.passport, per1.choice,
                                   int(input("Enter Card Information: ")))

                    print("PRINTING TICKET:\n")
                    print(per1.fullname())
                    plane1.plane_info()
                    print("Flight Destination: LAX. Total Cost = $550.00")
                    input()
                    done = True

                elif per1.choice == 3:

                    # instance of Payment; overrides per1 and allows to enter credit card information
                    per1 = Payment(per1.first, per1.last, per1.passport, per1.choice,
                                   int(input("Enter Card Information: ")))

                    print("PRINTING TICKET:\n")
                    print(per1.fullname())
                    plane1.plane_info()
                    print("Flight Destination: MCI. Total Cost = $300.00")
                    input()
                    done = True

            elif booking_choice == 2:

                # instance of Employee class, user enters first/last name and job title
                employee = Employee(input("First name: "), input("Last name: "), input("Enter job title: "))
                print(employee.fullname())
                print(employee.job_title)
                print("Thank you for signing in. Please wait for job assignment.")
                input()
                done = True


main()  # run main function

