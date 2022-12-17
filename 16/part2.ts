import { readFileSync } from "fs";

// This code takes many hours to
// run but does get the correct answer

class Node {
    flow: number
    id: string
    neighbors: string[]

    constructor(id: string, flow: string, neighbors: string[]) {
        this.id = id
        this.flow = Number.parseInt(flow);
        this.neighbors = neighbors;
    }
}

class Graph {
    nodes: { [id: string]: Node }
    constructor() {
        this.nodes = {}
    }
}

function parse_lines(lines: string[]) {
    let graph = new Graph();
    lines.forEach((line) => {
        const tokens = line.split(" ");
        const id = tokens[1]
        const flow = tokens[4].split("=").reverse()[0].replace(";", "");
        const neighbors = tokens.splice(9, tokens.length).map((x) => x.replace(",", ""));
        const newNode = new Node(id, flow, neighbors);
        graph.nodes[id] = newNode;
    })
    return graph;
}

let memory = {}

function dfs(graph: Graph, time: number, current: string, opened: {[id: string] : boolean}, rate: number, elephant: string) {
    if (time === 0) {
        return 0;
    }

    let stateString = "";
    Object.values(opened).forEach((value) => {
        stateString += (value ? "1" : "0");
    })
    stateString += String(time);
    stateString += String(current);
    stateString += String(elephant);

    if (stateString in memory) {
        return memory[stateString]
    }

    let released = 0;

    const currentOpen = !opened[current] && graph.nodes[current].flow > 0;
    const elephantOpen = !opened[elephant] && graph.nodes[elephant].flow > 0 && current !== elephant;

    // both can open
    if(currentOpen && elephantOpen) {
        // both open
        let nextOpened = {...opened, [current] : true, [elephant] : true };
        let nextRate = rate + graph.nodes[current].flow + graph.nodes[elephant].flow;
        let alt = dfs(graph, time - 1, current, nextOpened, nextRate, elephant)
        released = Math.max(released, alt)

        // i open elephant moves
        // nextOpened = {...opened, [current] : true}
        // nextRate = rate + graph.nodes[current].flow;
        // const nextElephants = graph.nodes[elephant].neighbors
        // nextElephants.forEach((neighbor) => {
        //     let alt = dfs(graph, time - 1, current, nextOpened, nextRate, neighbor)
        //     released = Math.max(released, alt)
        // })

        // i move elephant opens
        // nextOpened = {...opened, [elephant] : true}
        // nextRate = rate + graph.nodes[elephant].flow;
        // const nextPersons = graph.nodes[current].neighbors;
        // nextPersons.forEach((neighbor) => {
        //     let alt = dfs(graph, time - 1, neighbor, nextOpened, nextRate, elephant);
        //     released = Math.max(released, alt);
        // })
    } else if (currentOpen && !elephantOpen) {
        // i open elphant moves
        let nextOpened = {...opened, [current] : true};
        let nextRate = rate + graph.nodes[current].flow;
        
        const nextElephants = graph.nodes[elephant].neighbors;
        nextElephants.forEach((neighbor) => {
            let alt = dfs(graph, time - 1, current, nextOpened, nextRate, neighbor);
            released = Math.max(released, alt);
        })
    } else if (!currentOpen && elephantOpen) {
        // elepahnt opens i move
        let nextOpened = {...opened, [elephant] : true};
        let nextRate = rate + graph.nodes[elephant].flow;
        const nextPersons = graph.nodes[current].neighbors;
        nextPersons.forEach((neighbor) => {
            let alt = dfs(graph, time - 1, neighbor, nextOpened, nextRate, elephant);
            released = Math.max(released, alt);
        })
    } 

    const nextPersons = graph.nodes[current].neighbors;
    const nextElephants = graph.nodes[elephant].neighbors;

    nextPersons.forEach((nextPerson) => {
        nextElephants.forEach((nextElephant) => {
            let alt = dfs(graph, time - 1, nextPerson, opened, rate, nextElephant);
            released = Math.max(released, alt);
        })
    })

    released += rate;
    memory[stateString] = released;
    return released
}

function run() {
    const lines = readFileSync("./data.txt", 'utf-8').trim().split("\n");
    const graph = parse_lines(lines);

    let valveMap = {};
    Object.keys(graph.nodes).forEach((id) => {
        valveMap[id] = false;
    })

    const root = "AA";
    const result = dfs(graph, 26, root, valveMap, 0, root)
    // console.log("finished")
    console.log(result);
}

run();