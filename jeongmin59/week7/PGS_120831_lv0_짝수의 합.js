// lv0_짝수의 합

function solution(n) {
  let answer = 0;
  for (i = 0; i <= n; i++) {
      if (i % 2 === 0) {
          answer += i;
      }
  }
  return answer;
}

// 다른 사람 풀이 1
/*
function solution(n) {
    var answer = 0;

    for(let i=2 ; i<=n ; i+=2)
        answer += i;

    return answer;
}
/*

// 다른 사람 풀이 2
/*
function solution(n) {
    var half = Math.floor(n/2);   // 수열 공식 사용
    return half*(half+1);
}
*/
