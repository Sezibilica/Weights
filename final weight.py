#welcome interface
print("Welcome to the UNEB weight calculation application website.")
#to get user's course preference

course = input('''Please select a course from:
                  -Computer Science
                  -Law
                  -Medicine
                  -Economics
                  -Engineering''')
#to get the user's subjects and compare accordingly
#######################################################lastdone####################################
combination = sorted(input('Please enter your combination in the format: "P C B submath"'))

courses = {"Computer_Science":["C", "E", "M", "P", "subict"],\
           "Law":["D","E","H","L"],\
           "Medicine":["B", "C", "M", "P"],\
           "Economics":["E", "H", "L", "M"],\
           "Engineering":["B", "C", "M", "P"]
           }



legend  = {"A" : 6, "B" : 5, "C": 4, "D" : 3, "E" : 2, "O" : 1, "F" : 0}
best = input ("Enter your best subject's results")

if best == "A":
    weight = legend.get("A")*3
elif best =="B":
    weight = legend.get("B")*3
elif best == "C":
    weight = legend.get("C")*3
elif best =="D":
    weight = legend.get("D")*3
elif best == "E":
    weight = legend.get("E")*3
elif best =="O":
    weight = legend.get("O")*3
elif best =="F":
    weight = legend.get("F")*3

second = input("Enter your second best subject's results")

if second == "A":
    weight2 = weight + legend.get("A")*3
elif second =="B":
    weight2 = weight +legend.get("B")*3
elif second == "C":
    weight2 = weight +legend.get("C")*3
elif second =="D":
    weight2 = weight +legend.get("D")*3
elif second == "E":
    weight2 = weight +legend.get("E")*3
elif second =="O":
    weight2 = weight +legend.get("O")*3
elif second =="F":
    weight2 = weight +legend.get("F")*3

third = input("Enter your third best subject's results")

if third == "A":
    weight3 = weight2 + legend.get("A")*2
elif third =="B":
    weight3 = weight2 + legend.get("B")*2
elif third == "C":
    weight3 = weight2 + legend.get("C")*2
elif third =="D":
    weight3 = weight2 + legend.get("D")*2
elif third == "E":
    weight3 = weight2 + legend.get("E")*2
elif third =="O":
    weight3 = weight2 + legend.get("O")*2
elif third =="F":
    weight3 = weight2 + legend.get("F")*2

gen = input("Enter your result for General Paper")
if int(gen) <= 6:
    weight4 = weight3 + 1
else: weight4 = weight3 + 0

sub = input("Enter your grade for submath or subict")

if int(sub) <= 6:
    final_weight = weight4 + 1
else: final_weight = weight4 + 0

print(f"Your weights are {final_weight}")
