// 12910 lv1 나누어 떨어지는 숫자 배열
function solution(arr, divisor) {
  var answer = [];

  for (i = 0; i < arr.length; i++) {
    if (arr[i] % divisor === 0) {
      answer.push(arr[i]);
    }
  }
  // console.log(answer);
  if (answer.length >= 1) {
    return answer.sort((a, b) => a - b); // 오름차순으로 만드는 방법
  } else {
    answer.push(-1);
    return answer;
  }
}

// arr.sort((a, b) => a - b); 를 해야 하는 이유
// 답 중에 그냥 sort()만 했을 때 답이 [10, 5]로 나왔었음
// 숫자로 이루어진 배열을 정렬하기 위해서는 (a, b) => a - b 를 넣어줘야 함

// 다른 사람 풀이
function solution(arr, divisor) {
  var answer = arr.filter((v) => v % divisor == 0);
  return answer.length == 0 ? [-1] : answer.sort((a, b) => a - b);
}

// filter랑 삼항 연산자의 콜라보...
// filter를 통해 배열을 순회하면서 필터링 할 수 있음...
// 위 풀이가 내 답보다 시간이 훨씬 빠름
