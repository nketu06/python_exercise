nums = range(10)

squared = (x*x for x in nums)
evens = (x for x in squared if x % 2 == 0)
print(next(evens),evens.__next__())
 