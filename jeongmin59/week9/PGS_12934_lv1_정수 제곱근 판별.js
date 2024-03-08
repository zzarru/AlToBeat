// 12934 lv1 정수 제곱근 판별
function solution(n) {
  var answer = 0;
  answer = Math.sqrt(n); // 제곱근 반환
  // console.log(answer);
  if (Number.isInteger(answer)) {
    // 정수인지 실수인지 체크
    return (answer + 1) ** 2;
  }

  return -1;
}

// 다른 사람의 풀이
function solution(n) {
  switch (n % Math.sqrt(n)) {
    case 0:
      return Math.pow(Math.sqrt(n) + 1, 2);
    default:
      return -1;
  }
}
// switch case를 사용하는 게 내가 짠 코드보다 시간이 더 빠름
