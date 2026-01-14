foods = []
n = int(input("Enter number of favorite foods: "))
for i in range(n):
    food = input("Enter a favorite food: ")
    foods.append(food)

favorites = {}
for i in range(len(foods)):
    person = input("Enter name for person " + str(i+1) + ": ")
    favorites[person] = foods[i]

print("Favorite foods list:", foods)

print("Favorite foods dictionary:", favorites)
