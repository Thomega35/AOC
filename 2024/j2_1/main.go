package main

import (
	"fmt"
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
