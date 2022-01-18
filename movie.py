#program to make movie ticket thingy
movies = ('mov1',"mov2",)
Theaters = ()
location = input("Enter your city : ")
x = 0
select = 0 
def select():
    global s
    s = int(input("\nEnter the serial no of the your selection : "))
    print("You have selected :",movies[s-1])
    conf = input("Press Y to continue, N to reselect ")
    if conf == "Y" or conf == "y" :
        return s

print("\nTrending movies in ",location,"are :")
for i in movies:
    print(x+1,". ",i)
    x=x+1
    

while True :
    temp = select()
    if temp != None :
        selection =  temp - 1
        break
    
print(movies[selection])
    