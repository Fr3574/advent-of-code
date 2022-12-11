package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"

	"github.com/Fr3574/advent-of-code/utils"
)

func groupCalories(input string) []int {
	strings := strings.Split(input+"\n", "\n")
	var res []int
	sum := 0
	for _, element := range strings {
		if element == "" {
			res = append(res, sum)
			sum = 0
		} else {
			number, err := strconv.ParseUint(element, 10, 32)
			if err != nil {
				fmt.Println(err)
			}
			sum += int(number)
		}
	}
	return res
}

func getSumOfHighestCalories(size int, sortedSlice []int) int {
	sum := 0
	for _, elm := range sortedSlice[len(sortedSlice)-size:] {
		sum += elm
	}
	return sum
}

func main() {
	input := utils.ReadInput("input.txt")
	calories := groupCalories(input)
	sort.Ints(calories)
	fmt.Println(getSumOfHighestCalories(1, calories))
	fmt.Println(getSumOfHighestCalories(3, calories))
}
