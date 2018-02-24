# 2/24/18 - `.push` vs `.push.apply`

Today I learned about why you might want to use `push.apply`, rather than just `.push`. `.push` only allows for pushing in a single item, whereas `push.apply` allows you to push in an entire array of items (all as separate items). So for example, you could do something like:

```
  let nums = [1,2,3];
  nums.push.apply(nums, [4,5,6]); // => [1,2,3,4,5,6]
```

Whereas doing it without apply would give you this:

```
  let nums = [1,2,3];
  nums.push([4,5,6]); // => [1,2,3,[4,5,6]]
```

Why not just use `.concat` then? Because sometimes you may want to mutate the original array. Whereas `.concat` creates a new array and does not mutate the original, `.push` will mutate the original array. This is what I used to solve a `rotate` function with O(1) space complexity on LeetCode.
