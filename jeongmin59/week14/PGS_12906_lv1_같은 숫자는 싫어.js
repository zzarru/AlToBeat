// 12906 lv1 같은 숫자는 싫어
function solution(arr) {
  var answer = [];
  for (let i = 0; i < arr.length; i++) {
    if (answer.length === 0) {
      answer.push(arr[i]);
    } else {
      if (answer[answer.length - 1] !== arr[i]) {
        answer.push(arr[i]);
      }
    }
  }

  return answer;
}

// 다른 사람의 풀이
function solution(arr) {
  return arr.filter((val, index) => val != arr[index + 1]);
}

// 마지막은 인덱스로 참조할 요소가 없어서, undefined가 뜨기 때문에 이 값이랑 비교한다고 함...
// 문제 분류가 스택/큐로 되어 있어서 스택 방식으로 풀었지만 filter에 익숙하지 않아서 해당 방법이 생각나지 않았던 거 같음
