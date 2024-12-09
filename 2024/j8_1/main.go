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

	mapAntenna := make(map[string][]Position)

	for indexC, line := range inputParsed {
		fmt.Println("line", line)
		for indexL, char := range line {
			if char != '.' {
				mapAntenna[string(char)] = append(mapAntenna[string(char)], Position{indexL, indexC})
			}
		}
	}

	setAntiNode := make(map[Position]bool)
	for _, antenna := range mapAntenna {
		for _, pos := range antenna {
			for _, pos2 := range antenna {
				if pos != pos2 {
					fmt.Println("pos", pos, "pos2", pos2)
					diffX := pos.x - pos2.x
					diffY := pos.y - pos2.y
					fmt.Println("diffX", diffX, "diffY", diffY)
					antiNodePos1 := Position{pos.x + diffX, pos.y + diffY}
					antiNodePos2 := Position{pos2.x - diffX, pos2.y - diffY}
					fmt.Println("antiNodePos1", antiNodePos1, "antiNodePos2", antiNodePos2)
					if _, ok := setAntiNode[antiNodePos1]; !ok && antiNodePos1.x >= 0 && antiNodePos1.y >= 0 && antiNodePos1.x < len(inputParsed[0]) && antiNodePos1.y < len(inputParsed) {
						setAntiNode[antiNodePos1] = true
					}
					if _, ok := setAntiNode[antiNodePos2]; !ok && antiNodePos2.x >= 0 && antiNodePos2.y >= 0 && antiNodePos2.x < len(inputParsed[0]) && antiNodePos2.y < len(inputParsed) {
						setAntiNode[antiNodePos2] = true
					}
				}
			}
		}
		fmt.Println()
	}
	for indexC, line := range inputParsed {
		for indexL, char := range line {
			if _, ok := setAntiNode[Position{indexL, indexC}]; ok {
				fmt.Print("#")
			} else {
				fmt.Print(string(char))
			}
		}
		fmt.Println()
	}
	fmt.Println(mapAntenna)
	fmt.Println("length", len(inputParsed), len(inputParsed[0]))
	fmt.Println("setAntiNode", setAntiNode)
	fmt.Println("len of setAntiNode", len(setAntiNode))
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

type Position struct {
	x int
	y int
}
