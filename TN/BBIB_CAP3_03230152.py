################################
# Github Repo link: https://github.com/Laketsho187/03230152_BIA101_CAPIII
# Your Name: Lakezin Jamtsho
# Your Section : B
# Your Student ID Number: 03230152
################################
# REFERENCES
# https://www.youtube.com/watch?v=ac3nbZ0V9PU\
# https://www.youtube.com/watch?v=OehCy8mnWX4
# SOLUTION
# Your Solution Score: 478095
################################

# Read the input.txt file
def read_input(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    return lines

# Calculate the sum of numbers formed by the first and last digits in each line
def calculate_sum(lines):
    total_sum = 0
    for line in lines:
        # Using two pointer approach to find the first and last digit
        start = 0
        end = len(line) - 1
        while start < len(line) and not line[start].isdigit():
            start += 1
        while end >= 0 and not line[end].isdigit():
            end -= 1
        # Check if start and end are valid indices
        if start < len(line) and end >= 0:
            # Calculate the number formed by the first and last digit
            number = int(line[start]) * 10 + int(line[end])
            total_sum += number
    return total_sum

# Main function to execute the solution
def main():
    file_name = "152.txt"  # Replace with your file name based on your index
    lines = read_input(file_name)
    total_sum = calculate_sum(lines)
    print(f"The total sum from the given input file is {total_sum}")

# Run the main function
main()
