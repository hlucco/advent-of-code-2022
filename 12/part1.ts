import { readFileSync } from "fs";

const data = readFileSync("./data.txt", "utf-8");
const startChar = "S";
const endChar = "E";

let matrix = data.split("\n").map((x) => x.trim().split(""))
matrix = matrix.splice(0, matrix.length-1);

let startingPos;
matrix.forEach((row, i) => {
    row.forEach((col, j) => {
        if (col[j] === startChar) {
            startingPos = [i, j];
        }
    })
})

function getValue(letter: string): number {
    if (letter === startChar) {
        letter = "a";
    }

    if (letter === endChar) {
        letter = "z"
    }

    return letter.charCodeAt(0);
}

function getNeighbors(pos: number[], matrix: string[][]) {
    const offsets = [[1,0], [-1,0], [0,1], [0,-1]];
    const posValue = getValue(matrix[pos[0]][pos[1]]);
    let neighbors: number[][] = [];
    // console.log("Neighbors:");
    offsets.forEach((offset) => {
        const newNeighbor = [pos[0] + offset[0], pos[1] + offset[1]]
        if (
            // !(Object.keys(visited).includes(newNeighbor.toString())) &&
            (newNeighbor[0] >= 0 && newNeighbor[0] < matrix.length) && 
            (newNeighbor[1] >= 0 && newNeighbor[1] < matrix[0].length)
        ) {
            // console.log(matrix[newNeighbor[0]][newNeighbor[1]]);
            // console.log(getValue(matrix[newNeighbor[0]][newNeighbor[1]]));
            // console.log((getValue(matrix[newNeighbor[0]][newNeighbor[1]]) - posValue))
            const diff = getValue(matrix[newNeighbor[0]][newNeighbor[1]]) - posValue;
            if (diff <= 1) {
                neighbors.push(newNeighbor);
            }
        }
    })
    // console.log(neighbors)
    return neighbors;
}

function getMin(stack, dist) {
    let minVal = Number.MAX_VALUE;
    let best;
    stack.forEach((pos, index) => {
        if (dist[pos[0]][pos[1]] < minVal) {
            minVal = dist[pos[0]][pos[1]]
            best = [pos, index];
        }
    })

    // console.log("Best: ", best)
    return best;
}

function dijkstra(graph: string[][], source: number[]) {

    let dist = new Array(graph.length).fill(0).map(() => new Array(graph[0].length).fill(Number.MAX_VALUE));
    dist[source[0]][source[1]] = 0;
    let prev = new Array(graph.length).fill(0).map(() => new Array(graph[0].length).fill(undefined))

    let stack: number[][] = []
    for (let i = 0; i < graph.length; i++) {
        for(let j = 0; j < graph[0].length; j++) {
            stack.push([i, j])
        }
    }

    let target;
    while(stack.length !== 0) {
        const uTuple = getMin(stack, dist);
        const u: number[] = uTuple[0]
        const idx = uTuple[1]
        console.log("Current pos: ", u)

        if (graph[u[0]][u[1]] === endChar) {
            target = u;
            break;
        }

        stack.splice(idx, 1);
        const neighbors = getNeighbors(u, graph);
        console.log(neighbors)
        neighbors.forEach((v) => {
            if (stack.map((x) => x.toString()).includes(v.toString())) {
                const alt = dist[u[0]][u[1]] + 1;
                if (alt < dist[v[0]][v[1]]) {
                    dist[v[0]][v[1]] = alt
                    prev[v[0]][v[1]] = u
                }
            }
        })
    }

    let path: number[][] = []
    let currentNode = target;
    if (prev[currentNode[0]][currentNode[1]] || graph[currentNode[0]][currentNode[1]] === startChar) {
        while (currentNode) {
            path.push(currentNode)
            currentNode = prev[currentNode[0]][currentNode[1]]
        }
    }

    return path
}

const result = dijkstra(matrix, startingPos).reverse();
console.log(result, result.length-1)

// let backTrack = {}
// let goalPos;
// function dfs(pos: number[], matrix: string[][]) {
//     visited[pos.toString()] = true;
//     console.log(pos)
//     if (matrix[pos[0]][pos[1]] === endChar) {
//         goalPos = pos;
//         return
//     }

//     const neighbors = getNeighbors(pos, matrix);
//     console.log(neighbors)
//     neighbors.forEach((neighbor) => {
//         backTrack[neighbor.toString()] = pos.toString()
//         dfs(neighbor, matrix);
//         console.log("return")
//     })
// }

// dfs(startingPos, matrix);

// console.log(goalPos);
// let currentPos = goalPos.toString();
// let path: string[] = []
// while (currentPos !== startingPos.toString()) {
//     path.push(currentPos)
//     currentPos = backTrack[currentPos]
// }

// console.log(path.reverse(), path.length)