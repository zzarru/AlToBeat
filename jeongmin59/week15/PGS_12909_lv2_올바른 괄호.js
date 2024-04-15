// 12909 lv2 올바른 괄호
function solution(s) {
  let cnt = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      cnt += 1;
    } else {
      cnt -= 1;
    }

    if (cnt < 0) {
      return false;
    }
  }

  return cnt ? false : true;
}

// console.log(solution("())((()))(()"));
// 오랜만에 괄호 관련...
