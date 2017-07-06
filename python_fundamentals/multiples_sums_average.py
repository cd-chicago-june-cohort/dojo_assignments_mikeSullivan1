def print_odds(low,high):
    for i in range(low,high):
        if i % 2 == 1: # modulus 1 indicates odd
            print i

def print_increments(low,high,increment):
    for i in range(low,high):
        if i % increment == 0: # if i is divisible by 5
            print i

def print_sum(sum_list):
    sum = 0                 #initiates the =0
    for i in sum_list:      #i is the vale held at each index in the list sum_list
        sum += i            #adds current indexed value to sum
    print sum

def print_average(avg_list):
    sum = 0                 #initiates the =0
    for i in avg_list:      #i is the vale held at each index in the list sum_list
        sum += i            #adds current indexed value to sum
    values = len(avg_list)
    print sum/values

print_odds(1,1000)          #define range
print_increments(5,1000000,5) # calls function lower, upper and a variable increment
a = [1, 2, 5, 10, 255, 3]
print_sum(a)          
print_average(a)

