function solution(n) {
    var answer = 0;
    for (i = 1; i <= n; i ++){
        var remains = n % i
        if (remains == 0){answer += i}
    }
    return answer;
}