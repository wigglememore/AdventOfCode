program day01
    implicit none
    character(30) :: fnamep
    integer :: iostatus, line, singleIncreases, tripleIncreases, singleTemp, tripleTemp, i, storeTwoBack, storeOneBack, current

    ! ------------------------------ part 1 ------------------------------
    ! initialise variables
    singleTemp = 0
    singleIncreases = 0
    tripleTemp = 9999999
    i = 1
    ! input file name
    fnamep='data/day01.txt'
    ! import input data
    ! unit, file name & location, status (old = current file), iostat = status message (0 = fine, negative = error), action = possible actions with the file
    open(101, file=fnamep, status='old', action='read', iostat=iostatus)
    if ( iostatus /= 0 ) stop "Error opening file input file"

    do ! read file and complete operations during read
        read(101,*, iostat=iostatus) line
        if(iostatus/=0) then ! avoid end of file error
            exit
        else if (i == 1) then
            singleTemp = line
            storeTwoBack = line
        else
            ! part 1 solve
            if (line > singleTemp) then
                singleIncreases = singleIncreases + 1
            endif
            singleTemp = line
            ! part 2 solve
            if (i == 2) then
                storeOneBack = line
            else
                current = storeTwoBack + storeOneBack + line
                if (current > tripleTemp) then
                    tripleIncreases = tripleIncreases + 1
                endif
            endif
            tripleTemp = current
            storeTwoBack = storeOneBack
            storeOneBack = line
        end if
        i = i + 1
    end do
    close(101)

    ! print part 1
    print *, "Number of increases for part 1 is", singleIncreases

    ! print part 2
    print *, "Number of increases for part 2 is", tripleIncreases

end program
