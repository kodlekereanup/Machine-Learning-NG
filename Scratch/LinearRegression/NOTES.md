# Linear Regression:

## Introduction:

Formally, Linear Regression is a linear approch to modelling the relationship between  scalar response
(dependent variable) and one (simple) or more (multiple) explanatory variables (independent variables). 

Multiple LR is not the same as Multivariate LR, where multiple correlated dependent variables are predicted, rather than a single scalar variable.

The data is modelled using a straight line. Used with continuous variables (Real Values).

The toal error of the linear model is the sum of the error of each point

$\sum_{i=1}^n r_i^2$

## Example: 
Let's say there exists a case where a dataset of House Size and Price is given. 
Now, if you want to find a relationship bewteen them, the most feasible (for lack of a better term)
solution would be to plot the data on a 2-d graph and find a best fit line. 

This process is known as Linear Regression (Is it though? I'm still confused)

An equation of a straight line in a plane is given by:
    y = m * x + c

The equation is a function of x. 
Where m is the slope of the line and c is the y intercept 

## Estimation

The whole point is to estimate the values of m and c. For that, various methods are devised.

* Least-squares
* Maximum-likelihood
* Bayesian LR
* Principal Component regression

