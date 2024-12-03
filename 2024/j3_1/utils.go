package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

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
