function solution(array, n) {
    array.sort(function (a, b) {
        return a - b;
    });
    var answer = 0;
    var min = 100
    for (number of array){
        const sub = Math.abs(n-number)
        if (sub < min){
            min = sub
            answer = number
        }
    }
    return answer;
}