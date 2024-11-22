🌾 Crop Recommendation System

This project utilizes machine learning to recommend the most suitable crop based on soil and weather conditions, helping farmers optimize yield and productivity.

📑 Features

Predicts the most suitable crop using soil and weather parameters such as Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, and rainfall.

Supports multiple machine learning models, including Random Forest, Gradient Boosting, Support Vector Machine (SVM), and Decision Tree classifiers.

Achieved 99.32% accuracy with the Random Forest classifier.

📁 Dataset

The dataset includes the following columns:

N, P, K: Soil nutrient content.

Temperature: Average temperature of the region (°C).

Humidity: Average humidity percentage.

pH: Soil pH level.

Rainfall: Annual rainfall (mm).

Label: Target crop name.

🛠️ Technologies Used

Programming Language: Python

Libraries/Frameworks: Pandas, Numpy, Scikit-learn, Flask

Tools: VS Code

🚀 How It Works

1.Data Preprocessing:

Cleaned and normalized the data to remove inconsistencies.

Split the data into training and testing sets.

2.Model Training:

Trained multiple machine learning models to recommend the best crop based on the input features.

Evaluated model performance using metrics like accuracy and precision.

3.Model Deployment:

Integrated the best-performing model (Random Forest) into a Flask web application.

Accepts user input via a web interface and provides real-time crop recommendations.

🌐 Usage

1.Clone the repository:

https://github.com/Pooja395/Crop_recommendation_project.git

2.Install dependencies:

pip install -r requirements.txt

3.Run the Flask application:

python app.py

4.Access the web app at http://127.0.0.1:5000

📊 Results

Random Forest achieved the highest accuracy of 99.32% for crop recommendations.

🤝 Contributing

Contributions are welcome! If you have suggestions for improving the system, feel free to open an issue or submit a pull request.

📜 License

This project is licensed under the MIT License.

📧 Contact

For queries or collaboration opportunities, reach out at [Pooja-pooja20150112843@gmail.com].


   

   


