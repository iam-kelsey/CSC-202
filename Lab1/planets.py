# Kelsey Nguyen
# Section 07

def weight_on_planets():
   age = int(input("What do you weigh on earth? "))
   my_string = "\nOn Mars you would weigh {:.2f} pounds.\nOn Jupiter you would weigh {:.2f} pounds."
   print(my_string.format(age*0.38, age*2.34))


if __name__ == '__main__':
   weight_on_planets()