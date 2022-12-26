## The Wonderful World of Advent of Code 2022 ##
- [Day 1](#day-1)
- [Day 2](#day-2)
- [Day 3](#day-3)
- [Day 4](#day-4)
- [Day 5](#day-5)
- [Day 6](#day-6)
- [Day 7](#day-7)


## [Day 1: Calorie Counting](https://adventofcode.com/2022/day/1) ##

Holy moly!  Why does "with open() as name" remove the last empty line when reading!?  It does not strip all empty lines after the last entry, no, just the last one!  Anyhow my parse-as-you-read code works, as long as there are two new lines at the end of the list (the same as, one extra empty line after a copy-paste of the provided input).  I am sure there is a better way than using the "check for newline only" method, but this one is mine and I love it.  What a disaster.

## [Day 2: Rock Paper Scissors](https://adventofcode.com/2022/day/2) ##

A much more clean and pythonic solution for day 2, still solving whilst parsing the input but with some neat functions to cut-down on clutter and indentations.

## [Day 3: Rucksack Reorganization](https://adventofcode.com/2022/day/3) ##

Definitely should have split some of the work out into functions, but it works.  You cannot use enumerate on the "with open() as name" object, so instead of using readlines() and operating with enumerate, I just saved the last two values with a counter and a couple of variables to accomplish part 2.  Set intersection was my friend for this task.

## [Day 4: Camp Cleanup](https://adventofcode.com/2022/day/4) ##

Reasonably simple, almost worked first time after writing it all and pressing go.  If only I had remembered to change the strings to integers before comparing them.  Speaking of which, I should probably have done the conversion to integers at the start when splitting everything up, instead of doing it every time I used the input; some wasted time but it works.

## [Day 5: Supply Stacks](https://adventofcode.com/2022/day/5) ##

Well parsing the input took by far the most amount of time.  I tried writing proper code and (in my opinion) it looks quite nice.  Some nice uses for list comprehensions throughout.  Perhaps a bit too much "lets put as much as possible on one line" which kind of affects readability, but generally it feels like quite a nice solution.

## [Day 6: Tuning Trouble](https://adventofcode.com/2022/day/6) ##

The easiest day by far for me I think, definitely the one that took the least time.  Uses a very tidy function that takes in the input string and the length of the packet/message, so part 1 and part 2 just call the function with a different input.

## [Day 7: No Space Left On Device](https://adventofcode.com/2022/day/7) ##

I think a more proper way to do this would be to write a class for a directory, with attributes of parent and child directories, and methods to find the storage used; but I'm not very good at programming, so I kind of just tracked the current directory in a list of strings, and tracked the storage used in a dictionary.  I was intiially stumped until I realised (with the help of a search on the subreddit) that there could be the same name subdirectory in different directories, which I was counting as a single directory, rather than separate.  Part two was a simple extension by looping through the directory sizes with a bit of logic.

## [Day 8: Treetop Tree House](https://adventofcode.com/2022/day/8) ##

Finally left the realm of the base python installation to use numpy to handle the array operations.  Numpy's genfromtext made reading in the array a breeze.  Instead of checking every direction every time, I stopped checking if it became visible.  I'm sure you could optimise this by checking against the nearest two edges first since searching is O(n), but the code ran quickly enough.  Very similar solution for part 2, just changed the "check for visibility" function to "count to max visibility".  Also wrote a couple of functions to test for the solutions given in the examples which helped with debugging (which, as expected, was almost entirely due to come poor indexing and slicing..).

## Day next ##