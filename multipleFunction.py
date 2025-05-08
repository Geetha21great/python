class multiFunction():
    def Subfields():
        print('Sub-fields in AI are:')
        print('Machine Learning')
        print('Neural Networks')
        print('Vision')
        print('Robotics')
        print('Speech Processing')
        print('Natural Language Processing') 
        
    def OddEven():
        num=int(input('Enter a number'))
        if ((num%2)==0):
            print(f'{num} is Even number')
        else:
            print(f'{num} is odd number') 

    def Elegible():
        gender=input('Your gender:')
        age = int(input('Your age:'))
        if (gender == 'male' or gender == 'Male')&(age >= 21):
            print('you are eligible for marriage')
        elif(gender == 'female' or gender == 'Female')&(age >= 18):
            print('you are eligible for marriage') 
        else:
            print('you are not eligible for marriage')

    def percentage():
        sub1=int(input('subject-1 :'))
        sub2=int(input('subject-2 :'))
        sub3=int(input('subject-3 :'))
        sub4=int(input('subject-4 :'))
        sub5=int(input('subject-5 :'))
        Total = (sub1+sub2+sub3+sub4+sub5)
        percentage = (Total/5)
        print('Total:',Total)
        print('percentage:',percentage)

    def triangle():
        Height=int(input('Height'))
        Breadth=int(input('Breath:'))
        Area_triangel=(Height*Breadth)/2
        print('Area Formula:(Height*Breadth)/2')
        print('Area of Triangle:',Area_triangel)
        
        Height1=int(input('Height1:'))
        Height2=int(input('Height2:'))
        Breadth=int(input('Breath'))
        perimeter_triangle=Height1+Height2+Breadth
        print('Perimeter Formula:Height1+Height2+Breadth')
        print('Perimeter of triangle',perimeter_triangle)