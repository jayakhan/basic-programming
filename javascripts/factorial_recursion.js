var memo = {}; //Memomization is to improve efficiency by leveraging values already calculated before
var recursion = function(n){
    if(n === 0){
        return 1;
    }else if(memo.hasOwnProperty(n)){
        return memo[n];
    }
    var result = n*recursion(n-1);
    memo[n] = result;
    return result;
}

console.log("Factorial of 6 is:  " +recursion(6));