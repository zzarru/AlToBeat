function solution(spell, dic) {
    spell.sort()
    for (letter of dic){
        var letters = []
        for (l of letter){
            letters.push(l)
        }
        letters.sort()
        console.log(letters, spell)
        if(letters.join('') == spell.join('')){
            return 1
            break
        }else{
            continue
        }
    }

    return 2;
}