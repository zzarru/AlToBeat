'''
1,3,6,7,10의 경우 각 숫자의 차이가 2,3,1,3으로 구성된다
만일 그룹을 시킨다면 1,3,6의 그룹은 1과3의 차이 3과6의 차이를 합하면
1과6의 차이를 구할 수 있다. 어떠한 숫자차이를 빼주면 그걸 기점으로
그룹화 시켜줄 수 있다.
예를들어 2,3,1,3에서 두번째 3은 3,6의 차이이고 이를 삭제시키면
1,3 /6,7,10으로 그룹핑가능 그리고 남은 각자의 차이를 더해주면
두 그룹의 비용을 확인 할 수 있다.
'''

n, k = map(int,input().split())
student=list(map(int,input().split()))
fee=[]
for i in range(n-1):
    fee.append(student[i+1]-student[i])
fee.sort()
answer=sum(fee[:n-k])
print(answer)