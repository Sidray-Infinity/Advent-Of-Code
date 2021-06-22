package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func hasThreeVowels(s string) bool {
	count := 0
	for _, c := range s {
		if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
			count += 1
		}
		if count >= 3 {
			return true
		}
	}
	return false
}

func pairOfTwo(s string) bool {
	for i := 0; i < len(s)-1; i++ {
		currPair := string(string(s[i]) + string(s[i+1]))
		if strings.Count(s, currPair) >= 2 {
			return true
		}
	}
	return false
}

func adjacentPair(s string) bool {
	for i := 0; i < len(s)-2; i++ {
		if s[i] == s[i+2] {
			return true
		}
	}
	return false
}

func hasTwiceAppear(s string) bool {
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			return true
		}
	}
	return false
}

func noGivenComb(s string) bool {
	return strings.Contains(s, "ab") || strings.Contains(s, "cd") || strings.Contains(s, "pq") || strings.Contains(s, "xy")
}

func isNice(s string) bool {
	return hasThreeVowels(s) && hasTwiceAppear(s) && !noGivenComb(s)
}

func isNice2(s string) bool {
	return pairOfTwo(s) && hasTwiceAppear(s)
}

func main() {
	d, err := ioutil.ReadFile("5.txt")
	if err != nil {
		fmt.Println("Error reading file!", err)
		return
	}
	dataString := string(d)
	count := 0
	var data []string = strings.Split(dataString, "\r\n")
	for _, line := range data {
		if isNice(line) {
			count++
		}
	}
	fmt.Println("Part1:", count)
	count = 0
	for _, line := range data {
		if isNice2(line) {
			count++
		}
	}
	fmt.Println("Part2:", count)

}
