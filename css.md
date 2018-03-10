# 3/10/18 - `Animations`

In gearing up for a front end interview, today I learned about CSS animations for the first time.

CSS animations are nice because you can animate your HTML elements without having to use JavaScript.

Really it boils down to creating an animation by writing some animaton code in your CSS with the `@keyframes` keyword like this:

```
@keyframes animation-title-here {
  /* animation code goes in here */
}
```

You can then apply that animation to any selector using the `animation-name` property with the animation title as the value. So for example, if I wanted to set my `change-color` animation to all `div` elements:

```
@keyframes change-color {
  0% {
    background-color: red;
  }
  100% {
    background-color: yellow;
  }

div {
  height: 100px;
  width: 100px;
  animation-name: change-color;
  animation-duration: 4s;
}
```

Notice the use of the `animation-duration` property to set how long it will take to get from 0% to 100% defined in my animation code.

Here's a fun little animation I created in [JS fiddle](https://jsfiddle.net/kuke0xg6/26/). It was my attempt to reproduce the second example from https://css-tricks.com/almanac/properties/a/animation/ without looking at their code.
