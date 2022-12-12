package main

import (
	"fmt"
	"strings"

	"github.com/Fr3574/advent-of-code/utils"
)

func getShapesScore(char byte) int {
	switch char {
	case 'Y':
		return 2
	case 'X':
		return 1
	case 'Z':
		return 3
	}
	return 0
}

func getRoundsScore(game string) int {
	if (game[0] == 'A' && game[2] == 'Y') || (game[0] == 'B' && game[2] == 'Z') || (game[0] == 'C' && game[2] == 'X') {
		return 6
	} else if (game[0] == 'A' && game[2] == 'X') || (game[0] == 'B' && game[2] == 'Y') || (game[0] == 'C' && game[2] == 'Z') {
		return 3
	} else {
		return 0
	}
}

func getHighestScore(input string) int {
	strings := strings.Split(input, "\n")
	score := 0
	for _, el := range strings {
		score += getRoundsScore(el) + getShapesScore(el[2])
	}
	return score
}

func getShape(game string) byte {
	if game[2] == 'Y' {
		switch game[0] {
		case 'A':
			return 'X'
		case 'B':
			return 'Y'
		default:
			return 'Z'
		}
	} else if game[2] == 'X' {
		switch game[0] {
		case 'A':
			return 'Z'
		case 'B':
			return 'X'
		default:
			return 'Y'
		}
	} else {
		switch game[0] {
		case 'A':
			return 'Y'
		case 'B':
			return 'Z'
		default:
			return 'X'
		}
	}
}

func getOptimalScore(input string) int {
	strings := strings.Split(input, "\n")
	score := 0
	for _, el := range strings {
		optimalGame := el[:2] + string(getShape(el))
		score += getRoundsScore(optimalGame) + getShapesScore(optimalGame[2])
	}
	return score
}

func main() {
	input := utils.ReadInput("input.txt")
	score := getHighestScore(input)
	fmt.Println(score)
	fmt.Println(getOptimalScore(input))
}
