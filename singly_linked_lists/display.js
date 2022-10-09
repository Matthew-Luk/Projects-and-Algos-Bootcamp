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
            return "Empty List"
        }
        str += this.head.data
        let runner = this.head.tail
        while(runner != null){
            str += ", " + runner.data
            runner = runner.tail
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