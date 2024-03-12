// 12933 lv1 정수 내림차순으로 배치하기

function solution(n) {
  arr = n.toString().split("");
  let sorted = arr.sort().reverse();
  answer = Number(sorted.join(""));
  return answer;
}

// 다른 사람 풀이
// 숫자로 푸는 게 더 빠르다고 함
function solution(n) {
  var nums = [];
  do {
    nums.push(n % 10);
    n = Math.floor(n / 10);
  } while (n > 0);

  return nums.sort((a, b) => b - a).join("") * 1;
  //문자로 푸는 방법
  return (
    (n + "")
      .split("")
      .sort((a, b) => b - a)
      .join("") * 1 // 형 변환
  );
}
