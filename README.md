# Flipkart-product-recommender
Flipkart Product Recommender
A full-stack web application that leverages Natural Language Processing (NLP) to suggest products to users. The system analyzes the relationships between product metadata to calculate similarity scores.

 ## System Architecture
### 1. Web Interface (Flask)
**Authentication**: Manages user sessions and secure access to the recommendation engine.

**Session Management**: Uses flask_session with a filesystem backend to keep users logged in across routes.

**Dynamic Routing**: Handles product queries via POST requests and renders results using Jinja2 templates (login.html, intro.html, output.html).

### 2. Database Layer (MySQL)
**User Storage**: Stores credentials in a flipkart table within the flip database.

**Verification**: Validates plaintext passwords against stored usernames to grant access.

**New User Logic**: Includes functionality to prevent duplicate registrations.

### 3. Recommendation Engine (ML)
**Data Preprocessing**: Cleans the Flipkart e-commerce dataset by filling null values, removing duplicate product names, and using Regular Expressions to strip non-alphanumeric characters from category trees.

## Feature Engineering:
Combines product_name,description,brand,and category into a single "text" metadata string for each item.

**Vectorization**: Converts text data into numerical format using TF-IDF (Term Frequency-Inverse Document Frequency) with a limit of 2,500 features.

**Similarity Logic**: Employs Cosine Similarity to calculate the distance between the searched product and the entire catalog.
