package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func mustOpenFile(filename string) (*os.File, [][]string) {
	f, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return nil, nil
	}

	inputParsed := [][]string{}
	// splitline
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		rawText := scanner.Text()
		// Process each line here
		// Split line into words
		lines := strings.Split(rawText, "\n")
		for _, line := range lines {
			words := strings.Fields(line)
			inputParsed = append(inputParsed, words)
		}

	}
	return f, inputParsed
}

// Helper function to calculate the absolute value
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
