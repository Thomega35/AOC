package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	f, inputParsed := mustOpenFile("input.txt")
	defer f.Close()

	// map string to tuple int, int
	mapObjectPlaced := make(map[Position]bool)
	var playerPosition *Position = nil
	playerPosition = customInputParsing(inputParsed, mapObjectPlaced)

	numberInfinityLoop := 0

	for x := 0; x < len(inputParsed[0]); x++ {
		for y := 0; y < len(inputParsed); y++ {
			if _, ok := mapObjectPlaced[Position{x, y}]; !ok {
				newMapObjectPlaced := make(map[Position]bool)
				for key, value := range mapObjectPlaced {
					newMapObjectPlaced[key] = value
				}
				newMapObjectPlaced[Position{x, y}] = true

				lenToLeave := getLenToLeave(newMapObjectPlaced, &Position{playerPosition.x, playerPosition.y}, inputParsed)
				fmt.Println(lenToLeave)
				if lenToLeave == -1 {
					numberInfinityLoop++
				}
			}
		}
	}
	fmt.Println(playerPosition)
	fmt.Println(numberInfinityLoop)
}

func customInputParsing(inputParsed []string, mapObjectPlaced map[Position]bool) *Position {
	playerPosition := &Position{}
	for indexL, line := range inputParsed {
		for indexC, char := range line {
			if char == '#' {
				// add to map
				mapObjectPlaced[Position{indexC, indexL}] = true
			} else if char == '^' {
				playerPosition.x = indexC
				playerPosition.y = indexL
			}
		}
	}
	return playerPosition
}

func mustOpenFile(filename string) (*os.File, []string) {
	f, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return nil, nil
	}

	inputParsed := []string{}
	// splitline
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		rawText := scanner.Text()
		// Process each line here
		// Split line into words
		lines := strings.Split(rawText, "\n")
		inputParsed = append(inputParsed, lines...)
	}
	return f, inputParsed
}

func getLenToLeave(mapObjectPlaced map[Position]bool, playerPosition *Position, inputParsed []string) int {
	// set of visited position
	visited := make(map[Position]bool)
	direction := up
	isInside := true

	for index := 0; isInside; index++ {
		visited[*playerPosition] = true
		x, y := playerPosition.x, playerPosition.y
		if direction == up {
			y -= 1
		} else if direction == right {
			x += 1
		} else if direction == down {
			y += 1
		} else if direction == left {
			x -= 1
		}
		// check if the player is on the map
		if x < 0 || y < 0 || x >= len(inputParsed[0]) || y >= len(inputParsed) {
			isInside = false
			break
		}
		// check if the player is on an object
		if mapObjectPlaced[Position{x, y}] {
			direction = (direction + 1) % 4
			x, y = playerPosition.x, playerPosition.y
		}
		playerPosition.x = x
		playerPosition.y = y
		if index > 10000 {
			return -1
		}
	}
	return len(visited)
}

type Position struct {
	x int
	y int
}

type Direction int

const (
	up Direction = iota
	right
	down
	left
)
