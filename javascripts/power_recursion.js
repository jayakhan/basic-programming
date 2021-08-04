var power = function (x,n){
    if(n === 0){ //zero
        return 1;
    }
    else if(n < 0){ //reciprocal
        var a = power(x, -n);
        return 1/a;
    }
    else if((n%2) === 0){ //even
        var y = power(x, n/2);
        return y*y;
    }
    else if((n%2) !== 0){ //odd
        return x*power(x, n-1);
    }  
};
console.log(power(3,-1));