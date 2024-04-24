'''
캣닢이 가장 장수하는 세계선을 찾아야한다.

문제에서 제시한 화분들의 상태는 모두 동일하게 시작한다.
일단 이문제는 캣닢이 죽지 않아야하므로 살날이 얼마남지 않은
캣닢에게는 지속적으로 수혈이 필요하다.
이 말은 정렬을 해서 계속해서 수분기가 적은 캣닢을 찾아야한다는 말이다.
하지만 물을 줄떄는 연속한 A개의 캣닢에 물을 준다.
가장 베스트 선택지는 수분기가 적은 캣닢에 연달아 물을 공급하는게 최선이다.

하지만 문제에서 제시한 화분들의 상태는 모두 동일하게 시작하므로
결국 어떤 세계선은 이러한 베스트 선택지를 연달아 선택하는 경우가 있다는것이다.
이해하기 조금 어렵지만 일단 내 생각은 그렇다.
'''


N, K, A, B = map(int,input().split())
answer = 0
catnips = [ K for _ in range(N)]

while not 0 in catnips:
    catnips.sort()
    for i in range(A):
        catnips[i] += B

    for i in range(N):
        catnips[i] -= 1
        if not catnips[i]:
            break
    answer += 1
print(answer)