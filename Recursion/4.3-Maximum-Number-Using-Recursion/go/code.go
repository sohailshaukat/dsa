package main

func maximum(arr []int) int {
	if len(arr) == 1 {
		return arr[0]
	}

	var current int = arr[0]

	var other int = maximum(arr[1:])

	if current < other {
		return other
	}

	return current

}

func main() {
	arr := []int{1, 2, 6, 4, 5}
	var max int = maximum(arr)

	println(max)
}
