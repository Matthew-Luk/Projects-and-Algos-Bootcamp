class Node{
    constructor(data){
        this.head = data
        this.tail = null
    }
}

class SLL{
    constructor(){
        this.head = null
    }
    length(){
        let runner = this.head
        let sum = 0
        while(runner !== null){
            sum += 1
            runner = runner.tail
        }
        return sum
    }
}