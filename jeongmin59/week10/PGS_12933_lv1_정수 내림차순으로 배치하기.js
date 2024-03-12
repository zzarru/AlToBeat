// 12933 lv1 정수 내림차순으로 배치하기

function solution(n) {
  arr = n.toString().split("");
  let sorted = arr.sort().reverse();
  answer = Number(sorted.join(""));
  return answer;
}

// 다른 사람 풀이
function solution(n) {
  var nums = [];
  do {
    nums.push(n % 10);
    n = Math.floor(n / 10);
  } while (n > 0);

  return nums.sort((a, b) => b - a).join("") * 1;
  //문자는 느림
  return (
    (n + "")
      .split("")
      .sort((a, b) => b - a)
      .join("") * 1
  );
}
