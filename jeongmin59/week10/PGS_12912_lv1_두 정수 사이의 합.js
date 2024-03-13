// 12912 lv1 두 정수 사이의 합
function solution(a, b) {
  let answer = 0;
  if (a === b) {
    return a;
  } else {
    for (let i = Math.min(a, b); i <= Math.max(a, b); i++) answer += i;
  }
  return answer;
}

// 다른 사람의 풀이
function solution(a, b) {
  if (a === b) return a;
  let small = a < b ? a : b; // 삼항연산자 쓸 수 있음
  let big = a > b ? a : b;
  for (let i = small + 1; i < big + 1; i++) small += i;
  return small;
}
