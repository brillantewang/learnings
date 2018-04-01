# 4/1/18 - JavaScript30 Day1 Drumkit

Today I started JavaScript30 in preparation for my upcoming internship. These are what I learned from the drumkit exercise:

- `keydown` event
  - This is pretty awesome in that you can listen for whenever the user presses a key. The event object gives back a lot of useful properties such as `event.keyCode` which tells you the code of which key they pressed.
- `transitionend` event
  - This allows you to listen for whenever the CSS for an HTML element has finished its transition.
- `<audio>` HTML elements
  - These are HTML elements that you can select with something `querySelector` like and use its API. For example, you can use `.play` to play the corresponding audio clip (attached as a `src` property to the `<audio>` element).
- `data` attributes for HTML elements
  - At some point people started making up their own attribute names for HTML elements. So then we decided to create `data` attributes, which basically allow you to create any attribute you want as long as you put it after `data-`. It's basically so you can store metadata on any HTML element.

This was also the first time I've ever written JavaScript directly into an HTML file. Kinda cool!

# 3/12/18

Come back later and add entry about closures. Really good article https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures.

Quick note - A closure is a combination of a function and its `lexical environment`.

The `lexical environment` is basically the variables that were available, or in-scope, at the time the function was declared.

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
