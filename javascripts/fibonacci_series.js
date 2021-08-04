var fibonacci = function(n){
    var n1 = 0, n2 = 1; 
    var nextterm;
    for(i=0; i<n; i++){
        console.log(n1);
        nextterm = n1 + n2;
        n1 = n2;
        n2 = nextterm;
    }

};


fibonacci(30);