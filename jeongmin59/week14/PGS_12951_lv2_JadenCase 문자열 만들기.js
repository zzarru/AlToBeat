// 12951 lv2 JadenCase 문자열 만들기
function solution(s) {
  var answer = "";
  let isFirst = true; // 단어 첫 글자 확인

  for (let i = 0; i < s.length; i++) {
    // 단어의 첫 글자거나 공백이 아니면
    if (isFirst && s[i] !== " ") {
      answer += s[i].toUpperCase();
      isFirst = false;
    } else {
      answer += s[i].toLowerCase();
      if (s[i] === " ") isFirst = true; // 만약 공백이면 다음 글자가 단어의 첫 글자...
    }
  }

  return answer;
}

console.log(solution("  for the what 1what  "));
// '  For The What 1what  '

// 다른 사람의 풀이
function solution(s) {
  return s
    .split(" ")
    .map((v) => v.charAt(0).toUpperCase() + v.substring(1).toLowerCase())
    .join(" ");
}

// substring("시작 위치", "종료 위치") : 문자열 자르기
// charAt() :  문자열에서 지정된 위치에 존재하는 문자를 찾아서 반환
