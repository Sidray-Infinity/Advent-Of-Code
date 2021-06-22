package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func getAuntMap(line string) (int, map[string]int) {
	values := strings.SplitN(line, ": ", 2) // Stupidest shit in go
	props := make(map[string]int)
	for _, ele := range strings.Split(values[1], ", ") {
		vs := strings.Split(ele, ": ")
		props[vs[0]], _ = strconv.Atoi(vs[1])
	}
	auntNo, _ := strconv.Atoi(strings.Split(values[0], " ")[1])
	return auntNo, props
}

func main() {
	var recv string = "children: 3\ncats: 7\nsamoyeds: 2\npomeranians: 3\nakitas: 0\nvizslas: 0\ngoldfish: 5\ntrees: 3\ncars: 2\nperfumes: 1"

	ideal := make(map[string]int)
	for _, idealLines := range strings.Split(recv, "\n") {
		values := strings.Split(idealLines, ": ")
		ideal[values[0]], _ = strconv.Atoi(values[1])
	}

	d, _ := ioutil.ReadFile("16.txt")
	lines := strings.Split(string(d), "\n")
	rightAunt := 0
	for _, line := range lines {
		auntNo, props := getAuntMap(line)
		flag := true
		for k, v := range props {
			if v != ideal[k] {
				flag = false
				break
			}
		}
		if flag {
			rightAunt = auntNo
			break
		}
	}
	fmt.Println("Part1:", rightAunt)

	rightAunt = 0
	for _, line := range lines {
		auntNo, props := getAuntMap(line)
		flag := true
		for k, v := range props {
			if k == "cats" || k == "trees" {
				if v <= ideal[k] {
					flag = false
					break
				}
			} else if k == "pomeranians" || k == "goldfish" {
				if v >= ideal[k] {
					flag = false
					break
				}
			} else {
				if v != ideal[k] {
					flag = false
					break
				}
			}
		}
		if flag {
			rightAunt = auntNo
			break
		}
	}
	fmt.Println("Part2:", rightAunt)

}
