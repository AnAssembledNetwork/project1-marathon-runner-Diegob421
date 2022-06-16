
# """
#  *****************************************************************************
#    FILE:        marathon.py
#
#    AUTHOR:      {Your Name Here}
#
#    ASSIGNMENT: A marathon calculator to determine if a U.S. participant can
#    run in the Tokyo Marathon. 
#
#    DATE:         {Today's Date}
#
#    DESCRIPTION: {Your Description Here}
#
#  *****************************************************************************

# $1 = 134.28¥
JAPANESE_YEN = 134.28

# 1 mi = 1609.34 meters
METERS_IN_MILE = 1609.34 

KM_IN_MILE = 1.60934

# Insert Code Below
def fitness():
  print("Tokyo Marathon Qualifier")
  name = input("Please enter your name: ")
  miles_per_10mins = float(input("How many miles can you run in 10 minute? "))
  money_saved = (input("How much U.S.$ do you have saved for the marathon? "))
  space = name.find(" ")
  last = name[space + 1:]
  dollars = money_saved[1:]
  km_per_10mins = miles_per_10mins*KM_IN_MILE
  km_per_min = km_per_10mins/10
  dollars = float(dollars)
  yen_to_spend = dollars*JAPANESE_YEN
  print(f"Dear {last}, you have a pace of {km_per_min:.2f} km/min. ") 
  print(f"Additionally, you only have {yen_to_spend:.2f}¥ to spend.")

# This ignores our code so that we do not get an error Remove 'pass' when you want to start testing code.
    
    
    

# This invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    fitness()
