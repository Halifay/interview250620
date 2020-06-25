def get_zeros(n):
    ans = 0
    while n > 0:
        n //= 5
        ans += n
    return ans


print(get_zeros(5))
print(get_zeros(12))
print(get_zeros(100))
