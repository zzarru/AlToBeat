// 12932 자연수 뒤집어 배열로 만들기
function solution(n) {
  var answer = [];
  answer = String(n)
    .split("")
    .map((str) => Number(str))
    .reverse();
  return answer;
}

// 다른 사람 풀이
function solution(n) {
  // 문자풀이
  // return (n+"").split("").reverse().map(v => parseInt(v));

  // 숫자풀이
  var arr = [];

  do {
    arr.push(n % 10);
    n = Math.floor(n / 10);
  } while (n > 0);

  return arr;
}
