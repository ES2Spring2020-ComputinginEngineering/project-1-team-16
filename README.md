# Project1
Project 1 Starter Code

Names:Athena and Odin
Team Name: Team 16

Your primary tasks will be to:

- build a pendulum,
- use theoretical equations (from physics) to calculate the period of the pendulum,
- collect real-world experimental data from your pendulum,
- create a computer simulation of your pendulum numerically,
- plot and extract meaningful results 2 through 4

Your final submission should include (on GitHub):

All of your updated Python files
A README.md file explaining what .py files to run to get your results
A .pdf file containing your final plots and a brief report and discussion of results
At least five micro:bit data files from a pendulum for testing your parsing code.

# Project 1: Pendulum Analysis

In this project we used three modes of data production to compare the variety of ways to model and understand a pendulum. We used a theoretical, experimental, and simulated approach. By creating multiple graphs, we were able to compare and contrast our calculated and real world data.

## Instructions 

This code should be followed in a step by step manner beginning with the Step 2 folder up through the Step 5 folder. Each folder contains scripts and graphs relating to a different mode of data production with identical graphical analysis for simple comparisons.

Step 2 Calculates uses a theoretical physics equation to calculate the period for a specific length. It then graphs these periods with their respective length. 

Step 3 pertains to the collection of real world data with a Lego constructed pendulum and two radio communicating Micro:bits. It holds 5 data sets and the scripts used to collect them. To collect data with Step 3 scripts download the receiver.py script to one Micro:bit and logger.py script to another. The logger Micro:bit should be connected to the end of the pendulum and the receiver Micro:bit should be connected to a computer. For specific instructions on data collection, refer to the README.md file in the Step 3 folder. We used data sets provided by Dr. Jennifer Cross due to time and technological restraints. 

Step 4 takes the experimental data in the Step 3 folder for graphing and analysis. The first script from Step 4 is Experimental Plotting Acceleration Vs. Time.py. This script translates the raw acceleration data into three separate graphs for each dimension. The next script used should be the Experimental Calculation and Plotting of Angle.py. This script breaks down the most important acceleration from the microbit and calculates a corresponding angle which it then plots. The next script is Finding and Graphing Period and Peaks Experimental.py which finds the peaks on the angle vs time graph and calculates the time between each one to find the average period. Finally the average period is graphed for each length with Experimental Length vs Period.py.

Step 5 creates a simulated pendulum and graphs it with Pendulum Simulation.py. Pendulum Simulation.py also finds an average period for each length. Simulated Period vs. Length.py then graphs the average period with their corresponding length.

Step 6 compares the three length vs. period data sets on the same log graph for comparison.