// 12903 lv1 가운데 글자 가져오기
function solution(s) {
  var answer = "";
  var idx = 0;
  if (s.length % 2 === 1) {
    idx = s.length / 2 - 0.5;
    // console.log(idx);
    answer = s[idx];
  } else {
    idx = s.length / 2;
    answer = s[idx - 1] + s[idx];
    // console.log(answer);
  }
  return answer;
}

// 다른 사람의 풀이
function solution(s) {
  const mid = Math.floor(s.length / 2);
  return s.length % 2 === 1 ? s[mid] : s[mid - 1] + s[mid];
}

// Math.floor은 내림을 해주는 메소드임
// 내가 풀었던 과정을 보다 더 빠르고 쉽게 푼 풀이임
