package main

import (
	"fmt"
	"strconv"
	"strings"
)

func iterator(x string, n int) int {
	for i := 0; i < n; i++ {
		count := 1
		currNum := x[0]
		var res []string
		for j := 1; j < len(x); j++ {
			if x[j] != currNum {
				res = append(res, strconv.Itoa(count))
				res = append(res, string(currNum))
				currNum = x[j]
				count = 1

				if j == len(x)-1 {
					res = append(res, strconv.Itoa(count))
					res = append(res, string(currNum))
				}

			} else {
				count++
			}
		}
		x = strings.Join(res, "")
	}
	return len(x)
}

func main() {
	x := "1113222113"
	fmt.Println("Part1:", iterator(x, 40))
	fmt.Println("Part2:", iterator(x, 50))
}
