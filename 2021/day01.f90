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

module part2
  implicit none
  public :: countTripleIncreases
contains
  function countTripleIncreases (x, n) result(increases)
    implicit none
    integer, intent(in) :: n
    integer, dimension(n), intent(inout) :: x
    integer :: temp, current, i, increases

    increases = 0
    temp = x(1) + x(2) + x(3)
    do i=4,n
        current = x(i-2) + x(i-1) + x(i)
        if (current > temp) then
            increases = increases + 1
        endif
        temp = current
    end do

    return
  end function countTripleIncreases
end module part2

program day01
    use part1, only: countIncreases
    use part2, only: countTripleIncreases
    implicit none
    character(30) :: fnamep1
    integer :: length, iostatus1
    integer, dimension(:), allocatable :: depths(:)

    ! ------------------------------ part 1 ------------------------------
    ! part 1 input file name
    fnamep1='data/day01.txt'
    ! import part 1 input data
    ! unit, file name & location, status (old = current file), iostat = status message (0 = fine, negative = error), action = possible actions with the file
    open(101, file=fnamep1, status='old', action='read')
    length = 0
    do ! read file once to get length, allocate array, rewind file, re-read to get data
        read(101,*, iostat=iostatus1)
        if(iostatus1/=0) then ! avoid end of file error
            exit
        else
            length = length + 1
        end if
    end do
    allocate(depths(length))
    rewind 101
    read(101,*) depths
    close(101)

    ! solve and print part 1
    print *, "Number of increases for part 1 is", countIncreases(depths, length)

    ! solve and print part 2
    print *, "Number of increases for part 2 is", countTripleIncreases(depths, length)

end program
