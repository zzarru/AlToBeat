// 12950 lv1 행렬의 덧셈
function solution(arr1, arr2) {
  let answer = [];

  for (let i = 0; i < arr1.length; i++) {
    answer[i] = [];
    for (let j = 0; j < arr2[i].length; j++) {
      answer[i][j] = arr1[i][j] + arr2[i][j];
    }
  }

  return answer;
}

// 중간에 answer[i] = []; 해야 하는 이유
// answer라는 배열의 각 행에 빈 배열을 할당하기 위해서! 안 해주면 길이가 1인 배열에서 에러 발생
