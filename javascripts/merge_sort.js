var merge = function(array, p, q, r){
    console.log("merge function for: " +p +" " +q +" " +r);
    //[14, 7, 3, 12, 9, 11, 6, 2];
    var lowHalf = [];
    var highHalf = [];
    var k = p; //index of main array
    var i = 0; //index of lowHalf array
    var j = 0; //index of upperHalf array

    //Divide main array into subarrays - lowHalf and highHalf arrays - using for loop
    for(var i = 0; k <= q; i++, k++){
        lowHalf[i] = array[k];        
    }
    for(var j = 0; k <= r; j++, k++){
        highHalf[j] = array[k];
    }
    
    //Get back to base index in all arrays
    k = p; i = j = 0; 
    console.log("lowhalf array: " +lowHalf);
    console.log("highhalf array: " +highHalf);
    //Sorting elements in main array by comparison - Conquer
    while(i < lowHalf.length && j < highHalf.length){
        if(lowHalf[i] < highHalf[j]){
            array[k] = lowHalf[i];
            i++;
        }else{
            array[k] = highHalf[j];
            j++;
        }
        k++;
    };

    //Add reminaing elements from either of subarrays to main array
    while(i < lowHalf.length){
        array[k] = lowHalf[i];
        i++; k++;
    }
    while(j < highHalf.length){
        array[k] = highHalf[j];
        j++; k++;
    }
    console.log("final merged array: " +array);
};

var mergeSort = function(array, startIndex, endIndex){
    if(startIndex < endIndex){
        console.log("mergeSort function for: " +startIndex +" " +endIndex);
        var middleIndex = Math.floor((startIndex + endIndex)/2);
        mergeSort(array, startIndex, middleIndex);
        mergeSort(array, middleIndex+1, endIndex);
        merge(array, startIndex, middleIndex, endIndex);
    }
};

var array = [14, 7, 3, 12, 9, 11, 6, 2];
mergeSort(array, 0, array.length-1);
console.log("Array after merging: " + array);