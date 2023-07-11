# Intersect Sorted Arrays
def intersect_sorted_arrays1(list1, list2):
    answer = []
    for i in list1:
        if i in list2 and answer.count(i) < min(list1.count(i), list2.count(i)):
            answer.append(i)
    return answer

list1 = [1,2,2,2,7]
list2 = [2,2,6,6,7]

print(intersect_sorted_arrays1(list1, list2))

# Intersect Sorted Arrays (dedupe)
def intersect_sorted_arrays2(list1, list2):
    answer = []
    for i in list1:
        if i in list2 and i not in answer:
            answer.append(i)
    return answer


list1 = [1,2,2,2,7]
list2 = [2,2,6,6,7]

# print(intersect_sorted_arrays2(list1, list2))