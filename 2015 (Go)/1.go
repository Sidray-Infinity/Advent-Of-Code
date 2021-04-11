package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	data, err := ioutil.ReadFile("1.txt")
	if err != nil {
		fmt.Println("Error while reading file!", err)
		return
	}
	var count = 0
	for _, c := range string(data) {
		if string(c) == "(" {
			count++
		} else {
			count--
		}
	}
	fmt.Println("Part1:", count)

	count = 0
	for i, c := range string(data) {
		if string(c) == "(" {
			count++
		} else {
			count--
		}
		if count == -1 {
			fmt.Println("Part2:", i+1)
			break
		}
	}

}
