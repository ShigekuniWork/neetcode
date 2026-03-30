use std::collections::HashSet;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let nums_length = nums.len();
        let mut cache: HashSet<i32> = nums.into_iter().collect();

        nums_length != cache.len()
    }
}
