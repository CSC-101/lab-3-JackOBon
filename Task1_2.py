def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and
                                           # the corresponding return value. 1:1, 2:4, 3:9, 4:16


squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print()                                    # values recorded above? The value of square is a list and this relates to the values above by replacing
                                            #the old values with the new ones.