package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

type Graph map[string]map[string]int

func allVisited(visited map[string]bool) bool {
	for k := range visited {
		if visited[k] == false {
			return false
		}
	}
	return true
}

func tsp(graph Graph, visited map[string]bool, currNode string, globalValue *int, currValue int, calculatingMax bool) {
	if visited[currNode] {
		return
	}
	newVisited := make(map[string]bool)
	for k := range visited {
		newVisited[k] = visited[k]
	}
	newVisited[currNode] = true
	if allVisited(newVisited) {
		if calculatingMax {
			*globalValue = int(math.Max(float64(*globalValue), float64(currValue)))
		} else {
			*globalValue = int(math.Min(float64(*globalValue), float64(currValue)))
		}
		return
	}

	neighbours := graph[currNode]
	for n, v := range neighbours {
		tsp(graph, newVisited, n, globalValue, currValue+v, calculatingMax)
	}
}

func main() {
	// Travelling Salesman Problem (Directed Graph)

	d, _ := ioutil.ReadFile("9.txt")
	data := strings.Split(string(d), "\r\n")
	graph := make(Graph)
	visited := make(map[string]bool)
	for _, line := range data {
		lineData := strings.Split(line, " = ")
		nodes := strings.Split(lineData[0], " to ")
		if graph[nodes[0]] == nil {
			graph[nodes[0]] = make(map[string]int)
		}
		if graph[nodes[1]] == nil {
			graph[nodes[1]] = make(map[string]int)
		}
		graph[nodes[0]][nodes[1]], _ = strconv.Atoi(lineData[1])
		graph[nodes[1]][nodes[0]], _ = strconv.Atoi(lineData[1])
		visited[nodes[0]] = false
		visited[nodes[1]] = false
	}
	minValue := math.MaxInt64
	for city := range visited {
		for k := range visited {
			visited[k] = false
		}
		tsp(graph, visited, city, &minValue, 0, false)
	}
	fmt.Println("Part1:", minValue)

	maxValue := math.MinInt64
	for city := range visited {
		for k := range visited {
			visited[k] = false
		}
		tsp(graph, visited, city, &maxValue, 0, true)
	}
	fmt.Println("Part2:", maxValue)
}
