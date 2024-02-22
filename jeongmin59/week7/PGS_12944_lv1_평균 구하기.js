// 12944_평균 구하기
function solution(arr) {
  var answer = 0;
  let sum = 0;
  
  for (let i=0; i < arr.length; i++){
      sum += arr[i]
  }
  
  return answer = sum / arr.length;;
}

// 다른 사람 풀이
function average(array){
  return array.reduce((a,b) => a+b) / array.length;
}

// 생각해내지 못 했던 것 reduce 라는 메소드
// 생각보다 다양한 메소드가 있었다는 걸 까먹고 있었음