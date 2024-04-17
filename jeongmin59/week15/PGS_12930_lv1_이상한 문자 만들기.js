// 12930 lv1 이상한 문자 만들기
function solution(s) {
  var answer = "";
  let str = s.split(" ");
  console.log(str);

  for (let i = 0; i < str.length; i++) {
    for (let j = 0; j < str[i].length; j++) {
      if (j % 2 == 0) {
        answer += str[i][j].toUpperCase();
      } else {
        answer += str[i][j].toLowerCase();
      }
    }
    if (i < str.length - 1) {
      answer += " ";
    }
  }

  return answer;
}

// 다른 사람 풀이
function solution(s) {
  return s
    .split(" ")
    .map((i) =>
      i
        .split("")
        .map((j, key) => (key % 2 === 0 ? j.toUpperCase() : j.toLowerCase()))
        .join("")
    )
    .join(" ");
}

// 내가 짠 코드보다 훨씬 빠름....
// 중첩된 반복문 대신 내장 함수 사용해서 더 빠름
// map(), join()에 대해 추후 정리해보기
