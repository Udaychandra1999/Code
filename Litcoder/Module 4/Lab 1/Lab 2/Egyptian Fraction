def egyptian_fraction(numerator, denominator):
    fractions = []

    while numerator != 0:

        unit_fraction_denominator = -(-denominator // numerator) 
        fractions.append(str(unit_fraction_denominator))

        numerator = numerator * unit_fraction_denominator - denominator
        denominator *= unit_fraction_denominator

    return fractions

numerator_input = int(input())
denominator_input = int(input())

result = egyptian_fraction(numerator_input, denominator_input)
print("\n".join(result))