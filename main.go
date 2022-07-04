package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.Stat("test.txt")

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("File Name:", file.Name())
	fmt.Println("File Size:", file.Size())
	fmt.Println("Last Modified:", file.ModTime())
	fmt.Println("Is Directory:", file.IsDir())
}
