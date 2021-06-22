package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	d, err := ioutil.ReadFile("8.txt")
	if err != nil {
		fmt.Println("Error loading file!", err)
		return
	}

	data := strings.Split(string(d), "\r\n")
	sub := 0
	for _, c := range data {
		sub += 2
		i := 0
		for i < len(c) {
			if string(c[i]) == "\\" {
				sub++
				i++
				if i < len(c) && c[i] == 'x' {
					sub += 2
					i += 2
				}
			}
			i++
		}
	}
	fmt.Println("Part1:", sub)

	add := 0
	for _, c := range data {
		add += 4 // 2 quotes, 2 backslash
		i := 0
		for i < len(c) {
			if string(c[i]) == "\\" ||
				(string(c[i]) == "\"" && i != 0 && i != len(c)-1) {
				add++
			}
			i++
		}
	}
	fmt.Println("Part2:", add)
}
