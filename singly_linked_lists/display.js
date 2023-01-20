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
    display(){
        let str = ""
        if(this.head == null){
            return("Empty list")
        }
        str += this.head.data
        let node = this.head.tail
        while(node !== null){
            str += ", " + node.data
            node = node.tail
        }
        return str
    }
}

let SLL1 = new SLL()
SLL1.addFront(76)
SLL1.addFront(2)
console.log(SLL1.display())
SLL1.addFront(11.41)
console.log(SLL1.display())