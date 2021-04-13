package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
)

func main() {
	count := 1
	var hash [16]byte
	var hexString string
	for true {
		secretKey := []byte("yzbqklnj" + strconv.Itoa(count))
		hash = md5.Sum(secretKey)
		hexString = hex.EncodeToString(hash[:])
		if hexString[:5] == "00000" {
			fmt.Println("Part1:", count)
			break
		}
		count += 1
	}
	count = 0
	for true {
		secretKey := []byte("yzbqklnj" + strconv.Itoa(count))
		hash = md5.Sum(secretKey)
		hexString = hex.EncodeToString(hash[:])
		if hexString[:6] == "000000" {
			fmt.Println("Part2:", count)
			break
		}
		count += 1
	}
}
