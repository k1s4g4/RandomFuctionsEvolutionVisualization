# RandomFunctionsEvolutionVisualization

![alt text](https://github.com/k1s4g4/RandomFunctionsEvolutionVisualization/blob/master/screenshot/4.png)

This program was made as a way of better understanding how random functions work. Our understanding is better when we see things instead of just imagining them.It just generates random values within an interval, calculates relative frequencies (probability) for each value and plots probability distributions for six different functions. 

The functions are:

**-random.randint()**
the interval was chosen so that the window fits in the screen and that is because window width is parametrized with the interval.

**-random.uniform()**
same as random.randint()

**-random.triangular()**
same interval as above and as midpoint was chosen the average of the bounds.

**-random.gamma()**
parameters were chosen so that it generates most numbers between 0 and 1 and all numbers greater than 1 are rejected. All results are multiplied by the size of the above intervals so it can fit with the rest functions.

**-random.gauss()**
parameters were chosen so that it generates most numbers between -1 and 1 and numbers other numbers are rejected. Adding 1, dividing by 2 and multipling by the size of the above intervals makes it fit the rest functions

**-random.beta**
in the last case, parameters were chosen randomly. This function generates numbers between 0 and 1 so multipling by the size of the above interval fixes the interval problem.

Be carefull when changing paremeters because the problem is not hardly parametrized and possibly you might not be able to see exactly the same result.


Below you can see a sequence of screenshots from the same generation.

![alt text](https://github.com/k1s4g4/RandomFunctionsEvolutionVisualization/blob/master/screenshot/1.png)

![alt text](https://github.com/k1s4g4/RandomFunctionsEvolutionVisualization/blob/master/screenshot/2.png)

![alt text](https://github.com/k1s4g4/RandomFunctionsEvolutionVisualization/blob/master/screenshot/3.png)

![alt text](https://github.com/k1s4g4/RandomFunctionsEvolutionVisualization/blob/master/screenshot/4.png)

![alt text](https://github.com/k1s4g4/RandomFunctionsEvolutionVisualization/blob/master/screenshot/5.png)

![alt text](https://github.com/k1s4g4/RandomFunctionsEvolutionVisualization/blob/master/screenshot/6.png)

