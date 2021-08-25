### Bien tap du lieu

## Operator
# ^ | **      exp
# &           and
# |           or
# %%          modulus
# %/%         integer division
# isTRUE(x)   test if x is TRUE

### set wd
getwd()
# setwd("Desktop/ml-basic/")

### init variable
x1 <- c(1, 2, 3, 4)
x2 <- c(2, 5, 8, 10)

X = data.frame(x1, x2)

sum = x1 + x2

## add column sum = x1 + x2
X$sum = x1 + x2
X$mean = (x1 + x2)/2

## coding
id = c(1, 2, 3, 4, 5)
gender = c("MALE", "FEMALE", "FEMALE", "MALE", "MALE")

data = data.frame(id, gender)
data$sex[gender == "MALE"] = 1
data$sex[gender == "FEMALE"] = 2
data$group[id >= 1 & id < 4] = "A"
data$group[id >= 4] = "B"
data

## as numeric, vector, matrix, data.frame ...
id2 <- c("1", "2", "3", "4", "5")
id3 = as.numeric(id2)
mean(id3)
