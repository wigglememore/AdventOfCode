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
    character(30) :: fnamep1, fnamep2
    integer :: length, stat
    integer, dimension(:), allocatable :: depthsSingle(:), depthsTriple(:)

    ! input file names
    fnamep1='data/d1p1.txt'
    fnamep2='data/d1p2.txt'

    ! import part 1 input data
    ! unit, file name & location, status (old = current file), iostat = status message (0 = fine, negative = error), action = possible actions with the file
    open(1, file=fnamep1, status='old', iostat=stat, action='read')
    if (stat .ne. 0) then
       write(*,*) fnamep1, 'cannot be opened'
       go to 98
    end if
    ! need to fix this bit so the length doesn't have to be in the first line
    read(1,*) length
    allocate(depthsSingle(length))
    read(1,*) depthsSingle
    close(1)
    ! close the file
    98 close(1)

    ! solve and print part 1
    print *, "Number of increases for part 1 is", countIncreases(depthsSingle, length)

    ! import part 2 input data

    ! open the file
    ! unit, file name & location, status (old = current file), iostat = status message (0 = fine, negative = error), action = possible actions with the file
    open(2, file=fnamep2, status='old', iostat=stat, action='read')
    if (stat .ne. 0) then
       write(*,*) fnamep2, 'cannot be opened'
       go to 99
    end if
    ! need to fix this bit so the length doesn't have to be in the first line
    read(2,*) length
    allocate(depthsTriple(length))
    read(2,*) depthsTriple
    close(2)
    ! close the file
    99 close(2)

    ! solve and print part 2
    print *, "Number of increases for part 2 is", countTripleIncreases(depthsTriple, length)

end program
