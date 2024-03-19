// 12943 lv1 콜라츠 추측
function solution(num) {
  var ans = 0;

  function calc(num) {
    while (num !== 1) {
      num = num % 2 === 0 ? num / 2 : num * 3 + 1;
      ans += 1;
    }
  }
  if (num !== 1) {
    calc(num); // 재귀
    if (ans > 500) {
      return -1;
    }
    return ans;
  } else {
    return 0;
  }
}

// 다른 사람의 풀이
function solution(num) {
  var count = 0;

  while (count < 500) {
    // 그냥 while문을 써도 됐었네...
    if (num === 1) {
      return count;
    }
    count++; // += 뿐만 아니라 ++도 있었음
    num = num % 2 === 0 ? num / 2 : num * 3 + 1;
  }

  return -1;
}
