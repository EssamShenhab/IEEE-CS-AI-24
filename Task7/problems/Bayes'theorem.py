while True:
    try:
        a = input("prior_a = ")
        b = input("prior_b = ")
        b_given_a = input("conditional_b_given_a = ")

        if not (a.strip() and b.strip() and b_given_a.strip()):
            raise ValueError("Empty input! Please enter at least one number.")

        prior_a = float(a)
        prior_b = float(b)
        conditional_b_given_a = float(b_given_a)

        if not (0 < prior_a <= 1 and 0 < prior_b <= 1 and 0 < conditional_b_given_a <= 1):
            raise ValueError("Invalid input! Enter numbers between 0 and 1.")

        if prior_a == 0 or prior_b == 0:
            raise ValueError("Prior probabilities cannot be zero.")

        Bayes_theorem = (conditional_b_given_a*prior_a)/prior_b
        print(Bayes_theorem)
        break
    except ValueError:
        print("Invalid input! Enter numbers between 0 and 1.")
