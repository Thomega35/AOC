package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	f, inputParsed := mustOpenFile("test.txt")
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
	valOfGroup := -1
	numberInGroup := 0
	for i := len(shiftedLine) - 1; i >= 0; i-- {
		if shiftedLine[i] != -1 && valOfGroup == -1 {
			valOfGroup = shiftedLine[i]
			numberInGroup = 1
		} else if shiftedLine[i] == -1 && valOfGroup != -1 {
			shiftLeftGroup(shiftedLine, i, numberInGroup, valOfGroup)
			valOfGroup = -1
			numberInGroup = 0
		} else if shiftedLine[i] == valOfGroup {
			numberInGroup++
		} else if shiftedLine[i] != valOfGroup && valOfGroup != -1 {
			shiftLeftGroup(shiftedLine, i, numberInGroup, valOfGroup)
			valOfGroup = shiftedLine[i]
			numberInGroup = 1
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

func shiftLeftGroup(shiftedLine []int, indexPattern int, numberInGroup int, valOfGroup int) {
	lengthOfMinusOneGroup := 0
	for i := 0; i < indexPattern; i++ {
		if shiftedLine[i] == -1 {
			lengthOfMinusOneGroup++
		} else {
			if lengthOfMinusOneGroup == 0 {
				continue
			} else if lengthOfMinusOneGroup >= numberInGroup {
				fmt.Println("Swap", lengthOfMinusOneGroup, "-1", i, numberInGroup, valOfGroup)
				for j := i - lengthOfMinusOneGroup; j < (i-lengthOfMinusOneGroup)+numberInGroup; j++ {
					shiftedLine[j] = valOfGroup
				}
				for j := indexPattern + 1; j < indexPattern+numberInGroup+1; j++ {
					shiftedLine[j] = -1
				}
				return
			}
			lengthOfMinusOneGroup = 0
		}
	}
}
