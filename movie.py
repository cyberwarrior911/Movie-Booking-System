"""
CS Project (Term 2)

TOPIC : Movie Ticket Booking
Made by : Mayank Kushwaha  (17)  XII C 
          Ankit Lodhi      (05)  XII C
"""

import os
movies = ('Spiderman : No Way Home',"K.G.F. Chapter 2",)    #Edit to add more movies
theaters = ("Jugal Palace","CineMax","Inox",)               #edit to add more theaters and add same no. of elements to prices
prices = ("150","210","300")
timings = (
    "10:30 AM - 12:30 PM",
    "01:00 PM - 03:00 PM",
    "03:30 PM - 05:30 PM",
    "06:00 PM - 08:00 PM",
    "08:30 PM - 10:30 PM",
)
billno = 0
x = 0
select = 0 

# Functions

def select_mov():
    s = int(input("\nEnter the serial number of your selection : "))
    print("You have selected :",movies[s-1])
    conf = input("Enter Y to continue, N to reselect : ")
    if conf == "Y" or conf == "y" :
        return s
def select_the():
    s = int(input("\nEnter the serial number of your selection : "))
    print("You have selected ",theaters[s-1],"theater")
    conf = input("Enter Y to continue, N to reselect : ")
    if conf == "Y" or conf == "y" :
        return s
def select_time():
    s = int(input("\nEnter the serial number of your selection : "))
    print("You have selected ",timings[s-1],"show")
    conf = input("Enter Y to continue, N to reselect : ")
    if conf == "Y" or conf == "y" :
        return s
def select_seats():

    print("""                           SCREEN THIS SIDE   


             A     |_| |_| |_| |_| |_| |_| |_|     |_| |_| |_| |_| |_| |_| |_| 

             B     |_| |_| |_| |_| |_| |_| |_|     |_| |_| |_| |_| |_| |_| |_| 
             
             C     |_| |_| |_| |_| |_| |_| |_|     |_| |_| |_| |_| |_| |_| |_| 
             
             D     |_| |_| |_| |_| |_| |_| |_|     |_| |_| |_| |_| |_| |_| |_| 
             
             E     |_| |_| |_| |_| |_| |_| |_|     |_| |_| |_| |_| |_| |_| |_| 
             
             F     |_| |_| |_| |_| |_| |_| |_|     |_| |_| |_| |_| |_| |_| |_| 
             
             G     |_| |_| |_| |_| |_| |_| |_|     |_| |_| |_| |_| |_| |_| |_|
             
             H     |_| |_| |_| |_| |_| |_| |_|     |_| |_| |_| |_| |_| |_| |_|

                    1   2   3   4   5   6   7       8   9   10  11  12  13  14   """)
    global seats
    seats = {}
    i = 0
    while True:
        seatrow = input("\nEnter your desired seat row [like A,B,C...] : ").lower()
        seatcol = input("\nEnter your seat coloumn [1,2,3...] : ")
        if seatrow.__len__() == 1 and seatrow in "abcdefgh" and seatcol.isnumeric() == True and (int(seatcol) < 15 and int(seatcol) > 0):     
            seats[i] = seatrow.upper() + seatcol
            i =+ 1
        else :
            print("\ninput error...")
        
        con = input("\nY : more   |    N : end and checkout : ")
        if con.lower() == "n":
            global tickets
            tickets = len(seats)
            break
def billing():
    name = input("\nEnter name : ")
    show_time = timings[selection_time]
    venue = theaters[selection_the]
    movie = movies[selection_mov]
    mobileno = input("Enter mobile no. for payment : ")
    seatno = seats[billno]
    price = prices[selection_the]
    f = open("bill("+seatno+").txt",'w')
    f.write("Name : ")
    f.write(name)
    f.write("\nMovie : ")
    f.write(movie)
    f.write("\nShow time : ")
    f.write(show_time)
    f.write("\nTheater / Venue : ")
    f.write(venue)
    f.write(", ")
    f.write(location.capitalize())
    f.write("\nTicket Price : Rs. ")
    f.write(price)
    f.write("\nMoney Paid via UPI. Mobile no. used : ")
    f.write(mobileno)
    f.write("\nHave Fun !!!")
    f.close()

# __main__

os.system('cls' if os.name == 'nt' else 'clear' )

location = input("Enter your city : ")

# selects movie        

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
    
# selects theater

print("\nSelect your preferred theater :")
for i in  theaters:
    print(x+1,". ",i)
    x += 1
x = 0   
while True :
    temp = select_the()
    if temp != None :
        selection_the =  temp - 1
        break


# selects timing

print("\nSelect your preferred show timings :")
for i in  timings:
    print(x+1,". ",i)
    x += 1
x = 0  
while True :
    temp = select_time()
    if temp != None :
        selection_time =  temp - 1
        break

select_seats()

for billno in range(tickets):
    billing()
print("\nticket booked succesfully !, bill saved at current directory\n\n")


