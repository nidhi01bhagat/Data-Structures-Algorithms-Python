#Question1
#Monthly Expenses Data
exp = [2200, 2350, 2600, 2130, 2190]

#The difference between February's expenses and January's expenses
FebExp = exp[1] - exp[0]
print(FebExp)

#Total Spending in the First Quarter
FirQuat = exp[0] + exp[1] + exp[2]
print(FirQuat)

#Find out if you spent exactly 2000 dollars in any month
Exact = 2000 in exp
print(Exact)
#If $2000 is in the list, it prints True; otherwise, it prints False
#it will gives us false 

#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

exp.append(1980)
print(exp)

#You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense listbased on this based on this

#The expense for April is reduced by $200 to account for a refund or correction

exp[3] = exp[3] - 200
print(exp)

# question 2 
# Length of the list
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america'] #initialize the list 

print(len(heros))  

#Add 'black panther' at the end of this list
heros.append("black panther")
print(heros)

#Removes "black panther" and reinserts it at index 3 using insert()
heros.remove("black panther")  # Removes the last item
heros.insert(3, "black panther")  # Inserts it at position 3
print(heros)

#Now you don't like thor and hulk because they get angry easily :),So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.
heros[1:3] = ["doctor strange"] #slicing [1:3= 1,2..3]
print(heros)

#Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)

#Question 3 
#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
max = int(input("Enter the max number= "))

odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:  #  if the number is odd
        odd_numbers.append(i)  # Add odd numbers to the list
print("odd__numbers", odd_numbers)

