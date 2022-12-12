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
    let y = "even"
    for(i=0;i<arr.length;i++){
        if(arr[i] % 2 == 1){
            if(y == "odd"){
                x += 1
            }else{
                y = "odd"
                x = 1
            }
        }else{
            if(y == "even"){
                x += 1
            }else{
                y = "even"
                x = 1
            }
        }
        // handles printing even statement/odd statement
        if(x >= 3){
            if(y == "even"){
                console.log("Even more so")
            }else{
                console.log("That's odd")
            }
        }
    }
}


// if there is a transition between odds and evens we reset counter
evenAndOdds([1,1,1,1,2,2,2,3,4,4,5,5,5])


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


// Given array, write a function to reverse values, in-place. Example: reverse([3,1,6,4,2]) returns same array, containing [2,4,6,1,3].
function reverse(arr){
    console.log(arr.map((item,index) => arr[arr.length-1-index]))
}

console.log(reverse([3,1,6,4,2]))

function reverse(arr){
    let i = 0
    while(i < arr.length - 1){
        arr.splice(i,0,arr.pop())
        i++
    }
    return arr
}

console.log(reverse([3,1,6,4,2]))


// Given an array, create and return a new one containing all the values of the provided array, made negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5].
function negative(arr){
    let x = []
    for(i=0;i<arr.length;i++){
        if(arr[i] < 0){
            x.push(arr[i])
        }else{
            x.push(arr[i]*-1)
        }
    }
    return x
}

let f = negative([1,-3,5])
console.log(f)


// Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food". If no array elements are "food", then print "I'm hungry" once.
function alwaysHungry(arr){
    let x = 0
    for(i=0;i<arr.length;i++){
        if(arr[i] == "food"){
            console.log("yummy")
            x += 1
        }
    }if(x == 0){
        console.log("I'm hungry")
    }
}

alwaysHungry(["food","yellow","hello","food"])
alwaysHungry(["hello","world","good","bad","yellow"])


// Given array, swap first and last, third and third-tolast, etc.
function swap(arr){
    n = arr.length - 1
    for(i=0;i<arr.length/2;i++){
        let temp = arr[i]
        arr[i] = arr[n-i]
        arr[n-i] = temp
    }
    console.log(arr)
}

swap([1,2,3,4,5,6])


// Given array arr and number num, multiply each arr value by num, and return the changed arr.
function scale(arr,num){
    for(i=0;i<arr.length;i++){
        arr[i] = arr[i] * num
    }
    console.log(arr)
}

scale([1,2,3,4,5],3)