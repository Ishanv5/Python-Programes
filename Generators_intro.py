# Generators are iterators...
def nums(n):
    for i in range(1,n+1):
        yield(i)
        
print(nums(10))
for nos in nums(10):
    print(nos)

nos=nums(10)
for nums in nos:
    print(nums)