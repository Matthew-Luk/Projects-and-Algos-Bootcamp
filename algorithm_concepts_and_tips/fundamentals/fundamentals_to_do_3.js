// Given an array, write a function that changes all positive numbers in the array to “big”.
function makeItBig(arr){
    for(i=0;i<arr.length;i++){
        if(arr[i] > 0){
            arr[i] = "big"
        }
    }
    return(arr)
}

let a = makeItBig([-1,3,5,-5])
console.log(a)


// Create a function that takes an array of numbers. The function should print the lowest value in the array, and return the highest value in the array.
function printLowReturnHigh(arr){
    let x = arr[0]
    let y = arr[0]
    for(i=0;i<arr.length;i++){
        if(arr[i] < x){
            x = arr[i]
        }else if(arr[i] > y){
            y = arr[i]
        }
    }
    console.log("This is the lowest number:", x)
    console.log("This is the highest number:", y)
}

printLowReturnHigh([5,1,2,3,20,19,4])


// Build a function that takes an array of numbers. The function should print the second-to-last value in the array, and return first odd value in the array.
function printOneReturnAnother(arr){
    let x = 0
    for(i=0;i<arr.length;i++){
        if(x == 0){
            if(arr[i] % 2 != 0){
                x = arr[i]
            }
        }
    }
    console.log("This is the second to last number in the array:", arr[arr.length-2])
    return(`The first odd number is: ${x}`)
}

let b = printOneReturnAnother([4,2,3,4,5])
console.log(b)


// Given an array, create a function to return a new array where each value in the original has been doubled. Calling double([1,2,3]) should return [2,4,6] without changing original.
function double(arr){
    let x = []
    for(i=0;i<arr.length;i++){
        x.push(arr[i] * 2)
    }
    return x
}

let c = double([1,2,3])
console.log(c)


// Given an array of numbers, create a function to replace last value with the number of positive values. Example,  countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.
function countPositives(arr){
    let x = 0
    for(i=0;i<arr.length;i++){
        if(arr[i] < 0){
            x += 1
        }
    }
    arr[arr.length-1] = x
    console.log(arr)
}

countPositives([-1,-1,-1,1])


// Create a function that accepts an array. Every time that array has three odd values in a row, print "That’s odd!" Every time the array has three evens in a row, print "Even more so!"
function evenAndOdds(arr){
    let x = 0
    for(i=0;i<arr.length;i++){
        
    }
}

evenAndOdds([1,1,1,2,2,2,3,4,4,5,5,5])


// Given arr, add 1 to odd elements ([1], [3], etc.), console.log all values and return arr.
function incrementSeconds(arr){
    for(i=0;i<arr.length;i++){
        if(i%2 != 0){
            arr[i] = arr[i] + 1
        }
    }
    return arr
}

let d = incrementSeconds([1,1,3,3,5])
console.log(d)


// You are passed an array containing strings. Working within that same array, replace each string with a number – the length of the string at previous array index – and return the array.
function previousLengths(arr){
    let x = [0]
    for(i=1;i<arr.length;i++){
        x.push(arr[i-1].length)
    }
    console.log(x)
}

previousLengths(["hello","world","good","bad","yellow"])


// Build a function that accepts an array. Return a new array with all values except first, adding 7 to each. Do not alter the original array.
function addSevenToMost(arr){
    let x = [arr[0]]
    for(i=1;i<arr.length;i++){
        x.push(arr[i] + 7)
    }
    return x
}

let e = addSevenToMost([1,2,3,4,5])
console.log(e)