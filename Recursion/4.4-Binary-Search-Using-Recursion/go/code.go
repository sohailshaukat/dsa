package main

import "fmt"

func search(arr []int, target int) int {

	length := len(arr)

	if length == 0 {
		return -1
	}

	var mid int = (length - 1) / 2
	var guess int = arr[mid]

	if guess == target {
		return mid
	}
	if target < guess {
		position := search(arr[:mid], target)
		if position == -1 {
			return -1
		}
		return position
	} else {
		position := search(arr[mid+1:], target)
		if position == -1 {
			return -1
		}
		return mid + 1 + position
	}

}

func main() {
	arr := make([]int, 10)

	for i := 0; i < 10; i++ {
		arr[i] = i + 1
	}

	for i := 10; i > 0; i-- {
		result := search(arr, i)

		fmt.Printf("%d found at: %d\n", i, result)
	}
}
