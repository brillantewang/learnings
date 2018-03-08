# 3/5/18 - Binary
Today I came across a LeetCode problem that required a base understanding of binary. This isn't something that we really covered at App Academy so I did a bit of research and here's my understanding.

## What is it?
A number system with only two unique digits, 0 and 1. In everyday life, we normally use a `base 10` system (also known as a `denary` system). This is because we have ten digits to choose from, `0` up to `9`. If we want to go up to the next number, we 'round up' to `10`.

Binary on the other hand, is a `base 2` system, meaning it only has two digits to choose from, 0 and 1. That means `0` represents zero, `1` represents one, but if you want to go up to the next number, you'll have to 'round up' to `10` (which means two).

It's possible to convert between our everyday `denary` system and `binary`.

## Example
Let's break down what `1011` really means in a `denary` system (so our normal everyday system). Whether we realize it or not, we're really breaking it down into its digits and their corresponding exponents.

```
Digit:               1      0     1   1
Exponent (10^n):    1000   100   10   1
```

Notice that the farthest right digit corresponds to `10^0` or `1`, the second farthest right digit corresponds to `10^1` or `10` and etc.

Then we multiply each digit by its corresponding exponent:

```
1 * 1000 = 1000
0 * 100 = 0
1 * 10 = 10
1 * 1 = 1
```

And add them all up:

```
1000 + 0 + 10 + 1 = 1011
```

Now let's do the same but for binary. What number does `1011` represent in a binary system? Since binary is `base 2` system, the only difference is that the exponent is now `2^n`, again starting from the farthest right digit being `n = 0`.

```
Digit:              1   0   1   1
Exponent (2^n):     8   4   2   1
```

So we multiply each digit by its corresponding exponent:

```
1 * 8 = 8
0 * 4 = 0
1 * 2 = 2
1 * 1 = 1
```

And add them all up:

```
8 + 0 + 2 + 1 = 11
```

So `1011` in binary represents `11` in denary!

What if we wanted to convert a number from denary to binary? Say `26` for example.

Well first of all, think about how you would get the digits if we were thinking of this in terms of `base10`.
- First divide `26` by `10`. The remainder, `6`, takes the 'ones' place.
- Then divide the previous result, `2`, by `10`. The remainder, `2`, takes the 'tens' place.
- At this point, we can no longer divide because our result is at `0`, so we're done! Our digits are `26`.

This might look something like this:

```
26 / 10 = 2 remainder of 6

Ones Place: 6

2 / 10 = 0 remainder of 2

Tens Place: 2

Can't divide any further, so we're done!

Digits: 26

```

Similarly we can get the digits in binary if we think of this in terms of `base2`. So what does that look like?
