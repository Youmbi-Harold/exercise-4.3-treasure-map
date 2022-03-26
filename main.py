# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#first we need to get hold of the entered string in the form of a list and converting it into integer e.i digit1 digit2 with position 0 and 1 respectively
H_point = int(position[0])#horizontal point with place value 0
V_point = int(position[1])#vertical point with place value 1
box = map[V_point - 1]# I used a variable to address the vertical list of those box not forgetting they start at 0
box[H_point - 1] = 'X'#now, I address the vertical list using the horizontal point just like in a list not forgetting it starts at place value 0



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")