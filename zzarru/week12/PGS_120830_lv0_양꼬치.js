function solution(n, k) {
    const service = (n - n % 10) / 10; 
    var answer = (n*12000) + (k-service)*2000
    return answer;
}