// 12939 lv2 최댓값과 최솟값
function solution(s) {
  arr = s.split(" ");

  let minV = Math.min(...arr); // 문자열도 가능
  let maxV = Math.max(...arr);

  let answer = `${minV} ${maxV}`;
  return answer;
}

// 다른 사람 풀이
function solution(s) {
  const arr = s.split(" ");

  return Math.min(...arr) + " " + Math.max(...arr); // 이렇게 한 줄로도 작성 가능
}
