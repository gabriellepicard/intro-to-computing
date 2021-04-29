# QUESTION 1: CREATING A MATRIX

# Create the first matrix
matrix1 <- matrix(c(7, 2, 9, 4, 12, 13), nrow = 2, ncol = 3)

# Create the second matrix
matrix2 <- matrix(c(1, 2, 3, 7, 8, 9, 12, 13, 14, 19, 20, 21), nrow = 3, ncol = 4)

# Matrix multiplication
matrix1%*%matrix2

# QUESTION 2: CREATING A DATAFRAME

# Create a dataframe
Data_Frame <- data.frame(
  id = c(1:5),
  name = c('Peter', 'Amy', 'Ryan', 'Gary', 'Michelle'),
  salary = c(623.30, 515.20, 611.00, 729.00, 842.25)
)

# Add department columns
DF_new <- cbind(Data_Frame, department = c('Accounting', 'Intern', 'HR', 'IT', 'Engineering'))

# Extract row 1,3,5 with column 2,3
DF_new2 <- Data_Frame[-c(2,4), -c(1,4)]

# Plot row 1,4,5 and label with corresponding names

#x-axis
x <- c(Data_Frame[(1,4,5), 2]

#y-axis
y <- c(Data_Frame[(1,4,5), ])