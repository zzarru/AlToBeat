function solution(array, n) {
    var cnt = 0;
    array.forEach((number)=> {
        if(number === n){
            cnt +=1
        }
    })
    return cnt;
}