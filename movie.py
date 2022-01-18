#program to make movie ticket thingy
movies = ('mov1',"mov2",)
theaters = ("t1","t2","t3",)

location = input("Enter your city : ")
x = 0
select = 0 
def select_mov():
    s = int(input("\nEnter the serial no of the your selection : "))
    print("You have selected :",movies[s-1])
    conf = input("Press Y to continue, N to reselect ")
    if conf == "Y" or conf == "y" :
        return s
def select_the():
    s = int(input("\nEnter the serial no of the your selection : "))
    print("You have selected ",theaters[s-1],"theater")
    conf = input("Press Y to continue, N to reselect ")
    if conf == "Y" or conf == "y" :
        return s
        
#selects movie        

print("\nThis week's trending movies are :")
for i in movies:
    print(x+1,". ",i)
    x=x+1
x = 0

while True :
    temp = select_mov()
    if temp != None :
        selection_mov =  temp - 1
        break
    
#selects theater

print("\nSelect your preferred theater :")
for i in  theaters:
    print(x+1,". ",i)
    x += 1
    
while True :
    temp = select_the()
    if temp != None :
        selection_the =  temp - 1
        break

print(movies[selection_mov])
print(theaters[selection_the])