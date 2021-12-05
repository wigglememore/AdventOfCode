
program day01
    implicit none
    character(30) :: fname
    integer :: length, stat, increases, temp, i
    integer, dimension(:), allocatable :: depths(:)


    fname='data/input.txt'
    ! open the file
    ! unit, file name & location, status (old = current file), iostat = status message (0 = fine, negative = error), action = possible actions with the file
    open(1, file=fname, status='old', iostat=stat, action='read')
    if (stat .ne. 0) then
       write(*,*) fname, 'cannot be opened'
       go to 99
    end if

    ! need to fix this bit so the length doesn't have to be in the first line
    read(1,*) length
    allocate(depths(length))
    read(1,*) depths
    close(1)
    !write(*,*) depths

    ! close the file
    99 close(1)

    increases = 0
    temp = depths(1)
    do i=2,length
        if (depths(i) > temp) then
            increases = increases + 1
        endif
        temp = depths(i)
    end do

    print *, "Number of increases is", increases

end program

