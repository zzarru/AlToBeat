// 12969 lv1 직사각형 별찍기
process.stdin.setEncoding("utf8");
process.stdin.on("data", (data) => {
  const n = data.split(" ");
  const a = Number(n[0]),
    b = Number(n[1]);
  let star = "";

  for (let i = 0; i < b; i++) {
    for (let j = 0; j < a; j++) {
      star += "*";
    }
    star += "\n";
  }
  console.log(star);
});

// 다른 사람 풀이
process.stdin.setEncoding("utf8");
process.stdin.on("data", (data) => {
  const n = data.split(" ");
  const a = Number(n[0]),
    b = Number(n[1]);

  const row = "*".repeat(a); // repeat 메소드 사용
  for (let i = 0; i < b; i++) {
    console.log(row);
  }
});

// repeat 메소드는 문자열을 주어진 횟수만큼 반복해서 붙인 새로운 문자열을 반환함
