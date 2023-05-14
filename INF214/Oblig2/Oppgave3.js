function* itmp(iterable_input, func_to_be_applied) {
    for(let x of iterable_input){
        x = func_to_be_applied(x)
        yield x;
    }
}
const p = itmp( [10, 20],  x => x * x );
console.log( p.next() ); // 100
console.log( p.next() ); // 400
