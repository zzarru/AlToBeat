// lv1_x만큼 간격이 있는 n개의 숫자
function solution(x, n) {
  var answer = [];

  for (i = 1; i < n + 1; i++) {
    num = x * i;
    answer.push(num);
  }

  return answer;
}

// 다른 사람 풀이
function solution(x, n) {
  return Array(n)
    .fill(x)
    .map((v, i) => (i + 1) * v);
}

// Array fill 학습하기
// for문을 벗어나야겠다고 다짐함...
