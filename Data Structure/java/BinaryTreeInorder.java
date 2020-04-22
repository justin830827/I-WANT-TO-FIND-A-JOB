import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class BinaryTreeInorder {
    public List<Integer> inorderTraversalRecursion(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        helper(res, root);
        return res;

    }

    private void helper(List<Integer> res, TreeNode x) {
        if (x == null)
            return;
        helper(res, x.left);
        res.add(x.val);
        helper(res, x.right);
    }

    public List<Integer> inorderTraversalIteration(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode cur = root;
        while (cur != null || !stack.empty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            res.add(cur.val);
            cur = cur.right;
        }
        return res;
    }

    public List<Integer> inorderMorrisTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        TreeNode cur = root;
        while (cur != null) {
            if (cur.left != null) {
                TreeNode rightmost = cur.left;
                while (rightmost.right != null) {
                    rightmost = rightmost.right;
                }
                TreeNode tmp = cur;
                rightmost.right = tmp;
                cur = cur.left;
                tmp.left = null;
            } else {
                res.add(cur.val);
                cur = cur.right;
            }
        }
        return res;
    }
}