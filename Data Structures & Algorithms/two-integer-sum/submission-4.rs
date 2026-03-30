use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen: HashMap<i32, i32> = HashMap::new();

        for (i, &v) in nums.iter().enumerate() {
            let diff = target - v;
            if let Some(&index) = seen.get(&diff) {
                return vec![index, i as i32];
            }
            seen.insert(v, i as i32);
        }

        vec![]
    }
}
