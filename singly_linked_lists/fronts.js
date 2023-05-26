class Node {
    constructor(val){
        this.data = val
        this.next = null
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
        newNode.next = this.head
        this.head = newNode
        return this
    }
    removeFront(){
        let removeNode = this.head
        this.head = removeNode.next
        removeNode.next = null
        return this
    }
    front(){
        if(!this.head){
            return null
        }else{
            return this.head.data
        }
    }
    addBack(value){
        let newNode = new Node(value)
        let node = this.head
        while(node.next != null){
            node = node.next
        }
        node.next = newNode
        return
    }
    removeBack(){
        let node = this.head
        while(node.next.next !== null){
            node = node.next
        }
        node.next = null
    }
    back(){
        let result = 0
        let node = this.head
        while(node !== null){
            result = node.data
            node = node.next
        }
        return result
    }
}

let SLL1 = new SLL()
SLL1.addFront(3)
SLL1.addBack(1)
SLL1.removeBack()
console.log(SLL1.back())
// console.log(SLL1)
// SLL1.removeFront()
// SLL1.removeFront()
// console.log(SLL1)
// console.log(SLL1.front())
// SLL1.removeFront()
// console.log(SLL1.front())
// console.log(SLL1)