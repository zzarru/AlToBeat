# BOJ 9536 S3 여우는 어떻게 울지?

"""
파이썬의 리스트 remove메서드는
argument와 동일한 객체 하나만을 제거하기 때문에
list comprehension을 사용해서 중복되는 값들을 모두 제거한
리스트를 반환받을 수 있게 하였다.
"""

t = int(input())

# while 반복문을 끝내는 마지막 input과 비교할 문장
end_sentence = 'what does the fox say?'

start_flag = 0
animal_sound = []
for _ in range(t):
    while True:
        sentence = input()
        # 현재 입력이 end와 같으면 반복문 중지
        if sentence == end_sentence:
            start_flag = 0
            break

        # 첫번째로 받는건 동물들의 울음소리가 합쳐진 문장
        if not start_flag:
            animal_sound = list(sentence.split())
            start_flag = 1
        # 두번째부터는 각 동물들의 울슴소리를 설명하는 문장
        else:
            animal, goes, word = map(str, sentence.split())
            # 첫번째로 받은 울음소리가 섞인 문장에서 각 동물들의 울음소리를 제거한다.
            animal_sound = [sound for sound in animal_sound if sound != word]

    print(' '.join(animal_sound))
    animal_sound = []
