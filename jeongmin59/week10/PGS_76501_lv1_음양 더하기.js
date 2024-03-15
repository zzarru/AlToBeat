// 76501 lv1 음양 더하기
function solution(absolutes, signs) {
  var negative = 0;
  var positive = 0;

  for (let i = 0; i < absolutes.length; i++) {
    if (signs[i] == false) {
      negative += absolutes[i] * -1;
      // console.log(negative)
    } else {
      positive += absolutes[i] * 1;
      // console.log(positive)
    }
  }

  return negative + positive;
}

// 다른 사람의 풀이
function solution(absolutes, signs) {
  return absolutes.reduce((acc, val, i) => acc + val * (signs[i] ? 1 : -1), 0);
}

// reduce 메소드 형태
// 배열.reduce((누적값, 현재값, 인덱스, 요소), 초기값);
// 배열을 순회하면서 콜백 함수 실행 -> 콜백 함수 반환 값을 누적시킴 -> 순회 완료시 최종 값 반환
