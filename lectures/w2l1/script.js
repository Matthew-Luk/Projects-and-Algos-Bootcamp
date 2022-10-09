/* Given an array of numbers in your function, find the largest value in the array. No Googling, and no built-ins. 
Assume your given array will have at least one number in it. */
function maxValue(arr){
    let x = 0
    for(i=0;i<arr.length;i++){
        if(arr[i] > x){
            x = arr[i]
        }
    }
    console.log("The max value of the array is:", x)
}

maxValue([4,8,2,10,5])
maxValue([5,2,3,1,7])


/* Given an array of numbers in your function, return the SECOND highest value in the array. No Googling, and no built-ins. 
Assume your given array will have at least two numbers in it. */
function secondHighest(arr){
    let x = 0
    let y = 0
    for(i=0;i<arr.length;i++){
        if(arr[i] > x){
            x = arr[i]
        }
    }
    for(i=0;i<arr.length;i++){
        if(arr[i] > y && arr[i] < x){
            y = arr[i]
        }
    }
    console.log("The second largest value in the array is:",y)
}

secondHighest([4,8,2,10,5])
secondHighest([20,40,33,19,25])


class Node {
    constructor(val) {
        this.data = val
        this.next = null
    }
}

class SLL {
    constructor() {
        this.head = null
    }
    addFront(val) {
        let new_node = new Node(val)
        
    }
}

// create new SLL
var sll1 = new SLL()
// console.log(sll1)

// create new Node
var n1 = new Node(1)
// console.log(n1)

// assign sll1.head = Node instance created above
sll1.head = n1
// console.log(sll1)

var n2 = new Node(9)
sll1.head.next = n2
// console.log(sll1)

var n3 = new Node(33)
console.log(sll1.head.next)
sll1.head.next.next = n3
console.log(sll1)