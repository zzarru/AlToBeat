// 12919 lv1 서울에서 김서방 찾기
function solution(seoul) {
  var answer = 0;
  for (var i = 0; i < seoul.length; i++) {
    if (seoul[i] === "Kim") {
      answer = i;
      break;
    }
  }
  return `김서방은 ${answer}에 있다`;
}

// 다른 사람의 풀이
function solution(seoul) {
  return `김서방은 ${seoul.indexOf("Kim")}에 있다`;
}

// indexOf 라는 메소드를 알게 됨
// arr.indexOf(item, from)
// from부터 시작해 item(요소)을 찾을 수 있음
