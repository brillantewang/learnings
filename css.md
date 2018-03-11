# 3/10/18 - `Pseudo-classes`

I've been using CSS pseudo-classes for a while, but never knew they were actually called pseudo-classes until just now. A `pseudo-class` is a keyword you can add to the end of a CSS selector that allows you to give it certain properties when it's that state. For example:

```
div:hover {
  cursor: pointer;
}
```

This will change the mouse to the hand looking thing whenever your mouse is hovering over the `div`.

Some other ones I've used before are:
- `:first-child`
- `:last-child`
- `:disabled`
- `:active`

# 3/10/18 - `Sprites`

Learned a pretty cool way to boost performance using CSS Sprites today. Say you had a website that had a bunch of images. Well to load each of one those images it would normally have to make a separate HTTP request for each image. Making multiple requests can take a long time.

To reduce the number of HTTP requests, you can create what's called a CSS Sprite. It's essentially just one large image file that consists of all of your other image files combined.

So why on earth would anyone want to do that? It's so your website only has to make one HTTP request to get that large file (the CSS sprite). Then you can tailor each element to only display a certain part of the CSS sprite using CSS properties like `height` and `background-position`.

It can be really tedious to individually tailor the CSS properties for every image element you want to display, so there are tools out there (like Spritepad) that help you build the sprite, and give you the corresponding CSS that you can just copy over!

To me, this type of performance boost reminds me of using eager loading to avoid `N + 1` queries in Rails. You're basically batching all of the things you need in one big query, which is way faster than making a bunch of little queries, since each query has overhead to it.

Check [this](https://css-tricks.com/css-sprites/) guide out for more info.

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
