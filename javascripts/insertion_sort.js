var insert = function(array, rightIndex, value){
    for(var j=rightIndex; j>=0 && array[j] > value; j--){
        array[j+1] = array[j];
    }
    array[j+1] = value;
}

var insertionSort = function(array){
    for(var i = 1; i<array.length; i++){
        insert(array,i-1,array[i]);
    }
};
var array = [22, 11, 99, 88, 9, 7, 42];
insertionSort(array);
console.log(array);


/*var array = [3, 5, 7, 11, 13, 2, 9, 6];

insert(array, 4, 2);
console.log("Array after inserting 2:  " + array);
Program.assertEqual(array, [2, 3, 5, 7, 11, 13, 9, 6]);

insert(array, 5, 9);
console.log("Array after inserting 9:  " + array);
Program.assertEqual(array, [2, 3, 5, 7, 9, 11, 13, 6]);

insert(array, 6, 6);
console.log("Array after inserting 6:  " + array);
Program.assertEqual(array, [2, 3, 5, 6, 7, 9, 11, 13]);*/
