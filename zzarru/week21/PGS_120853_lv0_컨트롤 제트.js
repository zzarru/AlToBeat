function solution(s) {
    var answer = 0;
    var number = 0;
    var commands = s.split(" ") // 공백을 기준으로 나누기
    for (cmd of commands){
        if(cmd == 'Z'){
            answer -= number
        }else{
            number = Number(cmd) //정수형으로 바꿔준다
            answer += Number(cmd)
        }
    }
    return answer;
}