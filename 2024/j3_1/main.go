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
	multList := []string{}
	for _, line := range inputParsed {
		r := regexp.MustCompile(`mul\(\d+,\d+\)`)
		multList = append(multList, r.FindAllString(line, -1)...)
	}
	fmt.Println("Mult list:", multList)
	// Sum the result
	multRes := 0
	for _, mult := range multList {
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
