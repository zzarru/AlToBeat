function solution(my_string) {
    var answer = [];
    const letters = Array.from(my_string)
    letters.forEach((letter) => {
        if(answer.includes(letter) == false) {
            answer.push(letter)
        }
    })
    return answer.join("");
}