### Day 1

Holy moly!  Why does "with open() as name" remove the last empty line when reading!?  It does not strip all empty lines after the last entry, no, just the last one!  Anyhow my parse-as-you-read code works, as long as there are two new lines at the end of the list (the same as, one extra empty line after a copy-paste of the provided input).  What a disaster.