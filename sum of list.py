def list_sum(items):
    total = 0
    for i in items:
        total += i
    return total

nums = [1, 2, 3, 4, 5]
print("Sum:", list_sum(nums))
