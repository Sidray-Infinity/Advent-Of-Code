package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"reflect"
)

func pj(x interface{}, sum *int) {
	if reflect.TypeOf(x).String() == "[]interface {}" {
		for _, v := range x.([]interface{}) {
			pj(v, sum)
		}
	} else if reflect.TypeOf(x).String() == "map[string]interface {}" {
		t := x.(map[string]interface{})
		for k := range x.(map[string]interface{}) {
			pj(t[k], sum)
		}

	} else if reflect.TypeOf(x).String() == "float64" {
		*sum += int(x.(float64))
	}
}

func pj2(x interface{}, sum *int) {
	if reflect.TypeOf(x).String() == "[]interface {}" {
		for _, v := range x.([]interface{}) {
			pj2(v, sum)
		}
	} else if reflect.TypeOf(x).String() == "map[string]interface {}" {
		t := x.(map[string]interface{})
		for _, v := range t {
			if v == "red" {
				return
			}
		}
		for k := range t {
			pj2(t[k], sum)
		}

	} else if reflect.TypeOf(x).String() == "float64" {
		*sum += int(x.(float64))
	}
}

func main() {
	data, _ := ioutil.ReadFile("12.json")
	var store interface{}
	json.Unmarshal(data, &store)
	sum := 0
	pj(store, &sum)
	fmt.Println("Part1:", sum)
	sum = 0
	pj2(store, &sum)
	fmt.Println("Part2:", sum)
}
