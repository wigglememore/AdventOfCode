## The Wonderful World of Advent of Code 2022 ##
- [Day 1](#day-1)
- [Day 2](#day-2)
- [Day 3](#day-3)
- [Day 4](#day-4)


## [Day 1](https://adventofcode.com/2022/day/1) ##

Holy moly!  Why does "with open() as name" remove the last empty line when reading!?  It does not strip all empty lines after the last entry, no, just the last one!  Anyhow my parse-as-you-read code works, as long as there are two new lines at the end of the list (the same as, one extra empty line after a copy-paste of the provided input).  I am sure there is a better way than using the "check for newline only" method, but this one is mine and I love it.  What a disaster.

## [Day 2](https://adventofcode.com/2022/day/2) ##

A much more clean and pythonic solution for day 2, still solving whilst parsing the input but with some neat functions to cut-down on clutter and indentations.

## [Day 3](https://adventofcode.com/2022/day/3) ##

Definitely should have split some of the work out into functions, but it works.  You cannot use enumerate on the "with open() as name" object, so instead of using readlines() and operating with enumerate, I just saved the last two values with a counter and a couple of variables to accomplish part 2.  Set intersection was my friend for this task.

## [Day 4](https://adventofcode.com/2022/day/4) ##

Reasonably simple, almost worked first time after writing it all and pressing go.  If only I had remembered to change the strings to integers before comparing them.  Speaking of which, I should probably have done the conversion to integers at the start when splitting everything up, instead of doing it every time I used the input; some wasted time but it works.

## Day next ##