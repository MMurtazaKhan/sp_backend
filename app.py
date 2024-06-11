from flask import Flask, request, jsonify
import random
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app, resources={r"/simulate": {"origins": "http://localhost:3000"}})

def monte_carlo_simulation(credit_score):
    results = []
    base_default_rate = 0.05  # Base default rate without any modification
    for _ in range(100):  # Number of simulations
        # Random factor to simulate variability in default rate
        variability = random.gauss(0, 0.01)
        # Adjust default rate based on credit score
        adjusted_default_rate = base_default_rate * (650 / credit_score) + variability
        results.append(max(0, min(1, adjusted_default_rate)))  # Ensure rate is between 0 and 1
    # Return the average result of simulations
    return sum(results) / len(results)

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    credit_score = data['credit_score']
    default_probability = monte_carlo_simulation(credit_score)
    return jsonify(default_probability=default_probability)

# Second API
def macroeconomic_monte_carlo_simulation(credit_score, num_simulations, num_years):
    results = []
    base_default_rate = 0.05  # Base default rate without any modification
    for _ in range(num_simulations):  # Number of simulations
        yearly_results = []
        for _ in range(num_years):
            # Randomly generate macroeconomic factors
            unemployment_rate = np.random.normal(loc=5.0, scale=1.5)
            inflation_rate = np.random.normal(loc=2.0, scale=0.5)
            gdp_growth_rate = np.random.normal(loc=3.0, scale=1.0)
            
            # Factor in macroeconomic conditions to adjust the default rate
            macro_factor = 1 + (unemployment_rate / 100) - (inflation_rate / 100) + (gdp_growth_rate / 100)
            variability = random.gauss(0, 0.01)
            adjusted_default_rate = base_default_rate * (650 / credit_score) * macro_factor + variability
            yearly_results.append(max(0, min(1, adjusted_default_rate)))  # Ensure rate is between 0 and 1
        
        # Average yearly results for this simulation
        results.append(sum(yearly_results) / num_years)
    # Return the average result of all simulations
    return sum(results) / len(results)

@app.route('/simulate_macroeconomic_factors', methods=['POST'])
def simulate_macroeconomic_factors():
    data = request.get_json()
    
    # Parameters
    credit_score = data['credit_score']
    num_simulations = data.get('num_simulations', 1000)
    num_years = data.get('num_years', 5)
    
    # Simulate default probability based on macroeconomic factors
    default_probability = macroeconomic_monte_carlo_simulation(credit_score, num_simulations, num_years)
    
    return jsonify(default_probability=default_probability)


# Third API
@app.route('/simulate_financial_behavior', methods=['POST'])
def simulate_financial_behavior():
    data = request.get_json()
    
    credit_score = data['credit_score']
    spending_habits = data['spending_habits']  # scale of 1 to 10
    payment_history = data['payment_history']  # percentage of on-time payments
    debt_to_income_ratio = data['debt_to_income_ratio']  # percentage
    
    def financial_behavior_simulation(credit_score, spending_habits, payment_history, debt_to_income_ratio):
        results = []
        base_default_rate = 0.05
        for _ in range(100):
            variability = random.gauss(0, 0.01)
            adjusted_default_rate = base_default_rate * (650 / credit_score) * (10 / spending_habits) * (1 / payment_history) * (debt_to_income_ratio / 100) + variability
            results.append(max(0, min(1, adjusted_default_rate)))
        return sum(results) / len(results)
    
    default_probability = financial_behavior_simulation(credit_score, spending_habits, payment_history, debt_to_income_ratio)
    return jsonify(default_probability=default_probability)


# Fourth API
@app.route('/simulate_employment_status', methods=['POST'])
def simulate_employment_status():
    data = request.get_json()
    
    credit_score = data['credit_score']
    job_stability = data['job_stability']  # scale of 1 to 10
    income_level = data['income_level']  # annual income
    employment_type = data['employment_type']  # full-time, part-time, self-employed, unemployed
    
    def employment_status_simulation(credit_score, job_stability, income_level, employment_type):
        results = []
        base_default_rate = 0.05
        employment_factor = {'full-time': 1, 'part-time': 1.2, 'self-employed': 1.5, 'unemployed': 2}
        for _ in range(100):
            variability = random.gauss(0, 0.01)
            adjusted_default_rate = base_default_rate * (650 / credit_score) * (10 / job_stability) * (1 / income_level) * employment_factor[employment_type] + variability
            results.append(max(0, min(1, adjusted_default_rate)))
        return sum(results) / len(results)
    
    default_probability = employment_status_simulation(credit_score, job_stability, income_level, employment_type)
    return jsonify(default_probability=default_probability)


# Fifth API
@app.route('/simulate_geographic_location', methods=['POST'])
def simulate_geographic_location():
    data = request.get_json()
    
    credit_score = data['credit_score']
    region = data['region']  # e.g., 'urban', 'suburban', 'rural'
    housing_market_trends = data['housing_market_trends']  # scale of 1 to 10
    regional_unemployment_rate = data['regional_unemployment_rate']  # percentage
    
    def geographic_location_simulation(credit_score, region, housing_market_trends, regional_unemployment_rate):
        results = []
        base_default_rate = 0.05
        region_factor = {'urban': 1, 'suburban': 1.1, 'rural': 1.3}
        for _ in range(100):
            variability = random.gauss(0, 0.01)
            adjusted_default_rate = base_default_rate * (650 / credit_score) * region_factor[region] * (10 / housing_market_trends) * (regional_unemployment_rate / 100) + variability
            results.append(max(0, min(1, adjusted_default_rate)))
        return sum(results) / len(results)
    
    default_probability = geographic_location_simulation(credit_score, region, housing_market_trends, regional_unemployment_rate)
    return jsonify(default_probability=default_probability)


# Sixth API
@app.route('/simulate_age_demographics', methods=['POST'])
def simulate_age_demographics():
    data = request.get_json()
    
    credit_score = data['credit_score']
    age_group = data['age_group']  # e.g., '18-25', '26-35', '36-45', '46-55', '56+'
    education_level = data['education_level']  # e.g., 'high school', 'bachelor', 'master', 'phd'
    marital_status = data['marital_status']  # single, married, divorced, widowed
    
    def age_demographics_simulation(credit_score, age_group, education_level, marital_status):
        results = []
        base_default_rate = 0.05
        age_factor = {'18-25': 1.2, '26-35': 1, '36-45': 0.9, '46-55': 0.8, '56+': 0.7}
        education_factor = {'high school': 1.2, 'bachelor': 1, 'master': 0.8, 'phd': 0.7}
        marital_factor = {'single': 1.1, 'married': 1, 'divorced': 1.3, 'widowed': 1.2}
        for _ in range(100):
            variability = random.gauss(0, 0.01)
            adjusted_default_rate = base_default_rate * (650 / credit_score) * age_factor[age_group] * education_factor[education_level] * marital_factor[marital_status] + variability
            results.append(max(0, min(1, adjusted_default_rate)))
        return sum(results) / len(results)
    
    default_probability = age_demographics_simulation(credit_score, age_group, education_level, marital_status)
    return jsonify(default_probability=default_probability)


# Seventh API
@app.route('/simulate_health_insurance', methods=['POST'])
def simulate_health_insurance():
    data = request.get_json()
    
    credit_score = data['credit_score']
    health_conditions = data['health_conditions']  # scale of 1 to 10
    health_insurance_type = data['health_insurance_type']  # e.g., 'private', 'public', 'none'
    insurance_coverage_level = data['insurance_coverage_level']  # percentage
    
    def health_insurance_simulation(credit_score, health_conditions, health_insurance_type, insurance_coverage_level):
        results = []
        base_default_rate = 0.05
        insurance_factor = {'private': 1, 'public': 1.1, 'none': 1.5}
        for _ in range(100):
            variability = random.gauss(0, 0.01)
            adjusted_default_rate = base_default_rate * (650 / credit_score) * (10 / health_conditions) * insurance_factor[health_insurance_type] * (1 / insurance_coverage_level) + variability
            results.append(max(0, min(1, adjusted_default_rate)))
        return sum(results) / len(results)
    
    default_probability = health_insurance_simulation(credit_score, health_conditions, health_insurance_type, insurance_coverage_level)
    return jsonify(default_probability=default_probability)


if __name__ == '_main_':
    app.run(debug=False)