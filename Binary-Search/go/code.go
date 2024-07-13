package main

import "fmt"

func search(arr []int, target int) int {

	var low int = 0
	var high int = len(arr) - 1

	for low <= high {
		var mid int = (low + high) / 2

		guess := arr[mid]

		if guess == target {
			return mid
		}
		if target < guess {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}

	return -1
}

func main() {
	arr := make([]int, 10)

	for i := 0; i < 10; i++ {
		arr[i] = i + 1
	}

	result := search(arr, 5)

	fmt.Printf("Element found at: %d\n", result)
}
