#병합정렬
A=[int(a) for a in input().split()]
B=[int(b) for b in input().split()]
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

sorted_A,sorted_B = merge_sort(A),merge_sort(B)
answer=0
for i in range(3):
    answer+=sorted_A[i]*sorted_B[i]
print(answer)
