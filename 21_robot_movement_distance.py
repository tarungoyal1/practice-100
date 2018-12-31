# Question 21
# Level 3
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

from math import sqrt

def calculateDistance(movements):
    """
    :param movements:
        this is a list containing tuples of Direction and steps covered by robot
    :return: an integer which is a distance between the final computed point and origin(0,0)
    """

    pos = [0,0]

    for dir,steps in movements:
        d = dir.lower()
        if d=='up':
            pos[0]+=int(steps)
        elif d=='down':
            pos[0]-=int(steps)
        elif d=='left':
            pos[1]-=int(steps)
        elif d=='right':
            pos[1]+=int(steps)
    return int(round(sqrt((pos[0]**2)+(pos[1]**2))))

def main():
    # first ask for the direction and steps in tuples
    movements = []
    validmovements = {'up','down','left','right'}
    validsteps = {n for n in range(0,10)}

    while 1:
        i = str(input()).split(' ')
        if len(i)==2:
            if set(i[0].lower()).isdisjoint(validmovements):
                if set(i[1].lower()).isdisjoint(validsteps):
                    movements.append(tuple(i))
        else:
            break

    print(calculateDistance(movements))


if __name__=='__main__':
    main()