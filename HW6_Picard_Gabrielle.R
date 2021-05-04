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

# PLOT ROW 1,4,5 AND LABEL WITH CORRESPONDING NAMES

# Set x-axis
x <- Data_Frame[-c(2,3), -c(1,3)]

# Set y-axis
y <- Data_Frame[-c(2,3), -c(1,2)]

# Plot barplot
barplot(y, names.arg = x, main="Salaries", xlab="Name", ylab="Salary")

# PLOT A PIE CHART

# Calculate max, min, median
max(Data_Frame$salary)
min(Data_Frame$salary)
median(Data_Frame$salary)

# Create a vector of labels
mylabel <- c("Maximum", "Minimum", "Median")

# Create a vector of colors
colors <- c("deepskyblue", "coral", "darkviolet")

# Create a vector of values using variables
x <- c(max(Data_Frame$salary), min(Data_Frame$salary), median(Data_Frame$salary))

# Display pie chart
pie(x, label = mylabel, main = "Descriptive Statistics - Salaries", col = colors)

# QUESTION 3

# for loop in R

# Set up a function
list_process <- function(x) {
  
  # Create empty list
  new_list <- list();
  
  # Add for loop to process each element of the list
  for (word in x) {
    
    # Step 1: lowercase each element of list
    word2 <- tolower(word)
    print(paste("Step 1:", word2))
    
    # Step 2: remove punctuation from each element of list
    word3 <- gsub("[[:punct:]]+","",word2)
    print(paste("Step 2:", word3))
  }
}

# Test for loop function
list_process(list("fiNals", "Exams!", "todAY", "Oh NO"))
list_process(list("WiLL", "i.", "finish?", "this", "ASSIGNMENT"))
list_process(list("YES!", "I WiLL.", "SURELY?", "Complete", "The", "Assignment"))

# if else in R

# Set up a function
list_process2 <- function(x) {
 
  # Use for loop to iterate through the list
  for (word in x) {
    # Set up if statement so that the list stops iterating at q or Q
    if (word == "q") {
      print("Thank you! That's all.")
      break
    }
    else if (word == 'Q') {
      print("Thank you! That's all.")
      break
    }
    else {
      print(word)
    }
  }
}

# Test if else statement
list_process2(list("q", "finals", "exams"))
list_process2(list("finals", "exams", "q"))
list_process2(list("finals", "Q", "exams"))