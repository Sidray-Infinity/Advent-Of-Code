/*
DROPING FOR NOW AS I DONT LIKE THE QUESTION ... AND IT'S HARD
*/

package main

import (
	"io/ioutil"
	"strconv"
	"strings"
)

type prop struct {
	capacity   int
	durability int
	flavor     int
	texture    int
	calories   int
}

func main() {
	d, _ := ioutil.ReadFile("15.txt")
	lines := strings.Split(string(d), "\n")
	data := make(map[string]prop)
	for _, line := range lines {
		ignr := strings.Split(line, ": ")
		prop_eles := strings.Split(ignr[1], ", ")
		pr := prop{}
		pr.capacity, _ = strconv.Atoi(strings.Split(prop_eles[0], " ")[1])
		pr.durability, _ = strconv.Atoi(strings.Split(prop_eles[1], " ")[1])
		pr.flavor, _ = strconv.Atoi(strings.Split(prop_eles[2], " ")[1])
		pr.texture, _ = strconv.Atoi(strings.Split(prop_eles[3], " ")[1])
		pr.calories, _ = strconv.Atoi(strings.Split(prop_eles[4], " ")[1])
		data[ignr[0]] = pr
	}

}
