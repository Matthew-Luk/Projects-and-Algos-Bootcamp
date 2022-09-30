// Print 1-255
for(i=1;i<256;i++){
    console.log("current value of i:", i)
}


// Print Sum 0-255 (print each and also the sum)
var sum = 0
for(i=0;i<256;i++){
    sum += i
    console.log("current value of i:", i, "The current sum:",sum)
}


// Find and Print Max
let arr2 = [1,10,8,2,5,4,9,7,3,6]
let max2 = 0
for(let i=0;i<arr2.length;i++){
    if(arr2[i] > max2){
        max2 = arr2[i]
    }
}
console.log(max2)


// Array with Odds and Array with Evens
let arr3 = [1,2,3,4,5,6,7,8,9,10]
let evens = []
let odds = []
for(i=0;i<arr3.length;i++){
    if(arr3[i] % 2 == 0){
        evens.push(arr3[i])
    }else if(arr3[i] % 2 != 0){
        odds.push(arr3[i])
    }
}
console.log("These are the even numbers:",evens,"These are the odd numbers:",odds)


// Greater than Y
let arr4 = [1,2,3,4,5,6,7,8,9,10]
let results = []
let y = 5
for(i=0;i<arr4.length;i++){
    if(arr4[i] > y){
        results.push(arr4[i])
    }
}
console.log("These are the numbers greater than y:",results)


// Max, Min, Avg
let arr5 = [1,10,8,2,5,4,9,7,3,6]
let min3 = [1]
let max5 = [0]
let avg = 0
for(i=0;i<arr5.length;i++){
    avg += arr5[i]
    if(arr5[i] < min3[0]){
        min3.pop()
        min3.push(arr5[i])
    }if(arr5[i] > max5[0]){
        max5.pop()
        max5.push(arr5[i])
    }
}
console.log("The average on the array is:",avg/arr5.length)
console.log("The minimum number in the array is:",min3[0])
console.log("The minimum number in the array is:",max5[0])


// Replace negative numbers with string
let arr6 = [-5,1,2,3,-8,-9,4,-7,6,-10]
for(let i=0;i<arr6.length;i++){
    if(arr6[i] < 0){
        arr6[i] = "Hello"
    }
}
console.log("This is the adjusted array:",arr6)


// Replace negative numbers with 0 and print the final array
let arr7 = [-5,1,2,3,-8,-9,4,-7,6,-10]
for(let i=0;i<arr7.length;i++){
    if(arr7[i] < 0){
        arr7[i] = 0
    }
}
console.log("This is the adjusted array:",arr7)