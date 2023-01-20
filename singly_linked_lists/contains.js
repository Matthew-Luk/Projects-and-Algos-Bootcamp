class Node{
    constructor(data){
        this.data = data
        this.tail = null
    }
}

class LinkedList {
    constructor(){
        this.head = null
    }
    findSum(){
        let runner = this.head
        let sum = 0
        while(runner !== null){
            sum += runner.data
            runner = runner.tail
        }
        return sum
    }
    contains(value){
        let runner = this.head
        while(runner !== null){
            if(runner.data == value){
                return true
            }
            runner = runner.tail
        }
        return false
    }
}