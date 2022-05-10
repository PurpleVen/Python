#53_IT_Vendra, Question[2-3]
list =[9, 2, 87, 36, 54, 21, 57, 1]

ch=0

while ch!=3:

    ch = int(input('1.Ascending  2.Descending  3.Exit \n'))
    if ch==1:
        list.sort(reverse=False)
        print('Ascending Sorted list : ',list)

    elif ch ==2:
        list.sort(reverse=True)
        print('Desccending Sorted list : ',list)

    else:
        ch=3
