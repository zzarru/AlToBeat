// 12935 lv1 제일 작은 수 제거하기
function solution(arr) {
  var minValue = Math.min(...arr);
  if (arr.length === 1) {
    return [-1];
  } else {
    let filterd = arr.filter((element) => element !== minValue);
    console.log(minValue);
    return filterd;
  }
}

// 다른 사람의 풀이
function solution(arr) {
  const min = Math.min(...arr);
  return arr.length !== 1 ? arr.filter((i) => i !== min) : [-1];
}

// 위에서 내가 풀었던 코드를 단 2줄 만에 끝낸 코드다.
// 삼항 연산자, filter 다 알고 있었음에도 코드 줄?에 따라서 시간 차이가 꽤 나는 거 같음
// 내 코드는 평균 4~5초대인데, 위 코드는 평균 1초 정도 걸린 듯 함
// 좀만 더 생각해보는 연습을 해야겠다.
