import (
    "fmt"
    "strings"
)

func longestCommonPrefix(strs []string) string {
    m := strs[0] // shortes word

    for _, v := range strs {
        if len(v) < len(m) {
            m = v
        }
    }

    for i := 0; i < len(m); i++ {
        p := m[:i+1] // prefix
        for _, v := range strs {
            if !strings.HasPrefix(v, p) {
                return m[:i]
            }
        }
    }

    return m
}