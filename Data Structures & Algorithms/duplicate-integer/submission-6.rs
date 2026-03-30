use std::collections::HashSet;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let nums_length = nums.len();
        let set: HashSet<i32> = nums.into_iter().collect();
        set.len() < nums_length
    }
}
