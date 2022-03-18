from typing import List


def remove_element(nums: List[int], val: int) -> int:
    pointer, border = 0, len(nums) - 1
    while pointer <= border:
        if nums[pointer] == val:
            for i in range(pointer, border):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            border -= 1
            continue
        pointer += 1
    
    return pointer


if __name__ == '__main__':
    arr = [3, 2, 2, 3]
    res = remove_element(arr, 3)
    print(res)
    print(arr)
    arr = [0, 1, 2, 2, 3, 0, 4, 2]
    res = remove_element(arr, 2)
    print(res)
    print(arr)
    arr = [2]
    res = remove_element(arr, 3)
    print(res)
    print(arr)
    arr = [4, 5]
    res = remove_element(arr, 4)
    print(res)
    print(arr)