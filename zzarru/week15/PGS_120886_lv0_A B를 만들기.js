function solution(before, after) {
    const before_arr = Array.from(before).sort()
    const after_arr = Array.from(after).sort()
    for(i =0; i < before_arr.length; i++){
        if(before_arr[i] != after_arr[i]){
            return 0
        }
    }
    return 1;
}