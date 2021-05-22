package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type rd struct {
	speed       int
	stamina     int
	currStamina int
	rest        int
	currRest    int
	dist        int
	resting     bool
	points      int
}

func main() {
	d, _ := ioutil.ReadFile("14.txt")
	lines := strings.Split(string(d), "\r\n")
	var data []rd

	for _, line := range lines {
		words := strings.Split(line, " ")
		r := rd{}
		r.speed, _ = strconv.Atoi(words[3])
		r.stamina, _ = strconv.Atoi(words[6])
		r.rest, _ = strconv.Atoi(words[13])
		r.currStamina = r.stamina
		data = append(data, r)
	}

	for i := 0; i < 2503; i++ {
		for idx, r := range data {
			if r.resting {
				r.currRest += 1
				if r.currRest == r.rest {
					r.resting = false
					r.currRest = 0
				}
			} else {
				r.dist += r.speed
				r.currStamina -= 1
				if r.currStamina == 0 {
					r.resting = true
					r.currStamina = r.stamina
				}
			}
			data[idx] = r
		}
	}
	maxD := 0
	for _, r := range data {
		if r.dist > maxD {
			maxD = r.dist
		}
	}
	fmt.Println("Part1:", maxD)

	// reset
	for idx, r := range data {
		data[idx].currRest = 0
		data[idx].currStamina = r.stamina
		data[idx].resting = false
		data[idx].dist = 0
	}

	maxD = 0
	for i := 0; i < 2503; i++ {
		for idx, r := range data {
			if r.resting {
				r.currRest += 1
				if r.currRest == r.rest {
					r.resting = false
					r.currRest = 0
				}
			} else {
				r.dist += r.speed
				if r.dist > maxD {
					maxD = r.dist
				}
				r.currStamina -= 1
				if r.currStamina == 0 {
					r.resting = true
					r.currStamina = r.stamina
				}
			}
			data[idx] = r
		}
		for idx, r := range data {
			if r.dist == maxD {
				r.points += 1
			}
			data[idx] = r
		}
	}

	maxP := 0
	for _, r := range data {
		if r.points > maxP {
			maxP = r.points
		}
	}
	fmt.Println("Part2:", maxP)
}
