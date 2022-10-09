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
        newNode.tail = this.head
        this.head = newNode
        return this.head
    }
    removeFront(){
        let removedNode = this.head
        this.head = removedNode.tail
        removedNode.tail = null
        return this.head
    }
    front(){
        if(this.head == null){
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
SLL1.removeFront()
SLL1.removeFront()
console.log(SLL1.front())
SLL1.removeFront()
console.log(SLL1.front())