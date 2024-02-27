// lv1_문자열을 정수로 바꾸기

function solution(s) {
  var answer = 0;
  answer = Number(s);
  return answer;
}

// 다른 사람 풀이
function solution(s) {
  return s / 1;
}

// 암묵적 형 변환을 활용함
// 문자열에서 연산을 해줌으로 인해 숫자로 형변환 시켜버림
