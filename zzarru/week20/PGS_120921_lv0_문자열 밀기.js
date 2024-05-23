function solution(A, B) {
    //문자열을 리스트로 변환하여 저장
    var letters = []
    for(a of A){
        letters.push(a)
    }
    // 문자열의 길이만큼 반복한다.
    var leng = letters.length

    // 바꾼 횟수 저장
    var cnt = 0;


    for (i=0; i < leng; i ++){
        var AA = letters.join('') //리스트를 문자열로 변환
        if (AA == B){
            // 만약 바꾼 문자열이 B와 같다면 cnt 출력하고 break
            return cnt
            break
        } else{
            // 같지 않다면 맨 뒤의 원소 빼서 맨 앞에 넣는다.
            var letter = letters.pop()
            letters.unshift(letter)
            cnt ++
            continue
        }
    }
    return -1 // 모든 과정을 반복해도 같아질 수 없는 경우
}