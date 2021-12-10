Fortran huh

### Day 1

Initially I decided on something I through was typical, read in the data then parse it.  However I didn't want to hard-code the input data length, and I didn't want to use an array much bigger than necessary.  This meant that I had to read thorugh the data twice, once to determine the size of the array to allocate and again to read it into the array.  I decided a more Fortran-ic(?) way of doing this would be to do the calculations during read-in, however because part 1 and part 2 needed different initialisations the nested if loops look a little ugly.

In the end there is not any measurable difference in run time (both versions taking on average between 0.01s and 0.03s to run), although I suspect for a much longer list only reading through the data once would be measurably faster.  I think I will use this method for future problems when using the data during reading is possible.

### Day 2

For day 2 I used the [strings module](https://gbenthien.net/strings/index.html]) by George to split the direction and move amount and once again did the number crunching  during file read-in.  The 'split' subroutine should work for this, however the output of the string after the delimiter didn't seem to work, so I used the 'parse' subroutine instead.  Probably not quite as clean but it worked.

Additionally, I had trouble reading in each line of the input file with read(101,*, iostat=iostatus) line where 'line' was initialised as character(30) because it seemed to stop reading at the space between the direction and distance.  I fixed this by using read(101,'(A)', iostat=iostatus) line which I'm almost certain is bad Fortran 90 (I think it is left over from Fortran 77) but again, it worked...

To run day 2 you first need to compile precmod.f90 and stringmod.f90 before day02.f90