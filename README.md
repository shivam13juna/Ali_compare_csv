# Compare_csv for UpWork client Ali

The project consisted of two separate contracts

# First contract was to remove all the rows in csv A that shared phone numbers in another csv B
* Solved this simple problem by creating set of all the numbers in csv B, and then a simple for loop checking if the number in csv A exists in that set, if yes then remove that row.

# Second contract was to create a column 'similarity_column' which for each row consists indices with which it shares its estate_phone
* Solved this problem by brute method. 3 for loops checking if each number in each row is present in any other row's estate_phone

# How to train the model for new features?

For creating csv corresponding to first contract, execute `python3 Ali_diab_compare.py`
For creating csv corresponding to second contract, execute `python3 Ali_diab_compare_v2.py`
