var fib = function(n){
    if(n < 2){
        return n;
    }else{
        return fib(n-1) + fib(n-2);
    }
}
var nTerms = 200;
for(let i = 0; i < nTerms; i++) {
    console.log(fib(i));
}
