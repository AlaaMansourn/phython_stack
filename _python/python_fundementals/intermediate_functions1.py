import random
def randInt(min , max ):
    num = round (random.random() * (max-min) + min)
    
    return num


l=randInt(5,15)
print(l)