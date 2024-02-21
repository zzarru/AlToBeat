// lv1_짝수와 홀수

function solution(num) {
  var answer = '';
  if (num % 2 === 0) {
      answer = "Even";
  } else {
      answer = "Odd";
  }

  return answer;
}

// 다른 사람 풀이
function solution(num) {
  return num % 2 ? "Odd" : "Even"
}
// 삼항 연산자 사용함