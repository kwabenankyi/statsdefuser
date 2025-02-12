Experiments on calculating xG, xA, and other advanced metrics for football, such as passmaps and pass values.

For calculating xG, I plan to use different measures:
- distance from goal
    - Linear regression- RMSE: 0.1378999852136325; % error: 59.63032706203136
    - Exponential regression- RMSE: 0.14774965239018562; % error: 90.56841054216554
Techniques: hypothesis is that the decision trees / random forest models will be the most accurate as we
add more metrics.

# Shot parameters
## Pre-shot xG params:
- aerial_won
- follows_dribble
- first_time
- open_goal
- body_part
- type
- technique
- position
- location
- under_pressure
- player_positions

## Post-shot xG params:
- The above
- end_location
- deflected
- outcome

# Pre-shot parameters testing (2487 shots)
| Technique | MSE | Top 3 feature importance | Lowest 3 feature importance | % within 0.01xG | Median abs diff | Median % diff |
| --------- | --- | ------------------------ | --------------------------- | --------------- | --------------- | ------------- |
| Decision tree | 0.0093729 | type: 0.35613, location_x: 0.20041, open_goal: 0.19254 | first_time: 0.0063744, aerial_won: 0.0039419, follows_dribble: 0.0 | 43.574 | 0.013713 | 28.243 |
| Random forest | 0.0048319 | type: 0.35389, open_goal: 0.19625, location_x: 0.18702 | first_time: 0.0078999, aerial_won: 0.0074133, follows_dribble: 6.5621e-08 | 43.775 | 0.012769 | 25.057 |
| XGBoost | 0.0064219 | type: 0.62373, open_goal: 0.31644, aerial_won: 0.013574 | position: 0.0026037, first_time: 0.0022764, follows_dribble: 2.5284e-06 | 40.161 | 0.015830 | 32.398 |
| Bagging Regressor | 0.0052593 | | | 46.185 | 0.012372 | 24.603