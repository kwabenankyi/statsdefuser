Experiments on calculating xG, xA, and other advanced metrics for football, such as passmaps and pass values.

For calculating xG, I plan to use different measures:
- distance from goal
    - Linear regression- RMSE: 0.1378999852136325; % error: 59.63032706203136
    - Exponential regression- RMSE: 0.14774965239018562; % error: 90.56841054216554
Techniques: hypothesis is that the decision trees / random forest models will be the most accurate as we
add more metrics.