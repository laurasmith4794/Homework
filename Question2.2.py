def count_squares(x):
    # base case
    if x == 0:
        return 0
    # recursive case
    else:
        return x**2 + count_squares(x-1)

print(count_squares(1)) #1
print(count_squares(2)) #5
print(count_squares(3)) #14
print(count_squares(4)) #30