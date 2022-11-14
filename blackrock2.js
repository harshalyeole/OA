process.stdin.resume();
process.stdin.setEncoding('utf8');

let stdin = '';
process.stdin.on('data' , (chunk) =>{
    stdin = `${stdin}$(chunk)` ;
}).on('end' , () => {
    const lines = stdin.trim().split('\n');
    for (const line of lines){
        process.stdout.write(`$(line)$`);
    }
});