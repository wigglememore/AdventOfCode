## The Wonderful World of Advent of Code 2023 ##
- [Day 1: Trebuchet?!](#day-1)
- [Day 2: Cube Conundrum](#day-2)

## [Day 1: Trebuchet?!](https://adventofcode.com/2023/day/1) ##

Well, AOC really giving it to us this year.  Part 1 was fine: I didn't use the common replace or regex solutions, but just the .isdigit() method and a couple of for/if/breaks.  For part 2 I realised regex was the way, however I was using the findinter method which didn't deal with the overlapping numbers.  I didn't even realise the overlapping was the reason for my answer being wrong until I took to Reddit, then switching to regex.findall with the overlapped flag got the answer pretty quickly.  Could have done this whilst parsing the input but I switched everything into functions to have the example tests built in (not that it helped with part 2...). 

## [Day 2: Cube Conundrum](https://adventofcode.com/2023/day/2) ##

I think not as bad as day 1, but I wouldn't go as far as to say easy.  Took a little bit on inspiration from "webiste11" on Github for the layout as I got myself stuck trying to do too much in one function.  Splitting it up really helped and the results then came out pretty quickly using just the built in Python functions.

## Day next ##