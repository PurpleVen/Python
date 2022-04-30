#53_IT_Vendra, Question[5-2]
class DISTANCE:
    xfeet=int(input("Enter value of distance1 in feet : "))
    distance1 = xfeet
    xinches=float(input("Enter value of distance1 in inch : "))
    distance1 = xinches
    print("\n")
    yfeet=int(input("Enter value of distance2 in feet : "))
    distance2 = yfeet
    yinches=float(input("Enter value of distance2 in inch : "))
    distance2 = yinches



    feet = xfeet + yfeet
    inches = float(xinches+yinches)
print("\n")
print("The addition of distance in feet is : ", DISTANCE.feet)
print("The addition of distance in inches is : ", DISTANCE.inches)