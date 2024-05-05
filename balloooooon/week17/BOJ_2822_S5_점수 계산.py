scores = []

for i in range(1,9):
    scores.append((int(input()),i))

scores.sort(key = lambda x: -x[0])
scores = scores[:5]
scores.sort(key = lambda x: x[1])

score_sum = 0
num_list = []
for score, problem_number in scores:
    score_sum += score
    num_list.append(problem_number)

print(score_sum)
print(*num_list)