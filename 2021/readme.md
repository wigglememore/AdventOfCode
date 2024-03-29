### Day 1

Initially I decided on something I through was typical, read in the data then parse it.  However I didn't want to hard-code the input data length, and I didn't want to use an array much bigger than necessary.  This meant that I had to read thorugh the data twice, once to determine the size of the array to allocate and again to read it into the array.  I decided a more Fortran-ic(?) way of doing this would be to do the calculations during read-in, however because part 1 and part 2 needed different initialisations the nested if loops look a little ugly.

In the end there is not any measurable difference in run time (both versions taking on average between 0.01s and 0.03s to run), although I suspect for a much longer list only reading through the data once would be measurably faster.  I think I will use this method for future problems when using the data during reading is possible.

### Day 2

For day 2 I used the [strings module](https://gbenthien.net/strings/index.html]) by George to split the direction and move amount and once again did the number crunching  during file read-in.  The 'split' subroutine should work for this, however the output of the string after the delimiter didn't seem to work, so I used the 'parse' subroutine instead.  Probably not quite as clean but it worked.

Additionally, I had trouble reading in each line of the input file with read(101,*, iostat=iostatus) line where 'line' was initialised as character(30) because it seemed to stop reading at the space between the direction and distance.  I fixed this by using read(101,'(A)', iostat=iostatus) line which I'm almost certain is bad Fortran 90 (I think it is left over from Fortran 77) but again, it worked...

To run day 2 you first need to compile precmod.f90 and stringmod.f90 before day02.f90

### Day 3

The first part of day 3 went okay once I figured out how to read the input into an array and read that arrays in Fortran are column-major.  The only other issue was the binary to integer function I grabbed from a forum which (unless I briefly lost the ability to read) did not remotely do what I wanted it to.

Part 2 took a bit more thinking.  Initially I tried to find some kind of linked list module and came across [this](https://github.com/mapmeld/fortran-machine/tree/main/flibs-0.9/flibs/src/datastructures) great github repo of fortran utilities.  I was struggling to conceptualise the logic with the methods of this linked list implementation so came up with an alternate approach of using an additional array (of the same length as the input) of logicals to record which input numbers had been discounted by the rules.  Once this was decided, the rest went down extremely quickly.  I don't think it is a particularly efficient method and could probably be re-written using the same approach with a lot less loops, but it worked and I'm proud of it.

### Day 4

As per usual reading in the data took much longer to figure out than implementing the logic required for the bingo game.  I knew I needed a data type to contain the bingo boards and same sized logical array: in Python I would probably try a dictionary but I knew you could create your own data types in Fortran, and [jacobwilliams](https://github.com/jacobwilliams) on Github had a great implementation of a board type containing the two arrays which I used.  I also used a subroutine from Thomas Koenig (on the comp.lang.fortran google group) to split a line by comma delimiter to separate the initial line of (as I called them) bingo balls.

I discovered a ocuple of great built in functions for arrays to do some of the work in part 1

* Once again from [jacobwilliams](https://github.com/jacobwilliams) the [where](http://www.personal.psu.edu/jhm/f90/statements/where.html) function (used to mask the assignment or evaluation of arrays) to mark in the logical array where the last called bingo ball matched a number in a bingo board
* The [sum](https://gcc.gnu.org/onlinedocs/gfortran/SUM.html) function to quickly evaluate the result of the unmarked numbers

For part 2 the logic was written in a few minutes but I couldn't figure out why the answer was wrong, especially since it was correct for the example case.  A whole afternoon debugging and a lot of print statements (I know...) got me nowhere.  The next and fresh eyes instantly noticed that not all of the bingo balls were being read in; I hadn't allocated enough space in the character that read in the line so it was being cut short.  A quick change and part 2 was complete.
