test_list = [1, 2, 3, 7, 4, 6, 5]

test_list.sort()
print(test_list)

scores = [('eng', 88), ('sci', 90), ('math', 80)]
# 정렬

def check(x):
    return x[1]

scores.sort(key=lambda x:x[1])
print(scores)