// lv1_나머지가 1이 되는 수 찾기

function solution(n) {
  var x = 1;
  while (true) {
      if (n % x === 1) {
          return x;
      } else {
          x++;
      }
  }
}

// 다른 사람 풀이
function solution(n, x = 1) {    
    while (x++) {       // 증감 연산자 사용 while에서 사용 가능
        if (n % x === 1) {
            return x;
        }
    }    
}


// for문
const solution = function(n) {
    for (let i=0; i<n; i++){
        if (n%i == 1){
            return i
        }
    }
}