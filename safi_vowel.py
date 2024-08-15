vowels = ["a","e","i","o","u","A","E","I","O","U"]
word = input("Enter word")
sh = 0
for s in word:
    for h in vowels:
        if s == h:
            sh = sh+1
            print(s)
print(sh)
