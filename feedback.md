# Week 1 Feedback

## Testing

I'm glad to see you've does a lot of testing on your code, this is great to see!

I think you could have more tests for `lengthen_date`, in particular the util function that you've created. I think it's great that you've separated the suffix behaviour out into it's own function but htis should be well tested if we want to ensure that the data has the correct suffix. We also want to make sure it works for numbers like 11/12/13 as these are a bit of an exception to the usual rule.

In general I'd recommend trying to identify certain behaiours of your function. In this case I think that includes things like:

- having the correct day of the week
- having the correct month
- dates having the correct ordinal suffixes (this could be mutiple assertions in the same test if you wanted to greoup them like that)

I also like how you've thought about what could go wrong (invalid date) - this could be something you could handle using Python error handling for now that you've learnt about it.

## Solutions:

Your solutions are really nice! It's clear you're getting to grips with Python and the new syntax and methods we have access to.

Something you might want to look at the next time you work on katas is comprehensions. There are some case where youve used for loops that could be refactored to some kind of comprehension. Keep this in mind during the kata afternoon next week.