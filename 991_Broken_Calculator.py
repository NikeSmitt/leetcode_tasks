# There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:
#
# multiply the number on display by 2, or subtract 1 from the number on display. Given two integers startValue and
# target, return the minimum number of operations needed to display target on the calculator.


from collections import namedtuple


def broken_calc(start_value: int, target: int) -> int:
    if start_value > target:
        return start_value - target
    
    inc = 1
    if target % 2 != 0:
        inc = 2
    
    res_bank = [0] * (target + inc)
    res_bank[2] = 1
    
    for idx in range(4, len(res_bank) + 1):
        if idx % 2 == 0:
            res_bank[idx] = res_bank[idx // 2] + 1
            res_bank[idx - 1] = res_bank[idx] + 1
    return abs(res_bank[target] - res_bank[start_value])


def broken_calc_2(start_value: int, target: int) -> int:
    operations = 0
    
    while start_value < target:
        operations += 1
        if target % 2 == 1:
            target += 1
        else:
            target //= 2
    return operations + start_value - target


if __name__ == '__main__':
    TestCase = namedtuple('TestCase', ('start_value', 'target', 'expect'))
    cases = [
        TestCase(start_value=2, target=3, expect=2),
        TestCase(start_value=5, target=8, expect=2),
        TestCase(start_value=3, target=10, expect=3),
        TestCase(start_value=1024, target=1, expect=1023),
        TestCase(start_value=1, target=10 ** 6, expect=28),
    ]
    
    for testcase in cases:
        print(broken_calc_2(testcase.start_value, testcase.target) == testcase.expect)
    
    print(broken_calc(1, 10 ** 6))
