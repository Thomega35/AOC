package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	f, inputParsed := mustOpenFile("input.txt")
	// Parse the mul()
	multListUnSorted := []string{}
	for _, line := range inputParsed {
		r := regexp.MustCompile(`mul\(\d+,\d+\)|do\(\)|don't\(\)`)
		multListUnSorted = append(multListUnSorted, r.FindAllString(line, -1)...)
	}
	fmt.Println("Mult list UnSorted:", multListUnSorted)
	// Sort the mult
	multListSorted := []string{}
	isDoOn := true
	for _, mult := range multListUnSorted {
		if strings.Contains(mult, "do()") {
			isDoOn = true
		} else if strings.Contains(mult, "don't()") {
			isDoOn = false
		} else if isDoOn {
			multListSorted = append(multListSorted, mult)
		}
	}
	fmt.Println("Mult list Sorted:", multListSorted)
	// Sum the result
	multRes := 0
	for _, mult := range multListSorted {
		numberWithComma := mult[4 : len(mult)-1]
		numbersToMult := strings.Split(numberWithComma, ",")
		num1, _ := strconv.Atoi(numbersToMult[0])
		num2, _ := strconv.Atoi(numbersToMult[1])
		multRes += num1 * num2
	}
	fmt.Printf("The result is: %d\n", multRes)

	defer f.Close()
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
		inputParsed = append(inputParsed, strings.Split(rawText, "\n")...)

	}
	return f, inputParsed
}
