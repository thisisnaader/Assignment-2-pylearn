a = int(input("Lower digi: "))
b = int(input("Upper digit: "))

gcd = 1
for i in range(1,a + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(gcd)