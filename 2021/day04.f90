program day04
    implicit none

    ! new type to contain the boards (to avoid having 3d arrays)
    ! contains an array of the numbers, an array of logicals for numbers that have been called, and a logical for whether the board has won
    ! couldn't figure out how to get this to work in Fortran, so the implementation is from jacobwilliams
    type :: board
        integer,dimension(5,5) :: nums = 0
        logical,dimension(5,5) :: mask = .false.
        logical :: won = .false.
    end type board

    type(board),dimension(:),allocatable :: bingoBoards
    integer,dimension(:),allocatable :: bingoBalls
    integer :: iostatus, nLines, nEmptyLines, nBoards, iBoard, rows, rowBoard, iPlay, iCheck, winDraw, winBoard, score
    character(199) :: fname, line

    ! -------------------- parse input file to get lengths --------------------
    fname='data/day04.txt'
    open(101, file=fname, status='old', action='read', iostat=iostatus)
    nLines = 0
    nEmptyLines = 0
    do ! read file once to get lengths
        read(101, '(A)', iostat=iostatus) line
        nLines = nLines + 1
        if (iostatus/=0) then ! avoid end of file error
            exit
        else if (line=='') then
            nEmptyLines = nEmptyLines + 1
        end if
    end do
    nBoards = (nLines - 1 - nEmptyLines) / 5
    allocate(bingoBoards(nBoards))

    ! -------------------- parse input file to get bingoBalls and bingoBoards --------------------
    rewind 101
    iBoard = 0
    rowBoard = 1
    do rows = 1, nLines - 1
        read(101, '(A)', iostat=iostatus) line
        if (rows==1) then
            call split_read_int(line, bingoBalls)
        else if (line=='') then
            iBoard = iBoard + 1
            rowBoard = 1
        else
            read(line, '(I2,1X,I2,1X,I2,1X,I2,1X,I2))') bingoBoards(iBoard)%nums(rowBoard,:)
            rowBoard = rowBoard + 1
        end if
    end do
    close(101)

    !write(*,*) 'Bingo balls: ', bingoBalls
    !write(*,*) 'Board 1: ', bingoBoards(3)%nums

    ! -------------------- part 1 --------------------
    partOneMain: do iPlay = 1, size(bingoBalls)
        !play the game (where function in that was implemented in fortran 90 seen used by jacobwilliams also)
        do iBoard = 1, size(bingoBoards)
            where (bingoBoards(iBoard)%nums == bingoBalls(iPlay))
                bingoBoards(iBoard)%mask = .true.
            end where
        end do

        !check for win
        do iBoard = 1, size(bingoBoards)
            do iCheck = 1, 5
                if (all(bingoBoards(iBoard)%mask(iCheck,:))) then !winning col
                    winDraw = bingoBalls(iPlay)
                    winBoard = iBoard
                    exit partOneMain
                else if (all(bingoBoards(iBoard)%mask(:,iCheck))) then !winning row
                    winDraw = bingoBalls(iPlay)
                    winBoard = iBoard
                    exit partOneMain
                end if
            end do
        end do
    end do partOneMain

    score = winDraw * (sum(bingoBoards(winBoard)%nums) - sum(bingoBoards(winBoard)%nums, mask=bingoBoards(winBoard)%mask))
    write(*,*) 'Winning score for part 1 is: ', score

    ! -------------------- part 2 --------------------

    do iBoard = 1, size(bingoBoards)
        bingoBoards(iBoard)%mask = .false. !reset boards
    end do

    partTwoMain: do iPlay = 1, size(bingoBalls)
        !play the game (where function in that was implemented in fortran 90 seen used by jacobwilliams also)
        do iBoard = 1, size(bingoBoards)
            where (bingoBoards(iBoard)%nums == bingoBalls(iPlay))
                bingoBoards(iBoard)%mask = .true.
            end where
        end do

        !check for win, update won logical in board type
        do iBoard = 1, size(bingoBoards)
            do iCheck = 1, 5
                if (all(bingoBoards(iBoard)%mask(iCheck,:))) then !winning col
                    bingoBoards(iBoard)%won = .true.
                else if (all(bingoBoards(iBoard)%mask(:,iCheck))) then !winning row
                    bingoBoards(iBoard)%won = .true.
                end if
            end do
        end do

        !check for one left
        if (count(bingoBoards(:)%won) == size(bingoBoards) - 1) then
            do iBoard = 1, size(bingoBoards)
                if (.not. bingoBoards(iBoard)%won) then
                    winBoard = iBoard
                end if
            end do
        else if (count(bingoBoards(:)%won) == size(bingoBoards)) then
            winDraw = bingoBalls(iPlay)
            exit partTwoMain
        end if

    end do partTwoMain

    write(*,*) 'Last winning draw is: ', winDraw
    write(*,*) 'Last winning board is: ', bingoBoards(winBoard)
    score = winDraw * (sum(bingoBoards(winBoard)%nums) - sum(bingoBoards(winBoard)%nums, mask=bingoBoards(winBoard)%mask))
    write(*,*) 'Winning score for part 2 is: ', score

contains
    !subroutine to split line by comma delimiter from Thomas Koenig on the comp.lang.fortran google group
    subroutine split_read_int(input_str, output_array)
        character, parameter :: sep = ','
        character(len=*), intent(in) :: input_str
        integer, dimension(:), allocatable :: output_array
        integer :: i,n
        n = 1
        do i=1, len(input_str)
            if (input_str(i:i) == sep) n = n + 1
        end do
        allocate (output_array(n))
        read (unit=input_str,fmt=*) output_array
    end subroutine split_read_int

end program
