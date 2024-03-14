// 12947 lv1 하샤드 수
function solution(x) {
  let arr = String(x).split("");
  let xSum = 0;
  for (let i = 0; i < arr.length; i++) {
    xSum += Number(arr[i]);
  }
  if (x % xSum === 0) {
    return true;
  }

  return false;
}

// 다른 사람 풀이
function solution(x) {
  var a = 0;
  var s = (x + "").split("").map(Number);

  for (let i of s) {
    a += i;
  }

  return x % a == 0 ? true : false;
}
