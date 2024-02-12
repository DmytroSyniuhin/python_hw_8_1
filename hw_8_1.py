def add_one(some_list):
    num_ = 0
    count = 1

    for i in range(len(some_list)):
        num_ += some_list.pop(-1) * count
        count *= 10

    num_ += 1

    while num_ > 0:
        some_list.insert(0, num_ % 10)
        num_ = num_ // 10
    return some_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
