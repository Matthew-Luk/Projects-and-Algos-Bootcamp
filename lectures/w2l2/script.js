class Node {
    constructor(val) {
        this.val = val
        this.next = null
    }
}

class sll {
    constructor(){
        this.head = null
        this.tail = null
        this.length = 0
    }
    push(val){
        let newNode = new Node(val)
        if(!this.head){
            this.head = newNode
            this.tail = this.head
        }else{
            this.tail.next = newNode
            this.tail = newNode
        }
        this.length++
        return this
    }
    unshift(val){
        let newNode = new Node(val)
        if(!this.head){
            this.head = newNode
            this.tail = this.head
        }else{
            newNode.next = this.head
            this.head = newNode
        }
        this.length++
        return this
    }
    pop(){
        if(!this.head){
            return undefined
        }
        var current = this.head
        var newTail = current
        while(current.next){
            newTail = current
            current = current.next
        }
        this.tail = newTail
        this.tail.next = null
        this.length--
        if(this.length === 0){
            this.head = null
            this.tail = null
        }
        return current
    }
}

let test = new sll
test.push("Turn on computer").push("Log into computer").unshift("Plug computer into power").push("Log into website").pop()
//console.log("do we console log test?",test)
console.log(test)

let newTest = new sll
newTest.pop()
console.log(newTest)