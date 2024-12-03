// open j1.txt
package main

import (
	"fmt"
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
