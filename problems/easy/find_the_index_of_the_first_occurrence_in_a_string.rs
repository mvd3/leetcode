impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        let h = &haystack;
        let n = &needle;
        let mut r: i32 = -1;

        if let Some(i) = h.find(n) {
            r = i as i32;
        }

        r
    }
}