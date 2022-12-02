// Create a function that accepts a number as an input. Return a new array that counts down by one, from the number (as array’s ‘zeroth’ element) down to 0 (as the last element). How long is this array?
function Countdown(num){
    let newArray = []
    for(i=num;i>=0;i--){
        newArray.push(i)
    }
    console.log(newArray)
}

Countdown(15)


// Your function will receive an array with two numbers. Print the first value, and return the second.
function printAndReturn(arr){
    console.log("This is being printed:",arr[0])
    return(`This is being returned: ${arr[1]}`)
}

let a = printAndReturn([5,10])
console.log(a)


//Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).
function firstPlusLength(arr){
    let x = 0
    if(Number.isInteger(arr[0])){
        x = arr[0]
    }else{
        x = arr[1]
    }
    for(i=0;i<arr.length;i++){
        x += 1
    }
    console.log(x)
}

firstPlusLength([1,3,5,7,9])


// For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is.
function valuesGreaterThanSecond(arr){
    let x = 0
    for(i=0;i<arr.length;i++){
        if(arr[i] > arr[1]){
            console.log(arr[i])
            x += 1
        }
    }
    return(`The total count of numbers greater than the second value: ${x}`)
}

let b = valuesGreaterThanSecond([1,3,5,7,9,13])
console.log(b)


// Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. Print how many values this is. What will you do if the array is only one element long?
function valuesGreaterThanSecondGeneralized(arr){
    let x = 0
    for(i=0;i<arr.length;i++){
        if(arr[i] > arr[1]){
            console.log(arr[i])
            x += 1
        }
    }
    return(`The total count of numbers greater than the second value: ${x}`)
}

let c = valuesGreaterThanSecondGeneralized([10,20,15,17,35,80])
console.log(c)


// Given two numbers, return array of length num1 with each value num2. Print "Jinx!" if they are same.
function thisLengthThatValue(num1,num2){
    let x = []
    if(num1 === num2){
        return("Jinx")
    }else{
        for(i=0;i<num1;i++){
            x.push(num2)
        }
        return(x)
    }
}

let d = thisLengthThatValue(5,5)
console.log(d)
let e = thisLengthThatValue(5,10)
console.log(e)


// Your function should accept an array. If value at [0] is greater than array’s length, print "Too big!"; if value at [0] is less than array’s length, print "Too small!"; otherwise print "Just right!".
function fitTheFirstValue(arr){
    if(arr[0] < arr.length){
        console.log("Too small!")
    }else if(arr[0] > arr.length){
        console.log("Too big!")
    }else{
        console.log("Just right!")
    }
}

fitTheFirstValue([1,2,3,4,5])
fitTheFirstValue([7,2,3,4,5])
fitTheFirstValue([5,2,3,4,5])


// Kelvin wants to convert between temperature scales. Create fahrenheitToCelsius(fDegrees) that accepts a number of degrees in Fahrenheit and returns the equivalent temperature as expressed in Celsius degrees. For review, Fahrenheit = (9/5 * Celsius) + 32.
function fahrenheitToCelsius(num){
    let x = (num - 32) * 5/9
    return(x)
}

let f = fahrenheitToCelsius(100)
console.log(f)

// Create celsiusToFahrenheit(cDegrees) that accepts number of degrees Celsius, and returns the equivalent temperature expressed in Fahrenheit degrees.
function celsiusToFahrenheit(num){
    let x = ((9/5) * num + 32) 
    return(x)
}

let g = celsiusToFahrenheit(100)
console.log(g)

// Do Fahrenheit and Celsius values equate at a certain number? The scientific calculation can be complex, so for this challenge just try a series of Celsius integer values starting at 200, going downward (descending), checking whether it is equal to the corresponding Fahrenheit value
// -40 degrees Celsius would equal to -40 degrees Fahrenheit
