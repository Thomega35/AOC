package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, inputParsed := intOpenFile("input.txt")
	numberOfSafeReports := 0
	for _, report := range inputParsed {
		if safeUp(report) || safeDown(report) {
			numberOfSafeReports++
		}
	}
	fmt.Printf("There are %d safe reports\n", numberOfSafeReports)

	defer f.Close()
}

func intOpenFile(filename string) (*os.File, [][]int) {
	f, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return nil, nil
	}

	inputParsed := [][]int{}
	// splitline
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		rawText := scanner.Text()
		// Process each line here
		// Split line into words and convert to int
		lines := strings.Split(rawText, "\n")
		for _, line := range lines {
			words := strings.Fields(line)
			intWords := []int{}
			for _, word := range words {
				intWord, _ := strconv.Atoi(word)
				intWords = append(intWords, intWord)
			}
			inputParsed = append(inputParsed, intWords)
		}

	}
	return f, inputParsed
}

func safeUp(report []int) bool {
	last := report[0]
	for index := 1; index < len(report); index++ {
		if report[index] <= last || report[index] > last+3 {
			return false
		}
		last = report[index]
	}
	return true
}

func safeDown(report []int) bool {
	last := report[0]
	for index := 1; index < len(report); index++ {
		if report[index] >= last || report[index] < last-3 {
			return false
		}
		last = report[index]
	}
	return true
}
