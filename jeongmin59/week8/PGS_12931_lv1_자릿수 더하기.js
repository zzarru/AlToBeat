// lv1_자릿수 더하기
function solution(n) {
  var answer = 0;
  var nums = n.toString();

  for (i = 0; i < nums.length; i++) {
    answer += Number(nums[i]);
  }

  return answer;
}

// 다른 사람 풀이
function solution(n) {
  // n +"" 로 암묵적 형 변환 다음에 split 함
  // reduce는 처음 알게 됨
  return (n + "").split("").reduce((acc, curr) => acc + parseInt(curr), 0);
}

// 다른 사람 풀이 2
function solution(n) {
  var a = (n + "").split(""); // toString 사용 안 함
  var b = 0;
  for (var i = 0; i < a.length; ++i) {
    b += parseInt(a[i]);
  }
  return b;
}
