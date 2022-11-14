var lines = ['[',
'    {',
'        company_name: (BlackRock(',
'        ticker : (BLK{',
'        stock_price: {',
'        2022-04-03: (930]',
'        2022-04-02: (932}',
'        }',
'    }',
']'
]

let check = [ '[', ']', '{', '}', '(', ')']
let check2 = [  '}', '(', ')']


for (var i= 0; i<lines.length; i++) {
    let line = lines[i].trim();
    console.log("===", line[line.length-1])



    if (line.length === 1 && check.includes(line[line.length-1])) {
       
    } else {
        console.log("========222", line)
    }
    if (line.length === 1 && !check.includes(line[line.length-1]) && i < lines.length-1) {
        line += ','
    }

    if (line[line.length-1] === '}') {
        line+= ','
    }
}
console.log(lines)
try {
    JSON.parse(lines)
    console.log("valid")
} catch {
    console.log("invalid")
}


// if (!check.includes(line[line.length-1])) {
//     line += ','
// }
