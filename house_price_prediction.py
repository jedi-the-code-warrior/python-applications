
# coding: utf-8

"""
Published: November 10, 2018

Author: Anjani K Shiwakoti

Synopsis: Housing price prediction, based on 'Sale Price' and 'Living Area', using advanced regression technique

Data Source: Kaggle House Prices dataset (https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
"""

### This cell imports the necessary modules and sets a few plotting parameters for display

get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)

### Read in the data
tr_path = 'datasets/house-prices/train.csv'
test_path = 'datasets/house-prices/test.csv'
data = pd.read_csv(tr_path)

### Data Exploration
### The .head() function shows the first few lines of data for perspecitve
data.head()

### Lists column names
data.columns

### Data Visualization
### We can plot the data as follows
### Price v. living area
### with matplotlib

Y = data['SalePrice']
X = data['GrLivArea']

plt.scatter(X, Y, marker = "x")

### Annotations
plt.title("Sales Price vs. Living Area (excl. basement)")
plt.xlabel("GrLivArea")
plt.ylabel("SalePrice");

### read file into a pandas dataframe
def read_to_df(file_path):
    """Read on-disk data and return a dataframe."""
    data_frame = pd.read_csv(file_path)
    return data_frame


### Build a function called "select_columns"
### As inputs, take a DataFrame and a *list* of column names.
### Return a DataFrame that only has the columns specified in the list of column names

def select_columns(data_frame, column_names):
    """Return a subset of a data frame by column names.
    
    Positional arguments:
        data_frame -- a pandas DataFrame object
        column_names -- a list of column names to select
        
    Example:
        data = read_into_data_frame('train.csv')
        selected_columns = ['SalePrice', 'GrLivArea', 'YearBuilt']
        sub_df = subselect_linreg_data(data, selected_columns)
    """
    
    # dataframe is sliced by loc[rows, columns]
    # the first parameter gives all rows, that is, rows in location 0 to -1 or [:], 
    # the second parameter gives only those columns given in the list of column names
    # print (type(data_frame1)) to ensure output obect type is dataframe
    
    data_frame1 = data_frame.loc[:, data_frame.columns.isin(column_names)]  
    
    return data_frame1

#create data frame from csv
data_frame = read_to_df(tr_path)

row_names = []
#row_names = data_frame.index.tolist() # returns a list of row index names or labels

# 2nd way is to use index.values
row_names = data_frame.index.values # returns an numpy ndarray of row index names or labels

# 3rd way is to use axes[0] 
# row_names = data_frame.axes[0].tolist() # returns a list of row index names or labels

print (type (row_names))
print (row_names)

# accessing a row is very different from accessing columns
# in dataframe rows are treated as if they are indices
# there's no dataframe.rows attribute, gives an error
# so use dataframe.index or dataframe.axes[0] instead

column_names = []
column_names = list(data_frame) # returns a list

# 2nd way of creating an array of column names in a data frame:
# column_names = data_frame.columns #return an array 
# 3rd way of creating list of column names in a data frame:
#column_names = list(data_frame.columns.values)

print (type (column_names))
print (column_names)

# data_frame.columns.values[0]  
# or
data_frame.index[5]
#you can also index both row label and column labels


#select_columns(data_frame, column_names)


### Build a function called "column_cutoff"
### As inputs, accept a Pandas Dataframe and a list of tuples.
### Tuples in format (column_name, min_value, max_value)
### Return a DataFrame which excludes rows where the value in specified column exceeds "max_value"
### or is less than "min_value"

def column_cutoff(data_frame, cutoffs):
    """Subset data frame by cutting off limits on column values.
    
    Positional arguments:
        data -- pandas DataFrame object
        cutoffs -- list of tuples in the format: 
        (column_name, min_value, max_value)
        
    Example:
        data_frame = read_into_data_frame('train.csv')
        # Remove data points with SalePrice < $50,000
        # Remove data points with GrLiveArea > 4,000 square feet
        cutoffs = [('SalePrice', 50000, 1e10), ('GrLivArea', 0, 4000)]
        selected_data = column_cutoff(data_frame, cutoffs)
    """
    ### you do not want to change original dataframe
    df_new = data_frame.copy(deep=False)
    
    ### take the first element of first tuple from the list 
    ### and assign it to column name, and then to min, max respectively
    ### iterate over each tuple on the list
    
    for x in cutoffs:
        column_name = str(x[0])  
        min_val = float(x[1])
        max_val = float(x[2])
        
        # select column by name and compare all its elements to see if anything is below min_val or above max_val,
        # if so save them in a separate dataframe as you'll need access to its row indices next
        df_rows_to_delete = df_new[(df_new[column_name] < min_val) | (df_new[column_name] > max_val)] 
        
        # selecting indices of df_rows_to_delete, drop all rows with the matching indices from df_new 
        # if more than one data point exist, delete all rows starting from zero to end [:] 
        df_new = df_new.drop(df_rows_to_delete.index[:])  
        
    return (df_new)
    

tuple_list = [("CostPrice", '.10', '999'), ("SellPrice", '.10', '999')]

selected_data = column_cutoff(data_frame, tuple_list)            


### Build a function  called "least_squares_weights"
### take as input two matricies corresponding to the X inputs and y target
### assume the matricies are of the correct dimensions

### Step 1: ensure that the number of rows of each matrix is greater than or equal to the number
### of columns.
### ### If not, transpose the matricies.
### In particular, the y input should end up as a n-by-1 matrix, and the x input as a n-by-p matrix

### Step 2: *prepend* an n-by-1 column of ones to the input_x matrix

### Step 3: Use the above equation to calculate the least squares weights.

### NB: `.shape`, `np.matmul`, `np.linalg.inv`, `np.ones` and `np.transpose` will be valuable.
### If those above functions are used, the weights should be accessable as below:  
### weights = least_squares_weights(train_x, train_y)
### weight1 = weights[0][0]; weight2 = weights[1][0];... weight<n+1> = weights[n][0]



def least_squares_weights(input_x, target_y):
    """Calculate linear regression least squares weights.
    
    Positional arguments:
        training_input_x -- matrix of training input data
        training_output_y -- vector of training output values
        
        The dimensions of X and y will be either p-by-n and 1-by-n
        Or n-by-p and n-by-1
        
    Assumptions:
        -- training_input_y is a vector whose length is the same as the
        number of rows in training_x
    """
    
    n = len(selected_data) # number of samples
    target_y = selected_data.SellPrice.values.reshape((n,1))
    input_x = np.hstack((np.ones((n,1), dtype=np.float64), selected_data.CostPrice.values.reshape((n,1))))
    
    ### calculate least square weights
    lsw = np.linalg.inv(input_x.T.dot(input_x)).dot(input_x.T.dot(target_y))
    
    ### another way to calculate least square weights
    # w_LS = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, y))
    # print(w_LS)
    
    return lsw

### test on example dataset as follows                                                    
training_y = np.array([[208500, 181500, 223500, 
                        140000, 250000, 143000, 
                        307000, 200000, 129900, 
                        118000]])
training_x = np.array([[1710, 1262, 1786, 
                        1717, 2198, 1362, 
                        1694, 2090, 1774, 
                        1077], 
                        [2003, 1976, 2001, 
                        1915, 2000, 1993, 
                        2004, 1973, 1931, 
                        1939]])
weights = least_squares_weights(training_x, training_y)

print (weights)


df = read_to_df(tr_path)
df_sub = select_columns(df, ['SalePrice', 'GrLivArea', 'YearBuilt'])

cutoffs = [('SalePrice', 50000, 1e10), ('GrLivArea', 0, 4000)]
df_sub_cutoff = column_cutoff(df_sub, cutoffs)

X = df_sub_cutoff['GrLivArea'].values
Y = df_sub_cutoff['SalePrice'].values

### reshaping for input into function
training_y = np.array([Y])
training_x = np.array([X])

weights = least_squares_weights(training_x, training_y)
print(weights)

max_X = np.max(X) ### + 100
min_X = np.min(X) ### - 100

### Choose points evenly spaced between min_x in max_x
reg_x = np.linspace(min_X, max_X, 100)

### Use the equation for our line to calculate y values
reg_y = weights[0][0] + weights[1][0] * reg_x

plt.plot(reg_x, reg_y, color='#58b970', label='Regression Line')
plt.scatter(X, Y, c='k', label='Data', marker='x')

plt.xlabel('CostPrice')
plt.ylabel('SellPrice')
plt.legend()
plt.show()


"""
RMSE - ROOT MEAN SQUARED ERROR

"""
rmse = 0

b0 = weights[0][0]
b1 = weights[1][0]

for i in range(len(Y)):
    y_pred = b0 + b1 * X[i]
    rmse += (Y[i] - y_pred) ** 2
rmse = np.sqrt(rmse/len(Y))
print(rmse)


""" 
R-SQUARED (STATISTIC) OR COEFFICIENT OF DETERMINATION

"""

ss_t = 0   # SUM OF SQUARED TOTALS
ss_r = 0   # SUM OF SQUARED RESIDUALS
mean_y = np.mean(Y)
for i in range(len(Y)):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_r/ss_t)
print(r2)

### now compare our model with that of sci-kit learn linear model
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

### sklearn requires a 2-dimensional X and 1 dimensional y. The below yeilds shapes of:
### skl_X = (n,1); skl_Y = (n,)
skl_X = df_sub_cutoff[['GrLivArea']]
skl_Y = df_sub_cutoff['SalePrice']

lr.fit(skl_X,skl_Y)
print("Intercept:", lr.intercept_)
print("Coefficient:", lr.coef_)
