AI-Powered Product Analysis Dashboard


Overview

The AI-Powered Product Analysis Dashboard is a cutting-edge, interactive web-based tool developed to classify and evaluate bottles based on their visual and functional features. The project leverages machine learning and advanced image processing techniques to predict key attributes of bottles, including:

Master Categories: Classifies bottles into different product categories like beverage, cosmetic, household, medical, etc.

Subtypes: Identifies the specific type of bottle such as plastic, glass, spray, or pump dispensers.

Morphological Features: Analyzes the shape and size of the bottle (e.g., tall, short, wide, slim, etc.).

Functional Factors: Assesses performance traits such as thermal insulation, durability, hygiene design, chemical safety, and ergonomics.

Real World Usage Traits: Evaluates practical usage features like user-friendliness, eco-friendliness, reusability, affordability, and premium-grade standards.

This tool not only provides detailed bottle analysis but also offers expert insights through an integrated AI Assistant based on the ChatGPT model. Users can interact with the assistant to get personalized suggestions and recommendations for product design improvements and usage optimization.

Key Features
Multi-Model Analysis: Utilizes separate Convolutional Neural Networks (CNN) models for each classification category (master category, subtype, morphological features, etc.).

Dynamic Visual Feedback: Provides confidence scores for each prediction along with bar charts for visual representation of the classification.

Side-by-Side Bottle Comparison: Allows users to upload two bottles for comparative analysis on various attributes.

Interactive AI Assistant: Offers expert advice on product design, functionalities, and improvements.

User-Friendly Interface: Built with Streamlit for easy interaction and accessibility.

Feedback Form: Allows users to provide feedback to continuously improve the dashboard.

Project Background
This project was developed during my internship at the Indian Institute of Science (IISc), under the guidance of Dr. Rajath Desai and Mr. Puneet K. The goal was to create an AI-driven solution that can analyze the various factors affecting bottle design and functionality, based on image recognition and machine learning.

How It Works
Upload an Image: Users upload a bottle image via the dashboard.

Model Predictions: The backend models process the image and generate predictions on:

The master category of the bottle.

The subtype of the bottle.

Morphological features and functional factors.

Real-world usage traits.

Display Results: The results are displayed on the dashboard, with visualizations of the confidence scores and detailed analysis.

AI Assistant Interaction: Users can ask the AI Assistant for insights and suggestions regarding the bottle.

Technologies Used
Python: Primary programming language for development.

TensorFlow & Keras: For building and deploying the machine learning models.

Streamlit: For creating an interactive web application.

OpenAI GPT-3.5 Turbo: For generating responses in the AI Assistant.

gdown: To download pretrained models directly from Google Drive.

Pillow: For image manipulation and preprocessing.

Matplotlib & Seaborn: For data visualization.

Installation
To run the AI-Powered Product Analysis Dashboard locally:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/<darshhv>/AI-Powered-Product-Analysis-Dashboard.git
cd AI-Powered-Product-Analysis-Dashboard
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Contribution
This project is open to contributions! If you have suggestions for new features, improvements, or fixes, feel free to open an issue or create a pull request.

License
This project is licensed under the MIT License.

Acknowledgements
Special thanks to Dr. Rajath Desai and Mr. Puneet K for their invaluable guidance during my internship at the Indian Institute of Science (IISc) - Bengaluru.
