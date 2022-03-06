/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
       int sum =0;
    public int rangeSumBST(TreeNode current, int low, int high) {
       if(current == null)
            return 0;
        
        
        if(current.val >= low && current.val <= high)
            sum+=current.val;    
   
        
    rangeSumBST(current.left, low, high);
    rangeSumBST(current.right, low, high);
        
        return sum;
    }
 

}