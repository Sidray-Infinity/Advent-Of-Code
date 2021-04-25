package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type opFunc func(ops ...int) int

type LHS struct {
	op1 string
	op  string
	op2 string
}

func populateLhs(op1 string, op string, op2 string, lhs *LHS) {
	lhs.op1 = strings.Trim(op1, " ")
	lhs.op = strings.Trim(op, " ")
	lhs.op2 = strings.Trim(op2, " ")
}

func funcMapper(operation string) opFunc {
	switch operation {
	case "AND":
		return func(ops ...int) int {
			return ops[0] & ops[1]
		}
	case "OR":
		return func(ops ...int) int {
			return ops[0] | ops[1]
		}
	case "RSHIFT":
		return func(ops ...int) int {
			return ops[0] >> ops[1]
		}
	case "LSHIFT":
		return func(ops ...int) int {
			return ops[0] << ops[1]
		}
	default:
		return func(ops ...int) int {
			return ops[0]
		}
	}
}

func solve(circuitMap map[string]LHS, target string) int {
	if isNumber(target) {
		res, _ := strconv.Atoi(target)
		return res
	}
	var lhs LHS = circuitMap[target]
	if numEleActive(lhs) == 1 {
		// LHS is either integer, or another state (no operation)
		res := solve(circuitMap, lhs.op1)
		lhs.op1 = strconv.Itoa(res)
		lhs.op = ""
		lhs.op2 = ""
		circuitMap[target] = lhs
		return res
	} else if numEleActive(lhs) == 2 {
		// NOT statement
		res := solve(circuitMap, lhs.op1)
		lhs.op1 = strconv.Itoa(^res)
		lhs.op = ""
		lhs.op2 = ""
		circuitMap[target] = lhs
		return ^res
	} else {
		// 3 element statement
		op1 := solve(circuitMap, lhs.op1)
		op2 := solve(circuitMap, lhs.op2)
		res := funcMapper(lhs.op)(op1, op2)
		lhs.op1 = strconv.Itoa(res)
		lhs.op = ""
		lhs.op2 = ""
		circuitMap[target] = lhs
		return res
	}
}

func numEleActive(lhs LHS) int {
	count := 0
	if len(lhs.op1) > 0 {
		count++
	}
	if len(lhs.op) > 0 {
		count++
	}
	if len(lhs.op2) > 0 {
		count++
	}
	return count
}

func isNumber(num string) bool {
	if _, err := strconv.Atoi(num); err == nil {
		return true
	}
	return false
}

func main() {
	d, err := ioutil.ReadFile("7.txt")
	if err != nil {
		fmt.Println("Error loading file!", err)
		return
	}

	data := strings.Split(string(d), "\r\n")

	circuitMap := make(map[string]LHS)
	newCircuitMap := make(map[string]LHS)
	// Populate circuitMap
	for _, line := range data {
		lineData := strings.Split(line, " -> ")
		lhsData := strings.Split(string(lineData[0]), " ")
		var lhs LHS
		if len(lhsData) == 1 {
			populateLhs(lhsData[0], "", "", &lhs)
		} else if len(lhsData) == 2 {
			populateLhs(lhsData[1], lhsData[0], "", &lhs)
		} else {
			populateLhs(lhsData[0], lhsData[1], lhsData[2], &lhs)
		}
		circuitMap[lineData[1]] = lhs
	}

	for k, v := range circuitMap {
		newCircuitMap[k] = v
	}

	signalA := solve(circuitMap, "a")
	fmt.Println("Part1:", signalA)

	lhs := LHS{strconv.Itoa(signalA), "", ""}
	newCircuitMap["b"] = lhs

	fmt.Println("Part2:", solve(newCircuitMap, "a"))
}
