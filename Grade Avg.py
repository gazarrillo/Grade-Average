# Initial Input
test_score = float(input('Enter a test score, -1 to get the average: '))
# Initializing Variables
i = 0
total_score = 0
# Variable Determination
while test_score > -1:
    total_score = test_score + total_score
    test_score = float(input('Enter a test score, -1 to get the average: '))
    i += 1
# Average Calculation
average_score = total_score/i
# Display Results
print('The average for all the grades is:',round(average_score,1))
