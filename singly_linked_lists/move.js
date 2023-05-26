class Node{
    constructor(value){
        this.data = value
        this.next = null
    }
}

class SLL{
    constructor(){
        this.head = null
    }
    moveMin(){
        let min = 0
        let node = this.head
        while(node != null){
            if(node.data < min){
                min = node.data
            }
        }
    }
    moveMax(){
        let max = 0
        let node = this.head
        while(node != null){
            if(node.data > max){
                max = node.data
            }
            node = node.next
        }
        node = this.head
        while(node.data != max){
            node = node.next
        }
        console.log(node.data)
        let newNode = new Node(max)

    }
}