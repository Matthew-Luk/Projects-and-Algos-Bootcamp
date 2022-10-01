// Set myNumber to 42. Set myName to your name. Now swap myNumber into myName & vice versa.
var myNumber = 42
var myName = "Matthew"
var temp = myNumber
myNumber = myName
myName = temp
console.log("This is my number:",myNumber,"This is my name:",myName)


// Print integers from -52 to 1066 using a FOR loop.
for(i=-52;i<=1066;i++){
    console.log("This is the current value of i:",i)
}


// Create beCheerful(). Within it, console.log string "good morning!" Call it 98 times.
function beCheerful(){
    console.log("good morning!")
}
for(i=0;i<=98;i++){
    beCheerful()
}


// Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.
for(i=-300;i<=-7;i+=3){
    console.log("This is the current value of i:",i)
}


// Print integers from 2000 to 5280, using a WHILE.
var i=2000
while(i<=5280){
    console.log("This is the current value of:",i)
    i++
}


// If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day...." 


// Write a function that determines whether a given year is a leap year. If a year is divisible by four, it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is.
function leapYear(year){
    if(year % 4 == 0 && year % 100 != 0){
        console.log("This is a leap year")
    }else if (year % 100 == 0 && year % 400 == 0){
        console.log("This is a leap year")
    }
}
leapYear(2040)


// Print all integer multiples of 5, from 512 to 4096. Afterward, also log how many there were.
function multiplesof5(){
    let total = 0
    for(i=512;i<=4096;i++){
        if(i % 5 == 0){
            total += 1
            console.log("The current value of i:",i)
        }
    }
    console.log("The total number of multiples is:",total)
}
multiplesof5()


// Print multiples of 6 up to 60,000, using a WHILE.
var i = 0
while(i<=60000){
    if(i % 6 == 0){
        console.log("This is the current value of i:",i)
    }
    i++
}


// Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for(i=1;i<=100;i++){
    if(i % 5 == 0 && i % 10 == 0){
        console.log('Coding Dojo')
    }else if(i % 5 == 0){
        console.log('Coding')
    }else{
        console.log(i)
    }
}


// Your function will be given an input parameter incoming. Please console.log this value.
function incoming(incoming){
    console.log(incoming)
}
incoming("Hello World")


// Add odd integers from -300,000 to 300,000, and console.log the final sum. Is there a shortcut?
function oddInts(){
    for(i=-300000;i<=300000;i++){
        var sum = 0
        if(i % 2 == 1){
            sum += i
        }
    }
    console.log("This is the final sum:", sum)
}
oddInts()


// Log positive numbers starting at 2016, counting down by fours (exclude 0), without a FOR loop.
var i = 2016
while(i>=0){
    console.log("This is the current value of i:",i)
    i = i-4
}


// Based on earlier “Countdown by Fours”, given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).
function flexibleCountdown(lowNum,highNum,mult){
    for(i=highNum;i>=lowNum;i--){
        if(i%mult == 0){
            console.log(i)
        }
    }
}
flexibleCountdown(2,9,3)


// This is based on “Flexible Countdown”. The parameter names are not as helpful, but the problem is essentially identical; don’t be thrown off! Given 4 parameters (param1,param2,param3,param4), print the multiples of param1, starting at param2 and extending to param3. One exception: if a multiple is equal to param4, then skip (don’t print) it. Do this using a WHILE. Given (3,5,17,9), print 6,12,15 (which are all of the multiples of 3 between 5 and 17, and excluding the value 9)
function finalCountdown(param1,param2,param3,param4){
    var i = param2
    while(i<=param3){
        if(i === param4){
        }else if(i % param1 == 0){
            console.log(i)
        }
        i++
    }
}
finalCountdown(3,5,17,9)