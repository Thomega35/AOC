package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, inputParsed := mustOpenFile("input.txt")
	defer f.Close()

	pageBeforeToAfter := make(map[int][]int)
	listOfUpdates := [][]int{}

	customInputParsing(&inputParsed, &pageBeforeToAfter, &listOfUpdates)
	fmt.Println(pageBeforeToAfter)

	updateSum := 0

	for _, update := range listOfUpdates {
		updateSum += updateToNumber(pageBeforeToAfter, update)
		// fmt.Print(updateSum, " := ")
		// fmt.Println(update)
	}
	fmt.Println(updateSum)
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

func customInputParsing(inputParsed *[]string, pageBeforeToAfter *map[int][]int, listOfUpdates *[][]int) {
	firstpart := true
	// Parse the input
	for _, line := range *inputParsed {
		if len(line) == 0 {
			firstpart = false
			fmt.Println("done")
			continue
		}
		if firstpart {
			// Get the 2 numbers
			lineSeparated := strings.Split(line, "|")
			indexPageBefore, err1 := strconv.Atoi(string(lineSeparated[0]))
			indexPageAfter, err2 := strconv.Atoi(string(lineSeparated[1]))
			if err1 != nil || err2 != nil {
				fmt.Println("Error converting string to integer")
				return
			}
			// Add to the map
			(*pageBeforeToAfter)[indexPageBefore] = append((*pageBeforeToAfter)[indexPageBefore], indexPageAfter)
		} else {
			lineSeparated := strings.Split(line, ",")
			// parse int all elements
			update := make([]int, len(lineSeparated))
			for i, element := range lineSeparated {
				intElement, err := strconv.Atoi(element)
				if err != nil {
					fmt.Println("Error converting string to integer")
					return
				}
				update[i] = intElement
			}
			*listOfUpdates = append(*listOfUpdates, update)
		}
	}
}

func updateToNumber(pageBeforeToAfter map[int][]int, update []int) int {
	shouldAdd := false
	founded := true
	for founded {
		founded = doSwitch(pageBeforeToAfter, &update)
		if founded {
			shouldAdd = true
		}
	}
	if shouldAdd {
		fmt.Println("final -> ", update)
		fmt.Println()
		return update[len(update)/2]
	}
	return 0
}

func doSwitch(pageBeforeToAfter map[int][]int, update *[]int) bool {
	for indexCurrentPage, page := range *update {
		if len(pageBeforeToAfter[page]) == 0 {
			continue
		}
		for toCompareIndex := indexCurrentPage - 1; toCompareIndex >= 0; toCompareIndex-- {
			for _, pageAfter := range pageBeforeToAfter[page] {
				//put the pagebefore before the pageafter
				if pageAfter == (*update)[toCompareIndex] {
					fmt.Println("found", page, pageAfter, (*update)[toCompareIndex])
					//insert pagebefore before pageafter
					*update = append((*update)[:toCompareIndex], append([]int{page}, (*update)[toCompareIndex:]...)...)
					//remove pagebefore original
					fmt.Println("before -> ", *update, indexCurrentPage)
					*update = append((*update)[:indexCurrentPage+1], (*update)[indexCurrentPage+2:]...)
					fmt.Println("after -> ", *update)
					return true
				}
			}
		}
	}
	return false
}
