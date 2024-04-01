// for 문을 이용하여 짝수인지 검사하고 짝수라면 더해준다.

function solution(n) {
    var number;
    var even = 0;
    for (number = 1; number < n+1; number ++){
        if(number % 2 === 0){
            even += number
        }
    }
    return even;
}