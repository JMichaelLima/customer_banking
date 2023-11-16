# Import the create_cd_account and create_savings_account functions

from cd_account import create_cd_account
from savings_account import create_savings_account

# get_input function


def get_input(user_prompt: str, data_type: type, error_message: str):
    """
    This function prompts the user using the given message until the
    input can be successfully converted to the specified data type. If the input 
    does not match the data type, an error message is displayed and the user is 
    prompted again.

    Args:
        user_prompt (str): The message displayed to the user to prompt input.
        data_type (type): The type to convert the user's input to.
        error_message (str): The error message if user input cannot be converted 
        to the specified data type.

    Returns:
        User input, converted to the specified data type.
    """
    while True:
        try:
            return data_type(input(user_prompt))
        except ValueError:
            print(error_message)

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    tester = get_input
    savings_balance = get_input(
        "What is the initial savings account balance? ", float, "Please enter a valid balance. ")
    savings_interest = get_input(
        "What is the interest rate? ", float, "Please enter a valid interest rate. ")
    savings_maturity = get_input(
        "How many months? ", int, "Please enter a valid number of months. ")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(
        savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"updated_savings_balance: ${updated_savings_balance:,.2f}")
    print(f"interest_earned: ${interest_earned:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = get_input("What is the initial CD balance? ",
                           float, "Please enter a valid balance. ")
    cd_interest = get_input("What is the interest rate? ",
                            float, "Please enter a valid interest rate. ")
    cd_maturity = get_input("How many months? ", int,
                            "Please enter a valid number of months. ")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(
        cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"updated_cd_balance: ${updated_cd_balance:,.2f}")
    print(f"interest_earned: ${interest_earned:,.2f}")


if __name__ == "__main__":
    # Call the main function.
    main()
