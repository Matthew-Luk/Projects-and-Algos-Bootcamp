// Create a function that, given a string, returns all of that string’s contents, but without blanks. 
function removeBlanks(str){
    var str2 = ""
    for(i=0;i<str.length;i++){
        if(str[i] != " "){
            str2 += str[i]
        }
    }
    console.log("The string with no spaces:",str2)
}
removeBlanks(" Pl ayTha tF u nkyM usi c ")
removeBlanks("I can not BELIEVE it's not BUTTER")


// Create a JavaScript function that given a string, returns the integer made from the string’s digits. You are allowed to use isNaN() and Number().
function getDigits(str){
    var str3 = ""
    for(i=0;i<str.length;i++){
        if(!isNaN(str[i])){
            str3 += str[i]
        }
    }
    console.log("The string with numbers only:",str3)
}
getDigits("abc8c0d1ngd0j0!8")
getDigits("0s1a3y5w7h9a2t4?6!8?0")


// Create a function that, given a string, returns the string’s acronym (first letter of the word capitalized). You are allowed to use .split() and .toUpperCase().
function acronym(str){
    var str4 = ""
    str = str.split(" ")
    for(i=0;i<str.length;i++){
        if(str[i].length>0){
            str4 += str[i][0]
        }
    }
    console.log(str4.toUpperCase())
}
acronym(" there's no free lunch - gotta pay yer way. ")
acronym("Live from New York, it's Saturday Night!") 


// Create a function that, given a string, returns the number of non-space characters found in the string.
function countNonSpaces(str){
    var total = 0
    for(i=0;i<str.length;i++){
        if(str[i] != " "){
            total += 1
        }
    }
    console.log("The total number of non-space characters found in the string:",total)
}
countNonSpaces("Honey pie, you are driving me crazy")
countNonSpaces("Hello world !")


// Create a function that, given an array of strings and a numerical value, returns an array that only contains strings longer than or equal to the given value.
function removeShorterStrings(arr,num){
    newArr = []
    for(i=0;i<arr.length;i++){
        if(arr[i].length >= num){
            newArr.push(arr[i])
        }
    }
    console.log("These are the strings that are longer than or equal to the given value:",newArr)
}
removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4)
removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3)