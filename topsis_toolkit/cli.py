import argparse
import pandas as pd
from pankaj_102203410_topsis.topsis import topsis

def main():
    parser = argparse.ArgumentParser(description="Run TOPSIS analysis.")
    parser.add_argument("input", help="Path to input CSV file.")
    parser.add_argument("weights", help="Comma-separated weights for criteria.")
    parser.add_argument("impacts", help="Comma-separated impacts (+/-).")
    parser.add_argument("output", help="Path to save the output CSV file.")
    args = parser.parse_args()

    # Load data
    data = pd.read_csv(args.input)
    weights = list(map(float, args.weights.split(",")))
    impacts = [1 if impact == "+" else -1 for impact in args.impacts.split(",")]

    # Perform TOPSIS
    scores = topsis(data.iloc[:, 1:].values, weights, impacts)

    # Save results
    data["Topsis Score"] = scores
    data["Rank"] = scores.argsort()[::-1] + 1
    data.to_csv(args.output, index=False)
