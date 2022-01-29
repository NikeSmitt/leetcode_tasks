"""You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version
of your product fails the quality check. Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find
the first bad version. You should minimize the number of calls to the API.


1 <= bad <= n <= 2 ** 31 - 1
"""

import unittest


def first_bad_version(n: int, isBadVersion=None):
    if n == 1 or isBadVersion(1):
        return 1

    left, right = -1, n

    while right - left > 1:
        middle = (right + left)


# class TestFirstBadVersion(unittest.TestCase):
#
#     def test_first_bad_version(self):
#         self.assertEqual(first_bad_version(1), 1, 'Bad first version error')
#
#     def test_all_bad_version(self):
#         versions = [True] * 10
#
#     def test_all_bad(self):
#         versions = [True] * 10


def test_search(n, versions):
    left, right = 0, n

    while right - left > 1:
        middle = left + (right - left) // 2
        if versions[middle]:
            right = middle
        else:
            left = middle

    return right


if __name__ == '__main__':
    # unittest.main()
    v = [False, False, False, True]
    print(test_search(3, v))

    v = [True] * 10
    print(test_search(3, v))

    v = [False] * 10 + [True] * 2
    print(test_search(11, v))

