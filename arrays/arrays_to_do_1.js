// Given an array and an additional value, insert this value at the beginning of the array. You may use .push(), you are able do this without it though!
function pushFront(arr,num){
    arr.push(num)
    for(i=arr.length;i>0;i--){
        arr[i] = arr[i-1]
    }
    arr[0] = num
    arr.pop()
    console.log(arr)
}
pushFront([5,7,2,3],8)


// Given an array, remove and return the value at the beginning of the array. Prove the value is removed from the array by printing it. You may use .pop(), you are able do this without it though!
function popFront(arr){
    for(i=0;i<arr.length;i++){
        arr[i] = arr[i+1]
    }
    arr.pop()
    console.log(arr)
}
popFront([4,5,7,9])


// Given an array, index, and additional value, insert the value into array at given index. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val). You may use .push(), you are able do this without it though!
function insertAt(arr,index,val){
    for(i=arr.length;i>index;i--){
        arr[i] = arr[i-1]
    }
    arr[index] = val
    console.log(arr)
}
insertAt([9,33,7], 1, 42)


// Given an array and an index into array, remove and return the array value at that index. Prove the value is removed from the array by printing it. Think of popFront(arr) as equivalent to removeAt(arr,0).
function removeAt(arr,index){
    for(i=index;i<arr.length;i++){
        arr[i] = arr[i+1]
    }
    arr.pop()
    console.log(arr)
}
removeAt([8,20,55,44,98], 3)


// Swap positions of successive pairs of values of given array. If length is odd, do not change the final element.
function swapAt(arr){
    if(arr.length % 2 == 0){
        for(i=0;i<arr.length;i++){
            if(i % 2 == 0){
                var temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            }
        }
        console.log(arr)
    }else{
        for(i=0;i<arr.length-1;i++){
            if(i % 2 == 0){
                var temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            }
        }
        console.log(arr)
    }
}
swapAt(["Brendan",true,42])


// Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. If you already made the Remove At function, you are welcome to use that! If you solved this using nested loops, for an extra challenge, try to do it without any nested loops!
function removeDupes(){

}
removeDupes([9,19,19,19,19,19,29])