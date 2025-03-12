# Euphoria User Engagement Analysis Report

**Author:** Jakeman Pendleton 
**Date:** 03/11/2025

---

## Introduction

[Provide a brief overview of the project objectives and the importance of the analysis.]
This project dealt with finding different statistics like the average or the highest average of happiness and session duration for VR use in three different algorithms. The information that was found will help Euphoria determine which algorithm is performing the best.

## Methodology

[Describe the steps you took to perform the analysis, including any calculations and reasoning behind them.]
-The first step was to open the csv file and analyze the data.
-Next I found the average happiness rating for each algorithm by looping through them and dividing the total happiness by the amount of sessions.
-Then I found the amount of sessions by pulling from the dictionary called stats.
-After, I found the average session duration for each algotrithm by again looping through them and dividing total duration by session count.
- The last two values I found were the highest averages of happiness and session duration, I did this by creating an if statement to loop through each algorithm and fiinding the largest number in a particular algorithm and returning that value.

## Results

- **Average Happiness Rating per Algorithm**

  - JoyStream: 8.5
  - SerenityFlow: 7.0
  - DeepPulse: 5.0

- **Total Number of Sessions per Algorithm**

  - JoyStream: 4
  - SerenityFlow: 3
  - DeepPulse: 3

- **Average Session Duration per Algorithm**

  - JoyStream: 37.5 minutes
  - SerenityFlow: 30.0 minutes
  - DeepPulse: 45.0 minutes

- **Highest and Lowest Performers**
  - Highest Average Happiness Rating: 8.5
  - Longest Average Session Duration: 45.0

## Observations and Insights

[Discuss any patterns, anomalies, or noteworthy findings from your analysis. Include any ethical considerations or unexpected results, especially related to the DeepPulse algorithm.]
The DeepPulse algoritm was especially unexpected because it had the lowest happiness rating, but the longest average session. This makes me wonder what would cause people to want to be on it for longer if it doesn't make them as happy as the other algorithms.

## Conclusions and Recommendations

[Summarize your conclusions based on the results. Provide any recommendations for next steps or further analysis.]
In conclusion, the best performing algorithm in Euphoria is JoyStream because is has the highest happiness rating, the most sessions, and it is second in average session duration. therefore, people are on it for a good amount of time per session and it makes them the happiest compared to the other two algorithms.

---

_This report contains confidential information proprietary to OmniCo. Unauthorized use or disclosure is strictly prohibited._
