function solution(i, j, k) {
    var answer = 0;
    for (x = i; x <= j; x ++){
        x_str = x.toString()
        for (str of x_str){
            if (str == k.toString()){
                answer ++
            }
        }
    }
    return answer;
}