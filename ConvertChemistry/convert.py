import argparse
from chempy import mass_fractions, balance_stoichiometry
from chempy.units import to_unitless, default_units as u


def grams_to_moles(formula, grams):
    # Get the stoichiometric coefficients and molecular weights
    elements, coeffs = balance_stoichiometry(*mass_fractions(formula))
    mw = sum(elements[e]['mass'] * c for e, c in coeffs.items())

    # Convert grams to moles
    moles = to_unitless(mw*u.g/u.mol*grams/u.g)

    return moles


def main():
    parser = argparse.ArgumentParser(description='Convert mass in grams to moles')
    parser.add_argument('formula', type=str, help='The formula of the substance')
    parser.add_argument('grams', type=float, help='The mass of the substance in grams')

    args = parser.parse_args()

    moles = grams_to_moles(args.formula, args.grams)

    print(f"{args.grams} grams of {args.formula} is equal to {moles:.2f} moles.")


if __name__ == '__main__':
    main()
