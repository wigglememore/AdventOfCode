program day02
    use strings
    implicit none
    character(50) :: fname, moveDirection, line
    character(50), dimension(3) :: args
    integer :: iostatus, h_p1 = 0, d_p1 = 0, h_p2 = 0, d_p2 = 0, aim = 0, moveAmount, nargs

    fname='data/day02.txt'
    ! import input data
    ! unit, file name & location, status (old = current file), iostat = status message (0 = fine, negative = error), action = possible actions with the file
    open(101, file=fname, status='old', action='read', iostat=iostatus)
    if ( iostatus /= 0 ) stop "Error opening file input file"

    do ! read file and complete operations during read
        read(101,'(A)', iostat=iostatus) line ! I'm almost certain that is is bad Fortran 90 and is left over from 77
        if(iostatus/=0) then ! avoid end of file error
            exit
        else
            call parse(line, ' ', args, nargs)
            moveDirection = args(1) ! assign direction
            read(args(2),*) moveAmount ! assign amount as integer
            if (moveDirection == 'down') then
                d_p1 = d_p1 + moveAmount
                aim = aim + moveAmount
            else if (moveDirection == 'up') then
                d_p1 = d_p1 - moveAmount
                aim = aim - moveAmount
            else if (moveDirection == 'forward') then
                h_p1 = h_p1 + moveAmount
                h_p2 = h_p2 + moveAmount
                d_p2 = d_p2 + moveAmount * aim
            else
                stop "Movement command not recognised"
            end if
        end if
    end do

    ! print part 1
    print *, "Final position for part 1 is horizontal ", h_p1, " and depth ", d_p1, "with a h*d of ", h_p1*d_p1
    ! print part 2
    print *, "Final position for part 1 is horizontal ", h_p2, " and depth ", d_p2, " (aim = ", aim, ") with a h*d of ", h_p2*d_p2

end program
