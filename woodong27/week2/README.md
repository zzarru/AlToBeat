# Week2(입출력)

## Python에서 input()과 sys.stdin.readline()의 차이

- input()

  - 사용자가 키를 누르면 대응하는 데이터가 하나씩 버퍼에 입력된다.
  - 개행문자(enter == '\n')는 입력의 종료로 간주한다.
  - 입력이 끝나면 개행문자를 제거하고 문자열로 변경하여 반환한다.

- sys.stdin.readline()

  - 한 줄을 모두 읽어와서 버퍼에 저장한다.
  - 한 번 누를 때마다 데이터를 버퍼에 저장하는 input()보다 빠르다.
  - 입력이 많아질 수록 input()과의 차이가 더 커진다.
  - 대신 입력의 끝에 개행문자('\n')도 같이 입력받아져서, 문자나 문자열을 입력받을 때는 rstrip() 또는 strip()으로 개행문자를 제거해야한다.

<br>

- E.g : 백준 15552(빠른 A+B) - input()을 사용하면 시간초과 발생

---

## Python의 다양한 출력 방법

- f-string

  문자열과 다른 타입의 데이터를 동시에 사용할 때 편리하게 쓸수 있는 방법

  ```python
  time = 6

  print(f'내일 오후{time}시에 팀 회식이 예정되어 있습니다.....')
  # 출력 : 내일 오후 6시에 팀 회식이 예정되어 있습니다.

  # f-string을 쓰지 않을 경우
  print('내일 오후 ', time, '시에 팀 회식이 예정되어 있습니다.....', sep='')
  ```

- print의 sep 옵션

  동시에 여러 데이터를 출력할 때 해당 데이터들 사이에 올 구분자를 설정할 수 있음

  ```python
  a = 1
  b = 2
  c = 3

  print(a, b, c)
  # 출력 : 1 2 3

  print(a, b, c, sep='')
  # 출력 : 123

  print(a, b, c, sep='ㅋ')
  # 출력 : 1ㅋ2ㅋ3
  ```

- list(컨테이너 자료형) 출력 방법들

  - \*(aesterisk)기호를 사용해서 시퀀스형 자료의 packing/unpacking이 가능하다.
  - end 옵션으로 print 문을 이용해 출력을 완료한 뒤의 내용을 수정할 수 있다. 기본 값으로는 개행('\n')이 들어가있다.

  ```python
  numbers = [1, 2, 3, 4, 5]

  print(numbers)
  # 출력 : [1, 2, 3, 4, 5]

  for number in numbers:
    print(number)
  # 출력 :
  # 1
  # 2
  # 3
  # 4
  # 5

  for number in numbers:
    print(number, end=' ')
  # 출력 : 1 2 3 4 5
  # 대신 이 경우에는 뒤에 다른 print문이 있다면 5 뒤에 붙어서 출력된다.

  # e.g : 반복문이 끝나고 print('끝!')이 있는 경우
  for number in numbers:
    print(number, end=' ')
  print('끝!')
  # 출력 : 1 2 3 4 5 끝!
  # 그렇기 때문에 조건문으로 마지막 출력에는 end가 없게 하거나,
  # 그냥 *을 써서 unpacking 해주도록 하자

  print(*numbers)
  # 출력 : 1 2 3 4 5

  # 응용
  print(*numbers, sep='')
  # 출력 : 12345
  ```

---
