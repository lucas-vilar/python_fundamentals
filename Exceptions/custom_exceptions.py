class TooFarException(Exception):
    def __str__(self):
        return "You are too far from us. We can't deliver your food"
    
def delivery_system(distance):
    if distance > 30:
        raise TooFarException()
    else:
        print("Preparing your food!")

delivery_system(int(input('Type the distance: ')))