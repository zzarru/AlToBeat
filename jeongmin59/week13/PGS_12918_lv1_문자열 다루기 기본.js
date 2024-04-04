// 12918 lv1 문자열 다루기 기본
function solution(s) {
  if (s.length === 4 || s.length === 6) {
    for (let i = 0; i < s.length; i++) {
      if (Number.isNaN(parseInt(s[i]))) {
        console.log(parseInt(s[i]));
        return false;
      }
    }
    return true;
  }
  return false;
}
// console.log(!Number.isNaN("3e10"));

// 이 문제에 대해서는 지수 표기법으로 숫자로 변하는 것들을 조심해야 했음
// 지수 표기법으로 숫자로 변하는 것들도 다 false 처리 해야 통과 가능
// 정규표현식을 사용하는 방법 있지만, 외우지 않는 한 반례를 생각해서 예외 처리하는 게 중요하다고 느낌
