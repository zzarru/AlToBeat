// lv0_머쓱이보다 키 큰 사람

function solution(array, height) {
  var answer = 0;
  
  for (let i = 0; i < array.length; i++) {
      if(array[i] > height) {
          answer += 1;
      }
  }
  return answer;
}


// 다른 사람 풀이

function solution(array, height) {
    var answer = array.filter(item => item > height);
    return answer.length;
}

// 자바스크립트에 대해 무지함을 깨닫게 됨
// 파이썬으로 푸는 방식이 익숙했네요...