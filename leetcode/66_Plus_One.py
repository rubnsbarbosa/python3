
n = [4,3,2,1]

def plus_one(digits):
    digits[len(digits) - 1] += 1
    return digits

print(plus_one(n))
