import { readFileSync } from "fs";

class Monkey {
    id: number
    items: number[]
    operation: (a: number) => number
    test: number
    next: number[]
    inspectCount: number

    constructor(
        id: number, 
        items: number[], 
        operation: (a: number) => number, 
        test:number, 
        next: number[]
    ) {
        this.items = items;
        this.id = id;
        this.operation = operation;
        this.test = test;
        this.next = next;
        this.inspectCount = 0;
    }

    takeTurn(monkeys: Monkey[]) {
        this.items.forEach((item) => {
            const newValue = this.operation(item);
            const boardValue = Math.floor(newValue / 3);
            if (boardValue % this.test === 0) {
                monkeys[this.next[0]].recieveItem(boardValue);
            } else {
                monkeys[this.next[1]].recieveItem(boardValue);
            }
            this.items = this.items.filter((x) => x !== item)
            this.inspectCount++;
        })

        return monkeys;
    }

    recieveItem(item: number) {
        this.items.push(item);
    }
}

function parseMonkey(monkeyLines: string[]): Monkey {
    const id = parseInt(monkeyLines[0].split(" ")[1][0]);
    const items = monkeyLines[1].split(" ").splice(4, monkeyLines[1].split(" ").length).map((x) => parseInt(x));
    const tokens = monkeyLines[2].split(" ").splice(6, monkeyLines[2].split(" ").length);
    let operation = (old) => (tokens[1].trim() === "old" ? old : parseInt(tokens[1])) + old;
    if (tokens[0] === "*") {
        operation = (old) => (tokens[1].trim() === "old" ? old : parseInt(tokens[1])) * old;
    }
    const test = parseInt(monkeyLines[3].split(" ")[5]);
    const next = [(parseInt(monkeyLines[4].split(" ")[9])), (parseInt(monkeyLines[5].split(" ")[9]))];
    return new Monkey(id, items, operation, test, next);
}

const data = readFileSync("./data.txt", "utf-8").split("\n");

let monkeys: Monkey[] = []
let currentMonkey: string[] = []

for(let i = 0; i < data.length; i++) {
    currentMonkey.push(data[i])
    if (data[i] === "\r" || i === data.length-1) {
        monkeys.push(parseMonkey(currentMonkey));
        currentMonkey = []
    }
}

const rounds = 20;

for(let i = 0; i < rounds; i++) {
    for(let m = 0; m < monkeys.length; m++) {
        let currentMonkey = monkeys[m];
        monkeys = currentMonkey.takeTurn(monkeys);
    }
}

console.log(monkeys.map((monkey) => monkey.inspectCount).sort((a, b) => b - a).splice(0, 2).reduce((p, c) => p * c, 1))

