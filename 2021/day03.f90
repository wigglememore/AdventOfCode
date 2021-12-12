program day03
    implicit none
    character(30) :: fname
    character(len=:), allocatable :: line
    character(1) :: currentString
    integer, dimension(:, :), allocatable :: diagnostic
    integer :: io, row, col, currentDigit, columns, rows

    !input file name
    fname='data/day03.txt'
    columns = getColumns(fname)
    rows = getRows(fname)
    allocate(diagnostic(columns, rows))

    open(101, file=fname, status='old', action='read', iostat=io)
    row = 1
    allocate(character(columns) :: line)
    do
        read(101,*, iostat=io) line
        if(io/=0) then ! avoid end of file error
            exit
        else ! split line into separate digits and store in array
            do col=1,columns
                currentString = line(col:col)! split out one of the numbers
                read(currentString,*,iostat=io) currentDigit ! turn it into an integer
                ! print *, "Digit for row ", row, " and col ", col, " is ", currentDigit
                diagnostic(col, row) = currentDigit! store in array
            end do
        row = row + 1
        end if
    end do
    ! print *, diagnostic
    print *, "Power consumption is ", powerConsumption(diagnostic, rows, columns)
    print *, "Life support rating is ", lifeSupport(diagnostic, rows, columns)

contains
    ! open the file and count the number of rows
    function getRows(filename) result (rows)
        implicit none
        character(len=*), intent(in) :: filename
        integer :: iostatus, rows

        open(101, file=filename, status='old', action='read', position='rewind')
        rows = 0
        do
            read(101,*, iostat = iostatus)
            if(iostatus/=0) then ! avoid end of file error
                exit
            else
                rows = rows + 1
            end if
        end do
        close(101)
    end function getRows

    ! open the file and count the number of columns
    function getColumns(filename) result (columns)
        implicit none
        character(len=*), intent(in) :: filename
        character(30) :: line
        integer :: iostatus, columns

        open(101, file=filename, status='old', action='read', position='rewind')
        read(101,*, iostat = iostatus) line
        columns = len_trim(line)
        close(101)
    end function getColumns

    ! part 1 - function to calculate the power
    function powerConsumption(inputArray, lenRow, lenCol) result(power)
        implicit none
        integer, intent(in) :: lenRow, lenCol
        integer, dimension(lenCol, lenRow), intent(in) :: inputArray
        integer, dimension(lenCol) :: counter, epsilonBin, gammaBin
        integer :: power, i, j
        counter = 0 ! initialise counter array
        do i=1,lenRow
            do j=1,lenCol
                if (inputArray(j, i) == 1) then
                    counter(j) = counter(j) + 1
                end if
            end do
        end do
        do j=1,lenCol
            if (counter(j) > lenRow/2) then ! most common value = 1
                epsilonBin(j) = 1
            else
                epsilonBin(j) = 0
            end if
        end do
        gammaBin = 1 - epsilonBin
        power = bin2int(epsilonBin, lenCol) * bin2int(gammaBin, lenCol)
    end function

    ! part 2 - function to calculate the life support
    function lifeSupport(inputArray, lenRow, lencol) result(life)
        implicit none
        integer, intent(in) :: lenRow, lenCol
        integer, dimension(lenCol, lenRow), intent(in) :: inputArray
        logical, dimension(lenRow) :: keepO2, keepCO2
        integer :: j, i, mostCommon, life, O2int, CO2int
        keepO2 = .true. ! initialise
        keepCO2 = .true. ! initialise
        do j=1,lenCol
            if (count(keepO2) == 1) then
                exit
            else
                mostCommon = mostCommonNum(inputArray(j,:), keepO2, lenRow)! find most common passing the current column inputArray(:,j)
                do i=1,lenRow ! set keepO2 to false for those we don't want in the next round
                    if (inputArray(j,i) /= mostCommon) then
                        keepO2(i) = .false.
                    end if
                end do
            end if
        end do
        ! have repeated for O2 and CO2 separately as I don't think they will reach a single value left at the same time?
        do j=1,lenCol
            if (count(keepCO2) == 1) then
                exit
            else
                mostCommon = mostCommonNum(inputArray(j,:), keepCO2, lenRow)! find most common passing the current column inputArray(j,:)
                do i=1,lenRow ! set keepO2 to false for those we don't want in the next round
                    if (inputArray(j,i) == mostCommon) then
                        keepCO2(i) = .false.
                    end if
                end do
            end if
        end do
        O2int = findloc90(keepO2, .true., lenRow)
        CO2int = findloc90(keepCO2, .true., lenRow)
        life = bin2int(inputArray(:,O2int), lenCol) * bin2int(inputArray(:,CO2int), lenCol)
    end function

    ! function to calculate the most common of 0 and 1
    function mostCommonNum(inputColArray, keepArray, arrayLen) result(mostCommon)
        implicit none
        integer, intent(in) :: arrayLen
        integer, dimension(arrayLen), intent(in) :: inputColArray
        logical, dimension(arrayLen) :: keepArray
        integer :: mostCommon, i, counter
        real :: compareLen
        counter = 0 ! initialise counter
        do i=1,arrayLen
            if (keepArray(i) .eqv. .false.) then ! ignore values which have already been discarded
                cycle
            else if (inputColArray(i) == 1) then
                counter = counter + 1
            end if
        end do
        compareLen = count(keepArray)! compare against the remaining number of elements
        if (counter > compareLen/2) then ! most common value = 1
            mostCommon = 1
        else if (counter == compareLen/2) then ! half each, use most common = 1
            mostCommon = 1
        else
            mostCommon = 0
        end if
    end function

    ! function to transform a binary number to an integer (adapted from FJacq on tek-tips.com)
    function bin2int(b, lenB) result(i)
        implicit none
        integer :: i, k, j
        integer, intent(in) :: lenB
        integer, dimension(lenB), intent(in) :: b
        i = 0
        j=lenB-1
        do k=1,lenB
            i=i+b(k)*2**j
            j = j - 1
        enddo
    end function

    ! findloc in fortran 90 for logical arrays
    function findloc90(inputArray, checkVal, arrayLen) result(foundIndex)
        implicit none
        logical, dimension(arrayLen), intent(in) :: inputArray
        logical, intent(in) :: checkVal
        integer :: i, foundIndex, arrayLen
        do i=1,arrayLen
            if (inputArray(i) .eqv. checkVal) then
                foundIndex = i
                exit
            end if
        end do
    end function

end program
