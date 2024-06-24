from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# API 1: Basic Credit Score Simulation
@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    credit_score = data['credit_score']
    default_probability = monte_carlo_simulation(credit_score)
    return jsonify(default_probability=default_probability)

def monte_carlo_simulation(credit_score):
    results = []
    base_default_rate = 0.05
    for _ in range(100):
        variability = random.gauss(0, 0.01)
        adjusted_default_rate = base_default_rate * (650 / credit_score) + variability
        results.append(max(0, min(1, adjusted_default_rate)))
    return sum(results) / len(results)

# API 2: Credit Risk Based on Macroeconomic Factors
@app.route('/simulate_macroeconomic_factors', methods=['POST'])
def simulate_macroeconomic_factors():
    data = request.get_json()
    credit_score = data['credit_score']
    num_simulations = data.get('num_simulations', 1000)
    num_years = data.get('num_years', 5)
    projected_credit_scores, yearly_variance = macroeconomic_monte_carlo_simulation(credit_score, num_simulations, num_years)
    return jsonify(projected_credit_scores=projected_credit_scores, yearly_variance=yearly_variance)

def macroeconomic_monte_carlo_simulation(credit_score, num_simulations, num_years):
    yearly_scores_sum = [0] * num_years
    yearly_scores_squared_sum = [0] * num_years
    
    for _ in range(num_simulations):
        yearly_scores = []
        for year in range(num_years):
            unemployment_rate = random.uniform(0.03, 0.1)
            inflation_rate = random.uniform(0.01, 0.04)
            gdp_growth_rate = random.uniform(0.01, 0.05)
            macro_factor = unemployment_rate + inflation_rate - gdp_growth_rate
            variability = random.gauss(0, 0.01)
            adjusted_score = credit_score * (1 - macro_factor) + variability * 100
            yearly_scores.append(max(300, min(850, adjusted_score)))
        
        for year in range(num_years):
            yearly_scores_sum[year] += yearly_scores[year]
            yearly_scores_squared_sum[year] += yearly_scores[year] ** 2

    average_scores = [sum_value / num_simulations for sum_value in yearly_scores_sum]
    variance_scores = [(squared_sum / num_simulations - (sum_value / num_simulations) ** 2) for squared_sum, sum_value in zip(yearly_scores_squared_sum, yearly_scores_sum)]
    
    return average_scores, variance_scores

# API 3: Financial Behavior Simulation
@app.route('/simulate_financial_behavior', methods=['POST'])
def simulate_financial_behavior():
    data = request.get_json()
    credit_score = data['credit_score']
    spending_habits = data['spending_habits']
    payment_history = data['payment_history']
    debt_to_income_ratio = data['debt_to_income_ratio']
    risk_category_distribution = financial_behavior_simulation(credit_score, spending_habits, payment_history, debt_to_income_ratio)
    return jsonify(risk_category_distribution=risk_category_distribution)

def financial_behavior_simulation(credit_score, spending_habits, payment_history, debt_to_income_ratio):
    categories = {'low': 0, 'medium': 0, 'high': 0}
    for _ in range(100):
        risk_score = (credit_score / 850) * 0.4 + (payment_history / 100) * 0.3 - (debt_to_income_ratio / 100) * 0.2 + (spending_habits / 10) * 0.1
        variability = random.gauss(0, 0.05)  # Added variability
        adjusted_risk_score = risk_score + variability
        if adjusted_risk_score > 0.7:
            categories['low'] += 1
        elif adjusted_risk_score > 0.4:
            categories['medium'] += 1
        else:
            categories['high'] += 1
    return categories

# API 4: Employment Status Simulation
@app.route('/simulate_employment_status', methods=['POST'])
def simulate_employment_status():
    data = request.get_json()
    credit_score = data['credit_score']
    job_stability = data['job_stability']
    income_level = data['income_level']
    employment_type = data['employment_type']
    income_projection = employment_status_simulation(credit_score, job_stability, income_level, employment_type)
    return jsonify(income_projection=income_projection)

def employment_status_simulation(credit_score, job_stability, income_level, employment_type):
    base_growth_rate = 0.02  # Base growth rate of income per year
    stability_factor = job_stability / 10  # Job stability affects income stability
    type_factor = 1 if employment_type == 'full-time' else 0.8 if employment_type == 'part-time' else 1.2 if employment_type == 'self-employed' else 0.5
    income_projection = []
    
    for year in range(5):  # Simulate income for 5 years
        yearly_income_projection = []
        for _ in range(100):  # Monte Carlo iterations
            growth_rate = base_growth_rate * stability_factor * type_factor
            variability = random.gauss(0, 0.01)
            adjusted_income = income_level * (1 + growth_rate + variability)
            yearly_income_projection.append(adjusted_income)
        avg_yearly_income = sum(yearly_income_projection) / 100
        income_level = avg_yearly_income  # Update income level for the next year
        income_projection.append({'year': year + 1, 'income': income_level})
    
    return income_projection

# API 5: Geographic Location Simulation
@app.route('/simulate_geographic_location', methods=['POST'])
def simulate_geographic_location():
    data = request.get_json()
    credit_score = data['credit_score']
    region = data['region']
    housing_market_trends = data['housing_market_trends']
    regional_unemployment_rate = data['regional_unemployment_rate']
    regional_risk = geographic_location_simulation(credit_score, region, housing_market_trends, regional_unemployment_rate)
    return jsonify(regional_risk=regional_risk)

def geographic_location_simulation(credit_score, region, housing_market_trends, regional_unemployment_rate):
    region_factor = 1.2 if region == 'urban' else 1.0 if region == 'suburban' else 0.8
    market_factor = housing_market_trends / 10
    unemployment_factor = regional_unemployment_rate / 10
    risk_scores = []
    
    for _ in range(100):  # Monte Carlo iterations
        variability = random.gauss(0, 0.01)
        risk_score = (credit_score / 850) * 0.4 + region_factor * 0.3 + market_factor * 0.2 - unemployment_factor * 0.1 + variability
        risk_scores.append(risk_score)
    
    avg_risk_score = sum(risk_scores) / 100
    return {
        'risk_score': avg_risk_score,
        'region_factor': region_factor,
        'market_factor': market_factor,
        'unemployment_factor': unemployment_factor
    }

# API 6: Age and Demographics Simulation
@app.route('/simulate_age_demographics', methods=['POST'])
def simulate_age_demographics():
    data = request.get_json()
    credit_score = data['credit_score']
    age_group = data['age_group']
    education_level = data['education_level']
    marital_status = data['marital_status']
    demographic_impact = age_demographics_simulation(credit_score, age_group, education_level, marital_status)
    return jsonify(demographic_impact=demographic_impact)

def age_demographics_simulation(credit_score, age_group, education_level, marital_status):
    age_factor = 1.1 if age_group in ['36-45', '46-55'] else 1.0 if age_group in ['26-35', '56+'] else 0.9
    education_factor = 1.2 if education_level in ['master', 'phd'] else 1.0 if education_level == 'bachelor' else 0.8
    marital_factor = 1.1 if marital_status == 'married' else 1.0 if marital_status == 'single' else 0.9
    impact_scores = []
    
    for _ in range(100):  # Monte Carlo iterations
        variability = random.gauss(0, 0.01)
        impact_score = (age_factor + education_factor + marital_factor) * (credit_score / 850) + variability
        impact_scores.append(impact_score)
    
    avg_impact_score = sum(impact_scores) / 100
    return {
        'impact_score': avg_impact_score,
        'age_factor': age_factor,
        'education_factor': education_factor,
        'marital_factor': marital_factor,
        'age_group': age_group,
        'education_level': education_level,
        'marital_status': marital_status
    }

# API 7: Health and Insurance Simulation
@app.route('/simulate_health_insurance', methods=['POST'])
def simulate_health_insurance():
    data = request.json
    credit_score = data['credit_score']
    health_conditions = data['health_conditions']
    health_insurance_type = data['health_insurance_type']
    insurance_coverage_level = data['insurance_coverage_level']
    health_risk = health_insurance_simulation(credit_score, health_conditions, health_insurance_type, insurance_coverage_level)
    return jsonify(health_risk=health_risk)

def health_insurance_simulation(credit_score, health_conditions, health_insurance_type, insurance_coverage_level):
    condition_factor = (10 - health_conditions) / 10
    insurance_factor = 1.2 if health_insurance_type == 'private' else 1.0 if health_insurance_type == 'public' else 0.8
    coverage_factor = insurance_coverage_level / 100
    health_risk_scores = []
    
    for _ in range(100):  # Monte Carlo iterations
        variability = random.gauss(0, 0.01)
        health_risk_score = (condition_factor + insurance_factor + coverage_factor) * (credit_score / 850) + variability
        health_risk_scores.append(health_risk_score)
    
    avg_health_risk_score = sum(health_risk_scores) / 100
    return {'health_risk_score': avg_health_risk_score, 'condition_factor': condition_factor, 'insurance_factor': insurance_factor, 'coverage_factor': coverage_factor}

if __name__ == '__main__':
    app.run(debug=True)
