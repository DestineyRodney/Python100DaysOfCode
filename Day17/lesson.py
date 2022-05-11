# creating a class
#  NAME PascalCase
# can use pass if nothing in class
# class User:
#     pass
#
#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Michael"
# print(user_1.username)

# Constructor (initialized) by using init function

# init function will be called everytime new object is created
# self is actual object being initialized
class Car:
    def __init__(self, seats):
        self.seats = seats

    def enter_race_mode(self):
        self.seats = 2


my_car = Car(5)
print(my_car.seats)


class User:
    def __init__(self, username, user_id):
        self.username = username
        self.id = user_id
        self.followers = 0
        self.following = 0
# followers given a default value

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("Bobby", "1")
print(user_1.username)
print(user_1.id)
print(user_1.followers)

user_2 = User("Ray", "2")

user_1.follow(user_2)
print(f"Following: {user_1.following}")


# can also create methods



