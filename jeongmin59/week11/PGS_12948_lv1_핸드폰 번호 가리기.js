// 12948 lv1 핸드폰 번호 가리기
function solution(phone_number) {
  var answer = "";
  var sliced = phone_number.slice(phone_number.length - 4, phone_number.length);
  for (let i = 0; i < phone_number.length - 4; i++) {
    answer += "*";
  }
  answer += sliced;
  console.log(answer);
  return answer;
}

// 다른 사람의 풀이
function solution(phone_number) {
  return phone_number.replace(/\d(?=\d{4})/g, "*");
}
// replace : 문자열 치환 함수

function solution(phone_number) {
  var result = "*".repeat(phone_number.length - 4) + phone_number.slice(-4);
  return result;
}
// repeat : 반복 후 새로운 문자열로 반환
