//  12922 lv1 수박수박수박수박수박수?
function solution(n) {
  var answer = "";
  for (i = 0; i < n; i++) {
    add = i % 2 === 0 ? "수" : "박";
    answer += add;
  }
  return answer;
}

// 조금 바꿔본다면
function solution(n) {
  var answer = "";
  for (i = 0; i < n; i++) {
    i % 2 === 0 ? (answer += "수") : (answer += "박");
  }
  return answer;
}
