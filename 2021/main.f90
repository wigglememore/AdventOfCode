module part1
  implicit none
  public :: countIncreases
contains
  function countIncreases (x, n) result(increases)
    implicit none
    integer, intent(in) :: n
    integer, dimension(n), intent(inout) :: x
    integer :: temp, i, increases

    increases = 0
    temp = x(1)
    do i=2,n
        if (x(i) > temp) then
            increases = increases + 1
        endif
        temp = x(i)
    end do

    return
  end function countIncreases
end module part1

program day01
    use part1, only: countIncreases
    implicit none
    character(30) :: fname
    integer :: length, stat
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

    print *, "Number of increases is", countIncreases(depths, length)

end program

