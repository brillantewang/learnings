# 4/1/18 - Class methods, alternative constructors, and static methods

I recently accepted an internship-to-hire offer, and am preparing for it. I've been learning Python since that's what they use for their back end. Today I learned about class methods, alternative constructors, and static methods. Here is my understanding.

A class method is a method that automatically takes in the class, rather than the instance (like in instance methods). So instead of taking in `self` as an automatic argument, it takes in `cls` as an automatic argument. We don't want to use the variable name `class` because that's already a reserved keyword in Python, so we use `cls` instead.

So when do we need to write a class method? Whenever we need to reference the class itself, such as changing one of its class variables. For example:

```
@classmethod
def set_raise_amt(cls, amount):
    cls.raise_amt = amount
```

Above we're changing the class variable `raise_amt` to be the amount that we give it.

Another common use case for writing class methods is to write alternative constructors. This is basically another way of constructing your object insteads of going through the normal `__init__` method. Why would you want to do this? Because often times you want to pass some argument and parse it before passing the parsed results to the actual constructor method. For example:

```
@classmethod # an alternative constructor
def from_string(cls, emp_string):
    first, last, pay = emp_string.split("-")
    return cls(first, last, int(pay))
```

As you can see above, you have to 'decorate' the class method with `@clasmethod` above the function for it to be a class method.

What about static methods? Static methods are basically used when you want to write some method that logically relates to the class in some way, but doesn't need to reference the instance or class at all. So it doesn't automatically take in `self` or `cls`, it just takes in whatever other arguments it needs. So for example we could add this static method to the `Employee` class:

```
@staticmethod # doesn't automatically take in self, or cls cuz it doesn't need it
def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
        return False
    return True
```

So it relates to the Employee, but doesn't really need to do anything with any instances or the class itself. It just takes in an argument and returns something.

Notice that static methods also need to be decorated with `@staticmethod`

So to summarize?
- `instance method` - a method that does something with the instance.
- `class method` - a method that does something with the class.
- `alternative constructor` - a class method that first parses some input and then calls the actual constructor with the parsed results.
- `static method` - a method that doesn't do anything with the instance or class, but still makes sense to put on the class.

For the source of my learnings, see https://www.youtube.com/watch?v=rq8cL2XMM5M
