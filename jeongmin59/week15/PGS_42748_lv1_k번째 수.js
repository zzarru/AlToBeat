// 42748 lv1 k번째 수
function solution(array, commands) {
  var answer = [];

  for (let i = 0; i < commands.length; i++) {
    const start = commands[i][0] - 1;
    const end = commands[i][1];
    const idx = commands[i][2] - 1;

    let sortedArr = array.slice(start, end).sort((a, b) => a - b);

    answer.push(sortedArr[idx]);
  }

  return answer;
}

// 다른 사람 풀이
function solution(array, commands) {
  return commands.map((command) => {
    const [sPosition, ePosition, position] = command; // 구조 분해 할당이라고 함
    const newArray = array
      .filter((value, fIndex) => fIndex >= sPosition - 1 && fIndex <= ePosition - 1)
      .sort((a, b) => a - b);

    return newArray[position - 1]; // fillter가 새로운 배열을 return 하기 때문에 newArray 사용
  });
}
