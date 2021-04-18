package main

import (
	"fmt"
	"io/ioutil"
)

type pos struct {
	x int
	y int
}

func main() {
	data, err := ioutil.ReadFile("3.txt")
	if err != nil {
		fmt.Println("Cannot read file!")
		return
	}

	set := map[pos]struct{}{}
	currPos := pos{0, 0}
	set[currPos] = struct{}{}
	var stringData string = string(data)

	for _, c := range stringData {
		if c == '^' {
			currPos.y += 1
		} else if c == '>' {
			currPos.x += 1
		} else if c == '<' {
			currPos.x -= 1
		} else {
			currPos.y -= 1
		}
		set[currPos] = struct{}{}
	}
	fmt.Println("Part1:", len(set))

	santaSet := map[pos]struct{}{}
	roboSantaSet := map[pos]struct{}{}

	currSantaPos := pos{0, 0}
	currRoboSantaPos := pos{0, 0}

	santaSet[currSantaPos] = struct{}{}
	roboSantaSet[currRoboSantaPos] = struct{}{}

	for i, c := range stringData {
		if c == '^' {
			if i%2 == 0 {
				currSantaPos.y += 1
			} else {
				currRoboSantaPos.y += 1
			}
		} else if c == '>' {
			if i%2 == 0 {
				currSantaPos.x += 1
			} else {
				currRoboSantaPos.x += 1
			}
		} else if c == '<' {
			if i%2 == 0 {
				currSantaPos.x -= 1
			} else {
				currRoboSantaPos.x -= 1
			}
		} else {
			if i%2 == 0 {
				currSantaPos.y -= 1
			} else {
				currRoboSantaPos.y -= 1
			}
		}
		if i%2 == 0 {
			santaSet[currSantaPos] = struct{}{}
		} else {
			roboSantaSet[currRoboSantaPos] = struct{}{}
		}
	}
	commonPos := 0
	for k, _ := range santaSet {
		_, exists := roboSantaSet[k]
		if exists {
			commonPos += 1
		}
	}

	fmt.Println("Part2:", len(santaSet)+len(roboSantaSet)-commonPos)
}
