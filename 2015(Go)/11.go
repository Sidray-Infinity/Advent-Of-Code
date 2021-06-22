package main

import "fmt"

func hasIncreasingStraight(password [8]byte) bool {
	for i := 3; i < 8; i++ {
		if password[i] == password[i-1]+1 && password[i] == password[i-2]+2 {
			return true
		}
	}
	return false
}

func hasNoInvalidLetters(password [8]byte) bool {
	for i := 0; i < 8; i++ {
		if password[i] == byte(int('i')) || password[i] == byte(int('l')) || password[i] == byte(int('o')) {
			return false
		}
	}
	return true
}

func hasPairs(password [8]byte) bool {
	currPair := 0
	i := 1
	for i < 8 {
		if password[i] == password[i-1] {
			if currPair >= 97 {
				return true
			} else {
				currPair = int(password[i])
				i += 2
			}
		} else {
			i++
		}
	}
	return false
}

func isValid(password [8]byte) bool {
	return hasIncreasingStraight(password) && hasNoInvalidLetters(password) && hasPairs(password)
}

func increment(password string, newPassword *[8]byte) {
	idx := 7
	for i := 0; i < 8; i++ {
		(*newPassword)[i] = password[i]
	}

	for idx >= 0 {
		(*newPassword)[idx] += 1
		if (*newPassword)[idx] > 122 {
			(*newPassword)[idx] = 97
			idx--
		} else {
			break
		}
	}
}

func main() {
	currPassword := "hxbxwxba"
	var newPassword [8]byte

	increment(currPassword, &newPassword)
	for !isValid(newPassword) {
		increment(string(newPassword[:]), &newPassword)
	}
	fmt.Println("Part1:", string(newPassword[:]))

	increment(string(newPassword[:]), &newPassword)
	for !isValid(newPassword) {
		increment(string(newPassword[:]), &newPassword)
	}
	fmt.Println("Part2:", string(newPassword[:]))
}
