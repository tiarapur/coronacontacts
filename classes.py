#this code is based on the Garfield Example we did in class
#class user
class User:
    def __init__(self, id, userName, password):
        self.id = id
        self.password = password

#subclass customer
class customer(User):
    def __init__(self, c_name, c_mail, c_number):
        self.c_name = c_name
        self.c_mail = c_mail
        self.c_number = c_number

#sublass reservation
class reservation:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def make_reservation(self):
        for i in range(5):
            print("***" * i)
        print(self.name + " has made a reservation for", self.size)

Lisa = reservation("Lisa", 2 )
Mark = reservation("Mark", 1)
print(reservation.make_reservation(Lisa))
print(reservation.make_reservation(Mark))

class restaurant(User):
    def __init__(self, r_name, r_mail, r_number, r_address, r_capacity):
        self.r_name = r_name
        self.r_mail = r_mail
        self.r_number = r_number
        self.r_address = r_address
        self.r_capacity = r_capacity
        self.inventory = []
        self.occupied = 0

    def say_information(self):
        for i in range(5):
            print("****" *i)
        print("This places is called: " + self.r_name + "\nYou can find us here: " + self.r_address
              + "\nor contact us via our number (" + self.r_number + ") or E-Mail (" + self.r_mail + ")" +
              "\nUnfortunetly due to the corona virus or capacity is limited, our max. capacity is:", self.r_capacity )

    def add_people(self,reservation):
        if self.occupied + reservation.size <= self.r_capacity:
            self.occupied += reservation.size
            self.inventory.append(reservation)
            print(reservation.name + " was successfully added to the reservation list.")
        else:
            print(self.r_name + " is unfortunetly fully booked \nhence, " + reservation.name + ", your booking was unsuccessful")


tokas = restaurant("Tokas", "tokas@gmail", "+491702792", "Müllerstraße 101", 2)

print(restaurant.say_information(tokas))

#adding the number of people to the restaurant
theRestaurant= tokas
theRestaurant.add_people(Lisa)
theRestaurant.add_people(Mark)





