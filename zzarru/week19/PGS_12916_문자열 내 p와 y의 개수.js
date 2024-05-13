function solution(s){
    var p_cnt = 0
    var y_cnt = 0
    var letters = s.toLowerCase()
    for(letter of letters){
        if (letter == 'p'){p_cnt ++} else if (letter == 'y'){y_cnt ++}
    }
    if(p_cnt == y_cnt){
        return true
    } else {
        return false
    }
}