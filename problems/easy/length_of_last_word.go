import (
    "fmt"
    "strings"
)

func lengthOfLastWord(s string) int {
    w := strings.Split(strings.TrimRight(s, " "), " ")
    return len(w[len(w)-1])
}