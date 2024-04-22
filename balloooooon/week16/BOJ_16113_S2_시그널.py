'''
나는 숫자 사이에 나오는 공백을 기준으로 check라는 글자를 판독하는 함수로 숫자를 검사했다.
공백이후 어떤 글자가 나오면 5행 3열을 판독한다
판독중 중복판독을 막기위해 판독이후에는 방문배열에 방문함을 새겨뒀다.
1의 경우가 가장 걸림돌인데 만일 마지막 수가 1일때 check함수에선 second와 third는 오류가 나게된다.
어차피 마지막 수이기 때문에 예외처리해주고 답에 1을 추가해주면 돈다.
'''

N = int(input()) // 5
num_list = list(input())
visited = [0 for i in range(N)]
answer = []
def check(i):
    try:
        first = [password[0][i], password[1][i], password[2][i], password[3][i], password[4][i]]
        second = [password[0][i+1], password[1][i+1], password[2][i+1], password[3][i+1], password[4][i+1]]
        third = [password[0][i+2], password[1][i+2], password[2][i+2], password[3][i+2], password[4][i+2]]

        if first == ['#', '#', '#', '#', '#']:
            if second == ['#','.','.','.','#']:
                answer.append(0)
            elif second == ['#','.','#','.','#']and third == ['#','#','#','#','#']:
                answer.append(8)
            elif second == ['#','.','#','.','#'] and third == ['#','.','#','#','#']:
                answer.append(6)
            else:
                answer.append(1)
                visited[i] = 1
                return
        elif first == ['#','.','#','#','#']:
            answer.append(2)
        elif first == ['#','.','#','.','#']:
            answer.append(3)
        elif first == ['#','#','#','.','.']:
            answer.append(4)
        elif first == ['#','.','.','.','.']:
            answer.append(7)
        elif third == ['#','#','#','#','#']:
            answer.append(9)
        else:
            answer.append(5)

        visited[i] = 1
        visited[i+1] = 1
        visited[i+2] = 1
    except:
        answer.append(1)
        return

password = []
for i in range(5):
    password.append(num_list[N*i:N*(i+1)])

i=0

while 1:
    if i < N:
        pass
    else:
        break

    if [password[0][i], password[1][i], password[2][i], password[3][i], password[4][i]] == ['.','.','.','.','.']:
        pass
    else:
        if not visited[i]:
            check(i)
    i += 1

print(*answer, sep='')
