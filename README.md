### Training a Street Fighter Bot

#### 1. Data Collection
The data collection process involved running the game in different modes to gather information about both Player 1 and Player 2. For Player 1, the game was run in normal mode, and two rounds were played for each character. Player 2 data was collected in VS Battle mode, with two rounds played for each player. Each round played provided valuable information about the players' actions, health, coordinates, and move IDs. The collected data was stored in two separate CSV files, one for Player 1 and another for Player 2.

#### 2. Data Preprocessing
Before training the machine learning model, the collected dataset needed to be cleaned and prepared. To ensure data quality and eliminate noise, several preprocessing steps were performed:
- **Duplicate entries removal:** To prevent biases caused by repetitive data.
- **Exclusion of incomplete rounds:** Rows where the round had not started were excluded.
- **Health filtering:** Rows where players' health exceeded 200 were filtered out to maintain data consistency.

#### 3. Feature Engineering
In addition to the raw data, certain features were engineered to enhance the model's predictive capabilities. The Euclidean distance between Player 1 and Player 2 was calculated and included as a feature. This distance metric aimed to capture the spatial relationship between the two players, which could significantly impact gameplay strategies.

#### 4. Model Training
The preprocessed dataset was split into training and testing sets to evaluate the model's performance accurately. A Random Forest Classifier algorithm was chosen due to its effectiveness in handling classification tasks. During the training phase, the model learned patterns and relationships between the input features (x) and player controls (y).

#### 5. Model Export and Integration
Once the model was trained, it was exported using the Pickle library, allowing for easy retrieval and utilization. The model was saved within the `bot.py` file, which served as the bridge between the game and the machine learning model. By feeding each line of data from the game into the model, the bot generated predictions for player controls, enabling the character to make informed moves.

#### 6. Results and Future Enhancements
The integrated system demonstrated promising results, effectively predicting player controls based on the trained model. However, further improvements could be explored to enhance the bot's performance:
- **Advanced machine learning techniques:** Incorporating more sophisticated algorithms.
- **Feature engineering approaches:** Exploring new features to improve predictive accuracy.
- **Hyperparameter tuning:** Fine-tuning the model's parameters for optimal performance.
- **Larger dataset:** Collecting more diverse data to improve the model's generalization and adaptability to various gameplay scenarios.

#### How to run
1. Run command prompt in working directory
2. Run command 'python controller.py 1' 
3. Run the emulator file in single player directory
4. Run the gyroscope emulator alongside during the match
5. Watch the bot in action!
