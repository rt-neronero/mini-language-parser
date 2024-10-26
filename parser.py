class LT2Parser:
    def __init__(self, program):
        self.tokens = self.tokenize(program)  # Tokenize input
        self.current_token = None
        self.index = -1
        self.variables = {}  # Store variable values for interpretation
        self.python_code = []  # Store generated Python code
        self.next_token()

    def tokenize(self, program):
        """Tokenize the input program into individual tokens."""
        tokens = []
        current_token = ""
        for char in program:
            if char.isspace():  # If it's a space, flush the current token if it exists
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            elif char in "();":  # Handle parentheses and semicolons
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(char)
            else:
                current_token += char  # Build up the current token
        if current_token:
            tokens.append(current_token)  # Add the last token if it exists
        return tokens

    def next_token(self):
        """Move to the next token."""
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def expect(self, token):
        """Ensure the current token matches the expected token."""
        if self.current_token == token:
            self.next_token()
        else:
            raise SyntaxError(f"Expected '{token}' but got '{self.current_token}'")

    def parse_program(self):
        """<program> ::= <statement>*"""
        while self.current_token is not None:
            self.parse_statement()

    def parse_statement(self):
        """<statement> ::= <variable_declaration> | <print_statement> | <if_statement> | <comment>"""
        if self.current_token == "//":
            self.parse_comment()
        elif self.current_token.startswith("pout"):
            self.parse_print_statement()
        elif self.current_token == "if":
            self.parse_if_statement()
        else:
            self.parse_variable_declaration()

    def parse_variable_declaration(self):
        """<variable_declaration> ::= <identifier> ":" <expression> | <identifier1>, <identifier2> ":" <expression>"""
        identifiers = [self.parse_identifier()]

        if self.current_token == ",":
            self.next_token()  # Move past comma
            identifiers.append(self.parse_identifier())

        self.expect(":")
        expr = self.parse_expression()

        for identifier in identifiers:
            self.variables[identifier] = expr
            self.python_code.append(f"{identifier} = {expr}")

    def parse_print_statement(self):
        """<print_statement> ::= "pout(" <identifier> | <expression> ")" """
        self.expect("pout")
        self.expect("(")
        
        if self.current_token == ")":
            raise SyntaxError("Missing expression in pout()")
        
        # Check if the next token is an identifier
        while True:
            if self.current_token.isalpha():
                identifier = self.parse_identifier()
                if identifier not in self.variables:
                    raise NameError(f"Variable '{identifier}' not defined.")
                value = self.variables[identifier]
                print(value)
                self.python_code.append(f"print({identifier})")
            else:
                expression = self.parse_expression()  # Parse the full expression
                print(expression)  # This prints the evaluated expression
                self.python_code.append(f"print({expression})")

            if self.current_token == ")":
                break

        self.expect(")")  # Expect the closing parenthesis

    def parse_if_statement(self):
        """<if_statement> ::= "if" <condition> /n <block> ["elif" <condition> /n <block>]* ["else" /n <block>]"""
        self.expect("if")
        condition = self.parse_condition()
        self.expect("\n")
        if_block = self.parse_block()

        self.python_code.append(f"if {condition}:")
        self.python_code.extend([f"    {line}" for line in if_block])

        elif_blocks = []
        while self.current_token == "elif":
            self.next_token()
            elif_condition = self.parse_condition()
            self.expect("\n")
            elif_block = self.parse_block()
            elif_blocks.append((elif_condition, elif_block))
            self.python_code.append(f"elif {elif_condition}:")
            self.python_code.extend([f"    {line}" for line in elif_block])

        else_block = None
        if self.current_token == "else":
            self.next_token()
            self.expect("\n")
            else_block = self.parse_block()
            self.python_code.append("else:")
            self.python_code.extend([f"    {line}" for line in else_block])

    def parse_block(self):
        """<block> ::= <statement>*"""
        statements = []
        while self.current_token not in {None, "elif", "else"}:
            if self.current_token == "\n":
                self.next_token()
            else:
                statements.append(self.parse_statement())
        return statements

    def parse_comment(self):
        """<comment> ::= "//" <text>"""
        self.expect("//")
        while self.current_token not in {None, "\n"}:
            self.next_token()

    def parse_condition(self):
        """<condition> ::= <expression> ("==" | "!=" | ">" | "<" | ">=" | "<=") <expression>"""
        left_expr = self.parse_expression()
        op = self.current_token
        if op in {"==", "!=", ">", "<", ">=", "<="}:
            self.next_token()
        else:
            raise SyntaxError(f"Invalid comparison operator '{self.current_token}'")
        right_expr = self.parse_expression()
        return f"{left_expr} {op} {right_expr}"

    def parse_expression(self):
        """Parse an expression consisting of terms combined by '+' or '-'."""
        left_term = self.parse_term()  # Start with a term
        while self.current_token in {"+", "-"}:  # Continue while there are '+' or '-' operators
            op = self.current_token
            self.next_token()  # Move to the next token
            right_term = self.parse_term()  # Get the next term
            left_term = f"({left_term} {op} {right_term})"  # Combine terms
        return left_term

    def parse_term(self):
        """Parse a term consisting of factors combined by '*' or '/'."""
        left_factor = self.parse_factor()  # Start with a factor
        while self.current_token in {"*", "/"}:  # Continue while there are '*' or '/' operators
            op = self.current_token
            self.next_token()  # Move to the next token
            right_factor = self.parse_factor()  # Get the next factor
            left_factor = f"({left_factor} {op} {right_factor})"  # Combine factors
        return left_factor

    def parse_factor(self):
        """Parse a factor which can be a number, identifier, or an expression in parentheses."""
        if self.current_token.isdigit():  # If it's a number
            return self.parse_number()  # Parse number
        elif self.current_token.isalpha():  # If it's an identifier
            return self.parse_identifier()  # Parse identifier
        elif self.current_token == "(":  # If it's an opening parenthesis
            self.expect("(")
            expr = self.parse_expression()  # Parse the expression within parentheses
            self.expect(")")  # Expect the closing parenthesis
            return expr  # Return the parsed expression
        else:
            raise SyntaxError(f"Unexpected token '{self.current_token}'")
        
    def parse_number(self):
        """Parse a number (integer or float) from the current token."""
        if not self.current_token.isdigit():  # Check if the current token is a digit
            raise SyntaxError(f"Expected a number but got '{self.current_token}'")
        
        number = self.current_token  # Store the current token as the number
        self.next_token()  # Move to the next token
        return number  # Return the parsed number
    
    def parse_identifier(self):
        """<identifier> ::= <letter> <letter_or_digit>*"""
        if self.current_token.isalpha():
            identifier = self.current_token
            self.next_token()
            return identifier
        else:
            raise SyntaxError(f"Invalid identifier '{self.current_token}'")
