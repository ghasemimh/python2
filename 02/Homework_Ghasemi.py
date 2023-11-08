print()
# print friends
print("print friends")
friends  = ["Allameh" , "Meshkati" , "Moojani" , "Morshed" , "Mohebbi"]
for friend in friends:
    print(friend)

print()

# add me and print friends again
print("add me and print friends again")
friends.append("Ghasemi")
for friend in friends:
    print(friend)
    
print()

# moving index 2 with 3 and print again
print("moving index 2 with 3 and print again")
index0 = friends[0]
index2 = friends[2]
friends[0] = index2
friends[2] = index0
for friend in friends:
    print(friend)
    
print()

# removing me and print again
print("removing me and print again")
friends.remove("Ghasemi")
for friend in friends:
    print(friend)
     
print()