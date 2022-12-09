import { readFileSync } from "fs";

function updateHead(startPos: Position, direction: string): Position {

    switch(direction) {
        case("U"):
            startPos.x -= 1
            break;
        case("D"):
            startPos.x += 1
            break;
        case("R"):
            startPos.y += 1
            break
        default:
            startPos.y -= 1
    }

    return startPos
}

function updateTail(headPos: Position, tailPos: Position): Position {
    // row same col dif
    // positive diff right and down
    // negative diff up and left

    if (headPos.x == tailPos.x) {
        const diff = headPos.y - tailPos.y;
        if (Math.abs(diff) > 1) {
            tailPos.y = diff < 0 ? tailPos.y -1 : tailPos.y + 1;
        }
    }

    if (headPos.y == tailPos.y) {
        const diff = headPos.x - tailPos.x;
        if (Math.abs(diff) > 1) {
            tailPos.x = diff < 0 ? tailPos.x -1 : tailPos.x + 1
        }
    }
    
    // col same row diff
    if (headPos.x !== tailPos.x && headPos.y != tailPos.y) {
        // const distance = Math.hypot(tailPos.x - headPos.x, tailPos.y - headPos.y);
        const distance = Math.abs(headPos.x - tailPos.x) + Math.abs(headPos.y - tailPos.y);
        if (distance > 2) {
            let minDistance = Number.MAX_VALUE;
            let bestMove;
            const potentialMoves = [[1,1], [-1,-1], [1,-1], [-1, 1]];
            for(let i = 0; i < potentialMoves.length; i++) {
                const currentPos = {x: tailPos.x + potentialMoves[i][0], y: tailPos.y + potentialMoves[i][1]};
                const moveDistance = Math.abs(headPos.x - currentPos.x) + Math.abs(headPos.y - currentPos.y);
                if (moveDistance <= minDistance) {
                    bestMove = currentPos;
                    minDistance = moveDistance;
                }
            }
            tailPos.x = bestMove.x;
            tailPos.y = bestMove.y
        }
    }

    return tailPos;
}

const data = readFileSync("./data.txt", "utf-8");
const lines = data.split("\n").map((i => i.replace("\r", "")));

type Position = {
    x: number,
    y: number
}

let visited: Position[] = [];

let headPos = {x: 0, y: 0};
let tailPos = {x: 0, y: 0};

for (let i = 0; i < lines.length; i++) {
    const direction = lines[i].split(" ")[0];
    const steps = Number(lines[i].split(" ")[1]);

    let stepsRemaining = steps;
    while(stepsRemaining > 0) {
        visited.push({x: tailPos.x, y: tailPos.y});
        headPos = updateHead(headPos, direction);
        tailPos = updateTail(headPos, tailPos);
        console.log(tailPos)

        stepsRemaining -= 1
    }
}

//@ts-ignore
const unqiue = Array.from(new Set(visited.map(JSON.stringify))).map(JSON.parse);
console.log(unqiue.length)

