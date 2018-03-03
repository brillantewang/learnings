# 2/28/18 - Dynamic Programming

Today I got to the dynamic programming section on LeetCode and thought I needed a refresher. After some googling and watching some CS Dojo, here is my understanding of dynamic programming:

## What is it?
A way of making your code more efficient by storing (also known as memoizing) intermediate results so you can access them later, instead of having to re-calculate the results all over again.

## Example
A good example of this is fibonacci sequence, where given an input, n, you want to return the nth element of the fibonacci sequence:

On one hand, you could solve it recursively like this:

```
def fib(n)
  return 1 if n == 1 || n == 2

  return fib(n - 2) + fib(n - 1)
end
```

However this would result in a bunch of unnecessary recursive calls. For example, say n = 5. First, your function call fib(5) would need to call fib(3), which would need to call fib(2) and fib(1), both which return something and bubbles back up. Then your function would need to call fib(4), which would need to call fib(2), which returns something so bubbles back up, and then it would have to call fib(3) (notice this was already called before), which would need to call fib(2) and fib(1), both which return something and bubbles back up. Phew! As you can see, there's repetitive work being done here. This might be easier to understand if visualized as a tree:

```
        5
      /   \
    3       4
   / \     / \
  1   2   2   3
             / \
            1   2
```

Notice how there's a duplicate of the tree with a root of 3. It's duplicating the same exact work! So what if we just stored the result of fib(3) somewhere so it wouldn't ever need to be recalculated again? So when it ever has to call fib(3) again, it would immediately return the result instead of having to make further recursive calls. That way it would look like this:

```
        5
      /   \
    3       4
   / \     / \
  1   2   2   3
```

You may think, that doesn't look very different. However consider if the input was something greater, like 6. Without dynamic programming:

```
                    6
                /       \
              4           5
            /   \       /   \
           2     3     3     4
                / \   / \   / \
               1   2 1   2 2   3
                              / \
                             1   2
```

With dynamic programming:

```
                    6
                /       \
              4           5
            /   \       /   \
           2     3     3     4
                / \        
               1   2       
```

See the difference? This just gets even more pronounced as the input gets larger.

So what does this look like in code? We can either do this recursively and store the results in some sort of global variable:

```
$fibs = [0, 1, 1]

def fib(n)
  return $fibs[n] if $fibs[n]

  $fibs[n] = fib(n - 2) + fib(n - 1)
  $fibs[n]
end
```

Or we can do this iteratively, what we call a `bottom-up` approach.

```
def fib(n)
  return 1 if n == 1
  return 2 if n == 2

  fibs = [0, 1, 1]

  (3..n).each do |curr_fib|
    fibs[curr_fib] = fibs[curr_fib - 2] + fibs[curr_fib - 1]
  end

  fibs[n]
end
```

I tested out fib(50) without dynamic programming, and after 3 minutes of waiting I gave up and cancelled the function call. In contrast, I tried fib(50) with dynamic programming (both recursively and iteratively) and they both gave me the result (12586269025) immediately. The difference just gets more dramatic the larger the input. No wonder dynamic programming is so powerful!

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
