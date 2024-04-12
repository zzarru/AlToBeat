function solution(rsp) {
    var answer = '';
    for (i=0; i < rsp.length; i++){
        const letter = rsp[i];
        if(letter == '0'){
            answer += '5'
        } else if (letter == '2'){
            answer += '0'
        } else {
            answer += '2'
        }
    };
    return answer;
}