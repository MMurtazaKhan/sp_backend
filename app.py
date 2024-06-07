from flask import Flask, request, jsonify
import random
from flask_cors import CORS

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

if __name__ == '_main_':
    app.run(debug=True)