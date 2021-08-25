# Animal Outcomes at Austin Animal Center

This project evaluates the potential of predicting adoption outcomes for animals entering the Austin Animal Center and examines the implications of these findings.

### Authors
Katie Sylvia, Brian Berry, Rachael Friedman, Evan Hoefling, Maryam Amjad

### Table of Contents:

- Part I: Executive Summary
- Part II: Data Dictionary
- Part III: Conclusion

## Part I: Executive Summary

Pet shelters face enormous pressure to care for and to affect the ultimate wellbeing of animals brought into their care. One challenge this creates is capacity management as shelters have limited space and resources to allocate. For this reason, a thorough understanding of the shelter system and outcome likelihoods for the animals in question is necessary for the fulfillment of its central mission; it allows a shelter to manage capacity efficiently, both to maximize the potential for the adoption of certain animals quickly and for better planning to help as many "hard cases" as circumstances allow. This project seeks primarily to meet this need through the development of the strongest model to predict an animal's ultimate outcome (i.e. whether or not an animal will be adopted).

The process began with two datasets taken from the Austin Animal Center, one for intake information (or an animal's information upon being brought into the shelter system) and one for outcome information (information pertaining to an animal's being adopted, returned to owner, euthanized, etc.). The first step of preprocessing was to omit problematic/erroneous entries from each dataset. Then columns entered as strings were converted where possible to more model-friendly numeric values, and many features were engineered to experiment with anything that might prove useful for the predictive model. The final step was to merge the Intakes and Outcomes datasets, so that each stay of an animal at last consisted of a single entry in the final DataFrame.

The modeling process itself involved a great deal of exploration. The project team explored the possibility of modeling the dataset to predict an animal's duration of stay, though these attempts were unsuccessful, unable to improve our baseline score. The team had far greater success modeling for classification, both multi-class (an animal's final outcome across a variety of discrete possibilities) and binary classification (simply predicting whether or not an animal will be adopted). 

The binary classification model became our primary model as it closely aligns with the concerns and needs for animal shelters listed above. After much exploration, a simple Gradient Boost Classifier model showed the strongest accuracy results performing well above baseline. The final model exists in six different versions-- one model for each intake type. The StreamLit app filters for this value and applies the correct version of the model based on the information a user enters.

The flow of this project can be followed by reading into the following notebooks:
* [01: Data Cleaning]('code/01_Data_Cleaning.ipynb')
* [02: Initial EDA]('code/02_Initial_EDA.ipynb')
* [03: Final Data Prep]('code/03_Final_Data_Prep.ipynb')
* [04: Additional EDA]('code/04_Additional_EDA.ipynb')
* [05: Models]('code/05_Models.ipynb')

## Part II: Data Dictionary

Datasets Used/Created:
- [`Austin_Animal_Shelter_Intakes.csv`]('datasets/Austin_Animal_Shelter_Intakes.csv'): Initial Intakes dataset taken from the Austin Animal Center website
- [`Austin_Animal_Shelter_Outcomes.csv`]('datasets/Austin_Animal_Shelter_Outcomes.csv'): Initial Outcomes dataset taken from the Austin Animal Center website
- [`intakes_initial.csv`]('datasets/intakes_initial.csv'): Intakes dataset after preliminary cleaning, before the merge with Outcomes
- [`outcomes_initial.csv`]('datasets/outcomes_initial.csv'): Outcomes dataset after preliminary cleaning, before the merge with Intakes
- [`main.csv`]('datasets/main.csv'): Dataset used for modeling

Below is a list of relevant features included in `main.csv` as they relate to the final predictive model:

|Feature|Type|Dataset|Description|
|---|---|---|---|
|age_upon_intake|int|main.csv|Age of animal upon intake (in years)|
|animal_type|obj|main.csv|Species of animal|
|breed|obj|main.csv|Breed of animal|
|color|obj|main.csv|Color of animal|
|day_in|obj|main.csv|Day of week animal was brought to shelter|
|days_in_shelter|int|main.csv|Duration of animal's stay at shelter|
|intake_condition|obj|main.csv|Details related to animal's condition upon intake|
|intake_type|obj|main.csv|Details related to animal's circumstances upon intake|
|is_named_in|int|main.csv|Animal is named upon intake (binary)|
|is_neutered|obj|main.csv|Animal intact or neutered/spayed upon intake|
|mix|int|main.csv|Animal is a mixed breed (binary)|
|month_in|int|main.csv|Month animal arrived at shelter|
|outcome_type|obj|main.csv|Ultimate outcome for animal upon leaving shelter|
|prev_adoption|int|main.csv|Number of times animal had previously arrived at shelter and was adopted|
|prev_ret_to_owner|int|main.csv|Number of times animal had previously arrived at shelter and was returned to the owner|
|prev_transfer|int|main.csv|Number of times animal had previously arrived at shelter and was transferred|
|sex|obj|main.csv|Sex of animal|

## Part III: Conclusion & Recommendations

Ultimately, the project team was successful in crafting a model that performs well above the baseline when predicting whether or not an animal will be adopted. Our hope is that the Austin Animal Center can run our model with all of their intakes on a weekly basis to understand expected capacity at shelter and plan accordingly. While Austin Animal Center does a great job with data collection standardizing inputs such as age, date of birth, breed, and color could help make the information even more accurate and usable in the future.
