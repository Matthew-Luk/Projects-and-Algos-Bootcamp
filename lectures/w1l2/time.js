console.log("JS sheet is connected")

function theDateTime(){
    console.log("Inside the function")
    var t = new Date()
    console.log("The time is:",t)
    document.getElementById("dateTime").innerText = t
}
theDateTime()

function theDate(){
    console.log("Inside the second function")
    var t = new Date()
    var temp = t.toString()
    dateOnly = temp.slice(0,15)
    console.log("The date is:",temp)
    document.getElementById("date").innerText = dateOnly
}
theDate()

function theTime(){
    console.log("Inside the third function")
    var t = new Date()
    var temp = t.toString()
    timeOnly = temp.slice(16,60)
    console.log("The time is:",temp)
    document.getElementById("time").innerText = timeOnly
}
theTime()