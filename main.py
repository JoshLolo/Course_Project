import Course_Project

while True:
 city = (input("Please enter a zipcode or city (n to quit): "))  
 print()
 if city == 'n':
   print("Goodbye")
   break
 else:
   Course_Project.notmain(city)
   print()
