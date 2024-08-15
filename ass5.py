my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
x = 0
while x < 3:
    x += 1
    for days in my_list:
        if days != "Monday":
            print(days)
        
