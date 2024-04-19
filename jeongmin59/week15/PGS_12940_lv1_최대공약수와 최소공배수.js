// 12940 lv1 최대공약수와 최소공배수
function solution(n, m) {
  var answer = [];
  let gcd = 1; // 최대공약수
  for (let i = 1; i <= Math.min(n, m); i++) {
    if (n % i === 0 && m % i === 0) {
      gcd = i;
    }
  }
  let lcm = (n * m) / gcd; // 최소공배수는 두 수의 곱에서 최대공약수를 나눈 값
  answer.push(gcd, lcm);
  return answer;
}
