num = int(input("Enter a number: "))

original = abs(num)
reverse = 0

while original > 0:
    digit = original % 10
    reverse = reverse * 10 + digit
    original //= 10

if num < 0:
    reverse = -reverse

print("Reversed Number:", reverse)