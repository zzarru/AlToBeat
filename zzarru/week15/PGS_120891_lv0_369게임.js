function solution(order) {
    var answer = 0;
    const list = Array.from(order.toString())
    list.forEach((number) => {
        if (number == '3') {
            answer += 1
        } else if (number == '6') {
            answer +=1
        } else if (number == '9') {
            answer += 1}
        else {
        }
    })

    return answer;
}