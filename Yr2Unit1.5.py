#Jessica
#Bouncing Ball

def enter():
    num = int(input("Enter the corresponding number for the ball used: "))
    if num >= 1 and num <= 4:
        cor = [0.7,0.75,0.9,0.3]
        cor2 = cor[num-1]
        height = float(input("Enter the initial height in meters: "))
        if height > 0:
            return calc(num,height,cor2)
        else:
            print ("Invalid, must be more than zero")
            return enter()
    else:
        print ("Invalid, look at the list")
        return enter()

def mtocm(height):
    return height * 100

def cmtom(dt):
    return dt / 100

def calc(num,height,cor2):
    height = mtocm(height)
    bounce = 1
    dt = height
    while height * cor2 >= 10:
        height = cor2 * height
        dt += (2 * height)
        bounce +=1
    dt = cmtom(dt)
    return display(dt,bounce)

def display(dt,bounce):
    print ("Number of bounce:",bounce)
    print ("Meters traveled:",round(dt,2))
        


def main():
    print ("1 - Tennis Ball\n2 - Basketball\n3 - Super Ball\n4 - Softball")
    return enter()    
    

main()
