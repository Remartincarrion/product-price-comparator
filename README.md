
# Installation & Setup

1. Clone the repository

2. Create and activate a virtual environment
python -m venv venv

venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run mock api
python mock_api.py


# Usage 

1. Run the main script
python src/analysis.py

2. Check the generated report (report.md file)


# Why I chose a mock datasource?

For this project, I initially wanted to use an external datasource in order to obtain real-time product prices for comparison. However, I faced some problems with that idea:

1. Most pricing datasources are restricted to business accounts. requiring registering a real business account, which was not possible for this project.
2. Some websites provide pricing data, but only for paid subscriptions

Given these constraints, I decided to mock the external data source using FastAPI to create a local server. It was a great idea because I could structure the dataset as needed for testing and analysis. Also it's easy to modify and expand the dataset if required.

In conclusion, maybe it's not the same as using a real-world API for price comparisons, but using a mock API allowed me to create a functional aplication which could work with a real external API in the future. 