# 4. Write a recursive function to calculate the sum of first n natural numbers.
def sum_numbers(n):
    if n == 1 or n == 0 :
        return n
    result = n + sum_numbers(n-1)
    return result

num = int(input("Enter a number: "))
total = sum_numbers(num)
print(f"The sum of first {num} natural numbers is {total}")
