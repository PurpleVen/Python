#53_IT_Vendra, Question[3,2]
def simple_interest(p, t, r):
    print("\n")
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r) / 100
    print("\n")
    print("==========================")
    print('The Simple Interest is', si)
    print("==========================")
    return si

simple_interest(p = int(input("Enter the principal amount: ")), t = int(input("Enter time period: ")), r = int(input("Enter rate of interest: ")))

