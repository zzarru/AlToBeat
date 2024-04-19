function solution(n) {
    var factorial = 1;
    let i = 2
    while (factorial <= n){
        factorial = i*factorial

        i += 1
    }
    return i - 2
}