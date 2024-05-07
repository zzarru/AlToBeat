function solution(emergency) {
    var answer = [];
    var idx = 0;
    for (number of emergency){
        answer.push([number, idx])
        idx += 1
    }
    answer.sort(function(a, b) {
        return b[0] - a[0];
    });

    var new_answer = []
    var new_idx = 1;
    for (ans of answer){
        new_answer.push([new_idx, ans[1]])
        new_idx ++
    }
    new_answer.sort(function(a, b) {
        return a[1] - b[1];
    });

    var result = []
    for (rst of new_answer){
        result.push(rst[0])
    }
    return result;
}