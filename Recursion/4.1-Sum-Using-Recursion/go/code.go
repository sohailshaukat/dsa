package main

func sum(arr []int) int {
	if len(arr) == 0 {
		return 0
	}

	return arr[0] + sum(arr[1:])

}

func main() {
	arr := []int{1, 2, 3, 4}

	println(sum(arr))

}
