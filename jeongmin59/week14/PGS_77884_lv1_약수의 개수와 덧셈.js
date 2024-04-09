// 77884 lv1 약수의 개수와 덧셈
function solution(left, right) {
  var answer = 0;

  for (let i = left; i <= right; i++) {
    let arr = [];
    for (let j = 1; j <= i; j++) {
      if (i % j === 0) {
        arr.push(j);
      }
    }
    if (arr.length % 2 === 0) {
      answer += i;
      // console.log(i);
    } else {
      answer -= i;
    }
  }

  return answer;
}

// 다른 사람의 풀이
function solution(left, right) {
  var answer = 0;
  for (let i = left; i <= right; i++) {
    if (Number.isInteger(Math.sqrt(i))) {
      answer -= i;
    } else {
      answer += i;
    }
  }
  return answer;
}

// 속도 차이가 매우 큼...
// 제곱근이 정수면 약수의 개수가 홀수다...
