package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

func permutations(arr []string) [][]string {
	var helper func([]string, int)
	res := [][]string{}

	helper = func(arr []string, n int) {
		if n == 1 {
			tmp := make([]string, len(arr))
			copy(tmp, arr)
			res = append(res, tmp)
		} else {
			for i := 0; i < n; i++ {
				helper(arr, n-1)
				if n%2 == 1 {
					tmp := arr[i]
					arr[i] = arr[n-1]
					arr[n-1] = tmp
				} else {
					tmp := arr[0]
					arr[0] = arr[n-1]
					arr[n-1] = tmp
				}
			}
		}
	}
	helper(arr, len(arr))
	return res
}

func calc(perm []string, data map[string]map[string]int) int {
	sum := 0
	for idx, val := range perm {
		if idx == 0 {
			sum += data[val][perm[len(perm)-1]]
			sum += data[val][perm[idx+1]]
		} else if idx == len(perm)-1 {
			sum += data[val][perm[0]]
			sum += data[val][perm[idx-1]]
		} else {
			sum += data[val][perm[idx+1]]
			sum += data[val][perm[idx-1]]
		}
	}
	return sum
}

func main() {
	d, _ := ioutil.ReadFile("13.txt")
	lines := strings.Split(string(d), "\r\n")
	data := make(map[string]map[string]int)
	for _, l := range lines {
		words := strings.Split(l, " ")
		t := words[2]
		value, _ := strconv.Atoi(words[3])
		from := words[0]
		to := words[10][:len(words[10])-1]
		if t == "lose" {
			value *= -1
		}
		if data[from] == nil {
			data[from] = make(map[string]int)
		}
		data[from][to] = value
	}
	people := make([]string, 0, len(data))
	for p := range data {
		people = append(people, p)
	}
	maxHap := math.MinInt64
	for _, perm := range permutations(people) {
		hap := calc(perm, data)
		if hap > maxHap {
			maxHap = hap
		}
	}

	fmt.Println("Part1:", maxHap)

	data["me"] = make(map[string]int)
	for _, p := range people {
		data["me"][p] = 0
		data[p]["me"] = 0
	}
	people = append(people, "me")
	maxHap = math.MinInt64
	for _, perm := range permutations(people) {
		hap := calc(perm, data)
		if hap > maxHap {
			maxHap = hap
		}
	}
	fmt.Println("Part2:", maxHap)
}
