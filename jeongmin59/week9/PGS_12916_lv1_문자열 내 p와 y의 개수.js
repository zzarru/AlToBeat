// 12916 lv1 문자열 내 p와 y의 개수

function solution(s) {
  let arr = [...s];

  let p = arr.filter((value) => value === "p" || value === "P").length;
  let y = arr.filter((value) => value === "y" || value === "Y").length;

  if (p === y) {
    console.log(p, y);
    return true;
  } else {
    console.log(p, y);
    return false;
  }
}

// 다른 사람 풀이
function solution(s) {
  return s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length;
}
// 대문자로 바꾸고... 그거에 대한 길이로 판단...
