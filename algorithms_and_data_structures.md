# 2/28/18 - Dynamic Programming

Today I got to the dynamic programming section on LeetCode and thought I needed a refresher. After some googling and watching some CS Dojo, here is my summary of dynamic programming:

## What is it?
- A way of making your code more efficient by storing (also known as memoizing) intermediary results so you can access them later, instead of having to re-calculate the results all over again.

## Example
A good example of this is fibonacci sequence:

(to be continued)

# 2/26/18 - Breadth First Search

Today I solved a problem called `Binary Tree Level Order Traversal` on LeetCode. The problem is defined as:

```
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
```

I was able to solve this with a breadth first search approach. Here is the original solution I came up with:

```
var levelOrder = function(root) {
    if (root === null) return [];

    let levels = [[root.val]];

    let currLevel = [root];
    let nextLevel = [];
    while (true) {
        while (currLevel.length !== 0) {
            let currNode = currLevel[0];
            let currNodeLeft = currNode.left;
            let currNodeRight = currNode.right;

            if (currNodeLeft !== null) nextLevel.push(currNodeLeft);
            if (currNodeRight !== null) nextLevel.push(currNodeRight);
            currLevel.shift();
        }

        if (nextLevel.length === 0) { break; }
        let nextLevelVals = nextLevel.map(node => node.val);
        levels.push(nextLevelVals);

        currLevel = nextLevel;
        nextLevel = [];
    }

    return levels;
};
```

It's a bit long, but later I'm going to see if I can cut out some code but have it still be readable. I believe the time complexity of this is linear since it's traversing each node of the BST.

### Takeaways:
Use BFS if you need to traverse every node of a binary search tree in a horizontal manner. This was a perfect application to this problem since it needed to output the horizontal levels.
