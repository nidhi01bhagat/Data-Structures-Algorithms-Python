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



Question: 4 
class Solution:
    def largestElement(self, nums: List[int]) -> int:
        # Approach 1: sort and pick last
        # nums.sort()
        # return nums[-1]

        # Approach 2 (optimal): scan once
        largest = nums[0]
        for num in nums:
            if num > largest:
                largest = num
        return largest



Question 5: from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        
        for i in range(n):
            # Compare current with next (circular using %)
            if nums[i] > nums[(i + 1) % n]:
                count += 1
            # If more than one break, not sorted+rotated
            if count > 1:
                return False
        
        return True
Question 6 
def getElements(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)  # edge case when only one element is present in array
    arr.sort()
    small = arr[1]
    large = arr[n-2]
    print("Second smallest is", small)
    print("Second largest is", large)

if __name__ == '__main__':
    arr = [1, 2, 4, 6, 7, 5]
    n = len(arr)
    getElements(arr, n)

Question 7 Second Largest Element :
def second_largest(nums):
    # One pass, O(n) time, O(1) space
    if len(nums) < 2:
        return -1

    largest = float('-inf')
    second = float('-inf')

    for x in nums:
        if x > largest:
            # x becomes the new largest; old largest may become second
            second, largest = largest, x
        elif largest > x > second:
            # x is strictly between current largest and second
            second = x

    return second if second != float('-inf') else -1


8: Linear Search : class Solution:
    def find_index_rec(arr, num, i=0):
    if i == len(arr):
        return -1
    return i if arr[i] == num else find_index_rec(arr, num, i+1)


9: Linear Search : def first_index(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1

10: Left Rotate an array by one place
from typing import List
import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # In-place triple reversal, O(1) extra space
        n = len(nums)
        if n == 0:
            return
        k %= n
        if k == 0:
            return

        def rev(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1; r -= 1

        rev(0, n - 1)
        rev(0, k - 1)
        rev(k, n - 1)

11: Number is Palindrome or not solve it without using string 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negatives or numbers ending with 0 but not 0 itself can't be palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10
        
        # Even length: x == reversed_half
        # Odd length: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10


12 : with string 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)           # convert number to string
        return s == s[::-1]  # check if forward == backward
# This solution runs in O(d) time and O(d) space, where d is the number of digits. It’s simple, but not optimal in terms of space. If we want O(1) space, we need the math-based approach.
it uses extra memory (because it creates a string).

