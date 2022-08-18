class Car:
  def __init__(self, color, make, model, num_of_doors, is_manual, current_speed, top_speed):
    self.color = color
    self.make = make
    self.model = model
    self.num_of_doors = num_of_doors
    self.is_manual = is_manual
    self.current_speed = current_speed
    self.top_speed = top_speed

  def accelerate(self, rate):
    self.current_speed += rate

  def decelerate(self, rate):
    self.current_speed -= rate


car_1 = Car("red", "Honda", "Civic", 2, True, 0, 120)
car_2 = Car("black", "Tesla", "Model X", 4, False, 0, 200)

print(car_1.current_speed)
car_1.accelerate(40)
print(car_1.current_speed)

print(car_2.current_speed)
car_2.accelerate(65)
print(car_2.current_speed)
car_2.decelerate(30)
print(car_2.current_speed)




def make_car_go(car, speed):
  car['current_speed'] = speed


# car_2 = {
#   "color": "black",
#   "make": "Tesla",
#   "model": "Model X",
#   "num_of_doors": 4,
#   "is_manual": False,
#   "current_speed": 0
# }

# car_3 = {
#   "color": "white",
#   "make": "Toyota",
#   "model": "Prius",
#   "num_of_doors": 4,
#   "is_manual": False,
#   "current_speed": 0
# }