function solution(age) {
    var answer = ''
    const alpabets = 'abcdefghijklmnopqrstuvwxyz'
    const str_age = age.toString()
    for(i=0; i < str_age.length; i++){
        const idx = str_age[i]
        answer += alpabets[idx]
    }
    return answer
}