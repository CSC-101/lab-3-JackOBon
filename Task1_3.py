def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and 3, 4; 4,5
                                             # the corresponding return value.


def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and  1,2,3; false, true, true
                                             # the corresponding return value.


answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer?[4, 5]
print()