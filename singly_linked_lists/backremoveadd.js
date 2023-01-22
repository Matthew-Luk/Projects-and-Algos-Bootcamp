class Node{
    constructor(value){
        this.head = value
        this.next = null
    }
}

class SLL{
    constructor(){
        this.head = null
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
    removeBack(){
        let node = this.head
        while(node.next.next !== null){
            node = node.next
        }
        node.next = null
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
}