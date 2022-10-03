class Country {
    constructor(countryName, countryCapital, countryFlag, currency, government, language){
        this.countryName = countryName
        this.countryCapital = countryCapital
        this.countryFlag = countryFlag
        this.government = government
        this.language = language
        this.population = ""
        this.currency = ""
        this.state = []
    }
    addCurrency(currency){
        this.currency = currency
    }
    addState(state){
        this.state.push(state)
    }
}
class State{
    constructor(stateName,stateCapital,stateFlag,accent){
        this.stateName = stateName
        this.stateCapital = stateCapital
        this.stateFlag = stateFlag
        this.accent = accent
        this.bird = ""
    }
}

let america = new Country("Murica", "DC", "Starts and Stripes", "Constitutional Republic", "JavaScript")
// console.log("Country instance #1a: ", america)
america.currency = "Dollar"
// console.log("Country instance #1b: ", america)
america.addCurrency("NinjaBucks")
// console.log("Country instance #1c: ", america)

let dojo = new State("Dojo", "Silicon Valley", "Ninja Man", "Silent")
// console.log("State instance #1a: ", dojo)
let gendal = new State("Gendale", "Josh City", "MERN Master", "Floridian")

america.addState(dojo)
america.addState(gendal)
console.log("Country instance #1d: ", america)
console.log("State instance #1b: ", dojo)