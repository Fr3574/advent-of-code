package utils

import (
	"fmt"
	"os"
)

func ReadInput(path string) string {
	content, err := os.ReadFile(path)
	if err != nil {
		fmt.Println(err)
	}
	return string(content)
}
