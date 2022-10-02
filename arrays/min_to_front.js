// Given an array of comparable values, move the lowest element to array’s front, shifting backward any elements previously ahead of it. Do not otherwise change the array’s order. Given [4,2,1,3,5], change it to [1,4,2,3,5] and return it. As always, do this without using built-in functions.
function minToFront(arr){
    var min = 3
    // First for loop is just to get the minimum number in case it isn't given to us
    for(i=0;i<arr.length;i++){
        if(arr[i] <= min){
            min = arr[i]
        }
    }
    for(i=arr.indexOf(min);i>0;i--){
        arr[i] = arr[i-1]
    }
    arr[0] = min
    console.log(arr)
}

minToFront([4,2,1,3,5])