#dictionary application.
fstudent={'name':'lydia','age':22,'courses':['eng','math']}
mstudent={'name':'leo','age':28,'courses':['eng','math']}
female=fstudent
male=mstudent

print(fstudent['name'])
fstudent['weight']='64'
print(fstudent)
for key,value in fstudent.items():
    print("key:")
    print(key)
    print("value:")
    print(value)
    print(' ')

if female==fstudent:
    print("Student details are: ", fstudent)
else:
     print("Student details are: " ,mstudent)


#example 2
item1 ={'shop':'bread','price':5000} 
item2 ={'shop':'milk','price':2000} 
item3 ={'shop':'butter','price':6000} 
item4 ={'shop':'eggs','price':15000}   
shopping_list=[item1,item2,item3,item4]
for i in shopping_list:
    buy =i.get('shop',)
    print(buy) 


#example 3
school_shopping ={}
school_items= True
while school_items:
    items =input("\nplease enter item name: ")
    prices=input("please enter item price: ")  

    school_shopping[items]=prices
    other =input("\n would you like to specify the quantity: ") 
    if other=='no':
        school_items = False
        print("\n--------school shopping list----------") 
        for items,prices in school_shopping.items():
            print( items , ": ", prices)       
    elif other== 'yes':
        more = input("Add quantity: ")
        
        print("\n--------school shopping list----------")
        print(more, items, ":",prices)



# print("\n--------school shopping list----------") 
# for items,prices in school_shopping.items():
#     print( items , ": ", prices)      

