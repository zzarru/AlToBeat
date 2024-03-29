// 70128 lv1 내적
function solution(a, b) {
  const n = a.length;
  var answer = 0;
  for (i = 0; i < n; i++) {
    answer += a[i] * b[i];
  }

  return answer;
}

// 다른 사람의 풀이
function solution(a, b) {
  return a.reduce((acc, _, i) => (acc += a[i] * b[i]), 0);
}

// array.reduce(callback[, initialValue])
// callback 함수는 다음의 매개변수를 가짐
// accumulator : 콜백 함수의 반환 값
// currentValue : 현재 순회 중인 배열 요소
// currentIndex(옵션) : 현재 순회 중인 배열 요소의 인덱스
// array(옵션) : reduce 함수가 호출된 배열

// 자세한 정리는 블로그로 작성 예정
