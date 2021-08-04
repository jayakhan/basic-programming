palindrome = function(str){
    if(str.length <= 1){
        return 'yes';
    }else if(str.slice(0,1) !== str.slice(-1)){
        return 'no'
    }
    return palindrome(str.slice(1,-1));
}

var str = 'aaaaaaaaa';
var result = palindrome(str);
console.log("Is it a palindrome?:  " +result);
