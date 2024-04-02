// 82612 lv1 부족한 금액 계산하기
function solution(price, money, count) {
  var answer = 0;
  let charge = 0;
  for (let i = 1; i <= count; i++) {
    charge += price * i;
  }
  if (charge > money) {
    return Math.abs(charge - money); // 절댓값 반환
  } else {
    return answer;
  }
}

// 위의 식을 깔끔하게 정리한다면
function solution(price, money, count) {
  let answer = 0;

  for (let i = 1; i <= count; i++) {
    answer += price * i;
  }

  return answer > money ? answer - money : 0;
}
