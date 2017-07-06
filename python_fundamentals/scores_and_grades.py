import random
def grades_list(num):
    grades = []
    for x in range(0,num):
        grades.append(random.randint(60,100))
    return grades

def grade_eval(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'

tengrades = grades_list(10)

for x in tengrades:
    print "Score:", x,"; Your grade is", grade_eval(x)