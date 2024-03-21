// 86051 lv1 없는 숫자 더하기
function solution(numbers) {
  let answer = 0;
  var sortedNum = numbers.sort(); // 굳이 정렬 안해도 됐었음
  // console.log(sortedNum);
  for (let i = 0; i <= 9; i++) {
    if (!sortedNum.includes(i)) {
      // 배열이 특정값을 포함하고 있는지 여부를 boolean으로 반환
      answer += i;
    }
  }
  return answer;
}

// 다른 사람의 풀이
function solution(numbers) {
  return 45 - numbers.reduce((acc, cur) => acc + cur, 0);
}
// 전체 합 45와 reduce 활용
// 위 식은 배열의 합을 구해서 전체합인 45에서 뺄셈을 함...
