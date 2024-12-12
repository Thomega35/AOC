package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	f, inputParsed := mustOpenFile("input.txt")
	defer f.Close()
	fmt.Println(inputParsed)

	dotedLine := makeDotedLine(inputParsed)
	shifterLine := shiftDotedLine(dotedLine)
	checksm := calculateChecksum(shifterLine)
	fmt.Println(dotedLine)
	fmt.Println(shifterLine)
	fmt.Println(checksm)
}

func mustOpenFile(filename string) (*os.File, string) {
	f, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return nil, ""
	}

	inputParsed := ""
	// splitline
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		inputParsed = scanner.Text()
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return nil, ""
	}

	return f, inputParsed
}

func makeDotedLine(inputParsed string) []int {
	dotedLine := make([]int, 0)
	currentID := 0
	isNumber := true

	for i := 0; i < len(inputParsed); i++ {
		currentNumber, _ := strconv.Atoi(string(inputParsed[i]))

		if isNumber {
			for j := 0; j < currentNumber; j++ {
				dotedLine = append(dotedLine, currentID)
			}
			currentID++
		} else {
			for j := 0; j < currentNumber; j++ {
				dotedLine = append(dotedLine, -1)
			}
		}

		isNumber = !isNumber
	}
	return dotedLine
}

func shiftDotedLine(dotedLine []int) []int {
	shiftedLine := make([]int, len(dotedLine))
	copy(shiftedLine, dotedLine)
	for i := 0; i < len(dotedLine); i++ {
		if shiftedLine[i] == -1 {
			for j := len(dotedLine) - 1; j >= i; j-- {
				if shiftedLine[j] != -1 {
					if j == i {
						break
					}
					shiftedLine[i] = shiftedLine[j]
					shiftedLine[j] = -1
					break
				}
			}
		}
	}
	return shiftedLine
}

func calculateChecksum(shifterLine []int) int {
	checksum := 0

	for i := 0; i < len(shifterLine); i++ {
		if shifterLine[i] != -1 {
			temp := i * shifterLine[i]
			checksum += temp
		}
	}
	return checksum
}
