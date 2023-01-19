class Node {
    constructor(val){
        this.data = val
        this.tail = null
    }
}

class SLL {
    constructor(){
        this.head = null
    }
    addFront(value){
        let newNode = new Node(value)
        if(!this.head){
            this.head = newNode
            return this
        }
        newNode.tail = this.head
        this.head = newNode
        return this
    }
    removeFront(){
        let removeNode = this.head
        this.head = removeNode.tail
        removeNode.tail = null
        return this
    }
    front(){
        if(!this.head){
            return null
        }else{
            return this.head.data
        }
    }
}

let SLL1 = new SLL()
SLL1.addFront(18)
SLL1.addFront(5)
SLL1.addFront(73)
console.log(SLL1)
SLL1.removeFront()
SLL1.removeFront()
console.log(SLL1)
console.log(SLL1.front())
SLL1.removeFront()
console.log(SLL1.front())
console.log(SLL1)