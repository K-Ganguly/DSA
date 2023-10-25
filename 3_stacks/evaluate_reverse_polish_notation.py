# LeetCode Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty list to store the operands and results during evaluation.
        expression = list()

        # Define a set of valid operators: +, -, *, and /.
        operators = {"+", "-", "*", "/"}

        # Initialize the result variable to 0.
        result = 0

        # Check if there's only one token in the input list and it's not an operator; return it as the result.
        if len(tokens) == 1 and tokens[0] not in operators:
            return int(tokens[0])

        # Process each token in the input list.
        for token in tokens:
            if token not in operators:
                # Add non-operator tokens to the expression list, as they are operands.
                expression.append(token)
            else:
                # When encountering an operator, perform the following steps.
                # 1. Pop the last two operands from the expression list.
                operand1 = expression.pop()
                operand2 = expression.pop()

                # 2. Create a new expression by combining the two operands and the operator.
                result_expression = operand2 + token + operand1

                # 3. Evaluate the new expression and convert the result to an integer.
                result = str(int(eval(result_expression)))

                # 4. Append the result back to the expression list for further evaluation.
                expression.append(result)

        # After processing all tokens, the final result is stored in the 'result' variable.
        # Convert it to an integer and return as the answer.
        return int(result)
