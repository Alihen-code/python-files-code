def apply_discount(price, discount):
    """Validate inputs and return the price after discount."""
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    if price <= 0:
        return "The price should be greater than 0"
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    return price - (price * discount / 100)


def apply_tax(price, tax_rate):
    """Add tax to a price. tax_rate is a percentage (e.g. 15 for 15%)."""
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    if not isinstance(tax_rate, (int, float)):
        return "The tax rate should be a number"
    if price < 0:
        return "The price should be 0 or greater"
    if tax_rate < 0 or tax_rate > 100:
        return "The tax rate should be between 0 and 100"
    return price + (price * tax_rate / 100)


def get_number(prompt):
    """Prompt the user until they enter a valid number."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Invalid input — please enter a number (e.g. 100 or 19.99).")


def main():
    print("=== Price Calculator ===")

    price = get_number("Enter the price: ")
    discount = get_number("Enter the discount (%) or 0 for none: ")
    tax_rate = get_number("Enter the tax rate (%) or 0 for none: ")

    discounted = apply_discount(price, discount)

    # apply_discount returns a string on validation failure — detect that
    if isinstance(discounted, str):
        print(f"Error: {discounted}")
        return

    final_price = apply_tax(discounted, tax_rate)

    if isinstance(final_price, str):
        print(f"Error: {final_price}")
        return

    print("\n--- Receipt ---")
    print(f"Original price : {price:.2f}")
    print(f"Discount       : {discount:.2f}%  (-{price - discounted:.2f})")
    print(f"After discount : {discounted:.2f}")
    print(f"Tax            : {tax_rate:.2f}%  (+{final_price - discounted:.2f})")
    print(f"Final price    : {final_price:.2f}")


if __name__ == "__main__":
    main()