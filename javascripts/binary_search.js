var doBinarySearch = function(array, targetVal){
    var min = 0;
    var max = array.length - 1;
    var guess;
    var i = 0;
    while(max >= min){
        guess = Math.floor((max+min)/2);
        console.log("guess: " +guess);
        i++;
        if(array[guess] === targetVal){
            console.log("Total number of guess: " +i);
            return guess;
        }else if(array[guess] < targetVal){
            min = guess + 1;
        }else{
            max = guess - 1;
        }

    }
    return -1;
}

var primes = [2,4,5,6,7,8,12,15,19,23,25,27,29,34,37,49,51,52,53,56,59,65,66,67,89]

var result = doBinarySearch(primes, 29)
console.log("Found at: " + result)
