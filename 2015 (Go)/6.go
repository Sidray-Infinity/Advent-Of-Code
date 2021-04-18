package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

func updateGrid(grid [][]int, value int, toogle bool, x0 int, y0 int, x1 int, y1 int) {
	for i := x0; i <= x1; i++ {
		for j := y0; j <= y1; j++ {
			if toogle {
				if grid[i][j] == 0 {
					grid[i][j] = 1
				} else {
					grid[i][j] = 0
				}

			} else {
				grid[i][j] = value
			}
		}
	}
}

func updateGrid2(grid [][]int, value int, toogle bool, x0 int, y0 int, x1 int, y1 int) {
	for i := x0; i <= x1; i++ {
		for j := y0; j <= y1; j++ {
			if toogle {
				grid[i][j] += 2
			} else {
				grid[i][j] += value
				grid[i][j] = int(math.Max(0.0, float64(grid[i][j])))
			}
		}
	}
}

func main() {
	grid := make([][]int, 1000)
	var lineData []string
	for i := range grid {
		grid[i] = make([]int, 1000)
	}

	d, err := ioutil.ReadFile("6.txt")
	if err != nil {
		fmt.Println("Error reading file!", err)
		return
	}
	data := strings.Split(string(d), "\r\n")
	var x0, x1, y0, y1 int
	for _, line := range data {
		lineData = strings.Split(string(line), " ")
		if lineData[0] == "turn" {
			x0, _ = strconv.Atoi(strings.Split(lineData[2], ",")[0])
			y0, _ = strconv.Atoi(strings.Split(lineData[2], ",")[1])
			x1, _ = strconv.Atoi(strings.Split(lineData[4], ",")[0])
			y1, _ = strconv.Atoi(strings.Split(lineData[4], ",")[1])
			if lineData[1] == "on" {
				updateGrid(grid, 1, false, x0, y0, x1, y1)
			} else {
				updateGrid(grid, 0, false, x0, y0, x1, y1)
			}
		} else {
			x0, _ = strconv.Atoi(strings.Split(lineData[1], ",")[0])
			y0, _ = strconv.Atoi(strings.Split(lineData[1], ",")[1])
			x1, _ = strconv.Atoi(strings.Split(lineData[3], ",")[0])
			y1, _ = strconv.Atoi(strings.Split(lineData[3], ",")[1])
			updateGrid(grid, -1, true, x0, y0, x1, y1)
		}
	}
	count := 0
	for i := 0; i < 1000; i++ {
		for j := 0; j < 1000; j++ {
			if grid[i][j] == 1 {
				count++
			}
		}
	}
	fmt.Println("Part1:", count)
	grid = make([][]int, 1000)
	for i := range grid {
		grid[i] = make([]int, 1000)
	}
	for _, line := range data {
		lineData = strings.Split(string(line), " ")
		if lineData[0] == "turn" {
			x0, _ = strconv.Atoi(strings.Split(lineData[2], ",")[0])
			y0, _ = strconv.Atoi(strings.Split(lineData[2], ",")[1])
			x1, _ = strconv.Atoi(strings.Split(lineData[4], ",")[0])
			y1, _ = strconv.Atoi(strings.Split(lineData[4], ",")[1])
			if lineData[1] == "on" {
				updateGrid2(grid, 1, false, x0, y0, x1, y1)
			} else {
				updateGrid2(grid, -1, false, x0, y0, x1, y1)
			}
		} else {
			x0, _ = strconv.Atoi(strings.Split(lineData[1], ",")[0])
			y0, _ = strconv.Atoi(strings.Split(lineData[1], ",")[1])
			x1, _ = strconv.Atoi(strings.Split(lineData[3], ",")[0])
			y1, _ = strconv.Atoi(strings.Split(lineData[3], ",")[1])
			updateGrid2(grid, -1, true, x0, y0, x1, y1)
		}
	}
	count = 0
	for i := 0; i < 1000; i++ {
		for j := 0; j < 1000; j++ {
			count += grid[i][j]
		}
	}
	fmt.Println("Part2:", count)
}
