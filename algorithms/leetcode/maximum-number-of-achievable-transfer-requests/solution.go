func max(i, j int) int {
    if i > j {
        return i
    }

    return j
}

func maximumRequests(n int, requests [][]int) int {
    indegree := make([]bool, len(requests))

    return f(n, 0, indegree, requests)
}


func f(n, start int, indegree []bool, requests [][]int) int {
    count := 0
    counter := make(map[int]int)

    for i := range indegree {
        if indegree[i] {
            counter[requests[i][0]]--
            counter[requests[i][1]]++
            count++
        }
    }

    for _, val := range counter {
        if val != 0 {
            count = 0
            break
        }
    }

    for i := start; i < len(requests); i++ {
        indegree[i] = true
        count = max(count, f(n, i+1, indegree, requests))
        indegree[i] = false
    }

    return count
}