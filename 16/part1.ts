import { readFileSync } from "fs";

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

function dfs(graph: Graph, time: number, current: string, opened: {[id: string] : boolean}, rate: number) {
    if (time === 0) {
        return 0;
    }

    let stateString = "";
    Object.values(opened).forEach((value) => {
        stateString += (value ? "1" : "0");
    })
    stateString += String(time)
    stateString += String(current);

    if (stateString in memory) {
        return memory[stateString]
    }

    let released = 0;

    if (!opened[current] && graph.nodes[current].flow > 0) {
        let nextOpened = {...opened, [current] : true};
        let nextRate = rate + graph.nodes[current].flow;
        released = dfs(graph, time - 1, current, nextOpened, nextRate)
    }

    const neighbors = graph.nodes[current].neighbors;
    neighbors.forEach((next) => {
        let alt = dfs(graph, time - 1, next, opened, rate)
        released = Math.max(released, alt)
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
    const result = dfs(graph, 30, root, valveMap, 0)
    // console.log("finished")
    console.log(result);
}

run();