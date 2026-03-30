/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */


func diameterOfBinaryTree(root *TreeNode) int {
	maxDiameter := 0
	var dfs func(*TreeNode) int
	dfs = func(root *TreeNode) int {
		if root == nil {
			return 0
		}

		left := dfs(root.Left)
		right := dfs(root.Right)

		maxDiameter = max(maxDiameter, left+right)

		return max(left, right) + 1
	}

	dfs(root)
	return maxDiameter
}

