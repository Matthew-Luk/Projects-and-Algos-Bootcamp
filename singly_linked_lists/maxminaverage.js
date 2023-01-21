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
    max(){
        let max = 0
        let node = this.head
        while(node !== null){
            if(node.data > max){
                max = node.data
            }
            node = node.next
        }
        return max
    }
    min(){
        let node = this.head
        let min = node.data
        while(node !== null){
            if(node.data < min){
                min = node.data
            }
            node = node.next
        }
        return min
    }
    average(){
        let sum = 0
        let count = 0
        let node = this.head
        while(node !== null){
            sum += node.data
            count += 1
            node = node.next
        }
        return(sum/count)
    }
}