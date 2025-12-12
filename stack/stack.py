def expressionParenthesisParser(expression):
    # 計算を実行するヘルパー関数
    def calculate(operator, num1, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            # 割り算は切り捨て
            return int(num1 / num2)
        else:
            raise ValueError(f"Unknown operator: {operator}")

    # 演算子の優先順位定義
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    operand_stack = []   # 数字（オペランド）用スタック
    operator_stack = []  # 演算子（オペレーター）用スタック
    temp_num = ''        # 複数桁の数字を一時的に保持する変数

    def apply_op():
        ope = operator_stack.pop()
        num2 = operand_stack.pop()
        num1 = operand_stack.pop()
        operand_stack.append(calculate(ope, num1, num2))
    
    for char in expression:

        if char.isdigit()