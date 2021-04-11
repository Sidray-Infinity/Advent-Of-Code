package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

func main() {
	data, err := ioutil.ReadFile("2.txt")
	if err != nil {
		fmt.Println("Error while reading input file!")
		return
	}

	Data := string(data)
	splittedData := strings.Split(Data, "\r\n")
	count := 0
	for _, box := range splittedData {
		dims := strings.Split(box, "x")

		a, _ := strconv.ParseInt(dims[0], 10, 64)
		b, _ := strconv.ParseInt(dims[1], 10, 64)
		c, _ := strconv.ParseInt(dims[2], 10, 64)

		count += int(2 * (a*b + b*c + c*a))
		count += int(math.Min(math.Min(float64(a*b), float64(b*c)), float64(a*c)))
	}
	fmt.Println("Part1:", count)

	count = 0
	for _, box := range splittedData {
		dims := strings.Split(box, "x")

		a, _ := strconv.ParseInt(dims[0], 10, 64)
		b, _ := strconv.ParseInt(dims[1], 10, 64)
		c, _ := strconv.ParseInt(dims[2], 10, 64)

		count += int(math.Min(math.Min(float64(2*(a+b)), float64(2*(b+c))), float64(2*(a+c))))
		count += int(a * b * c)
	}
	fmt.Println("Part2:", count)
}
