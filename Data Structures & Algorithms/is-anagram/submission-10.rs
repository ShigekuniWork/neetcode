use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut count_s: HashMap<u8, i32> = HashMap::new();
        let mut count_t: HashMap<u8, i32> = HashMap::new();

        for (s_value, t_value) in s.bytes().zip(t.bytes()) {
            *count_s.entry(s_value).or_insert(0) += 1;
            *count_t.entry(t_value).or_insert(0) += 1;
        }
        count_s == count_t
    }
}
