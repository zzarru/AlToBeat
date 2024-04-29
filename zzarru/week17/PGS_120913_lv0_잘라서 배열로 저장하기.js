function solution(my_str, n) {
    var answer = [];
    var len = my_str.length;

    for (var i = 0; i < len; i += n) {
        var letter = my_str.slice(i, i + n);
        answer.push(letter);
    }

    return answer;
}