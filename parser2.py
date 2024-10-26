class LT2Parser:
    def __init__(self, program):
        self.lines = self.split_lines(program)  # <statement_list> ::= <statement> | <statement> <statement_list>
        self.current_token = None
        self.index =1
        self.variables = {}  # Store variable values for interpretation
        self.python_code = []  # Store generated Python code
        self.next_token()  # Move to the first token
        self.rel_op = ["==", "!=", ">", "<", ">=", "<="]   # <rel_op> ::= "==" | "!=" | ">" | "<" | ">=" | "<=

    def split_lines(self, program):
        """ Tokenize the program per line."""
        lines = []
        for line in program.split("\n"):
            lines.extend(line.split())
        return lines

    def next_token(self):
        """ Move to the next token."""
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def expect(self, token):
        """ Ensure the current token matches the expected token."""
        if self.current_token == token:
            self.next_token()
        else:
            raise Exception(f"Expected '{token}' but got '{self.current_token}'")

    def parse_program(self):
        """ <program> ::= <statement_list>"""
        current_line = 0
        for line in self.lines:
            current_line += 1
            self.parse_statement(line)
    
    def parse_statement(self, line):
        """ <statement> ::= <variable_declaration> 
                            | <print_statement> 
                            | <if_statement> 
                            | <comment>"""
        # tokenize the line
        tokens = []
        current_token = ""
        for char in line:
            if char.isspace():
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            else:
                current_token += char
        if current_token:
            tokens.append(current_token)
        # parse the line
        if tokens[0] == "//":
            self.parse_comment()
        elif tokens[0] == "pout":
            self.parse_print_statement()
        elif tokens[0] == "if":
            self.parse_if_statement()
        else:
            self.parse_variable_declaration()
    
    def parse_variable_declaration(self):
        """ <variable_declaration>  ::= <identifier> ":" <expression>
                                        | <identifier1> "," <identifier2> ":" <expression>"""
    
    def parse_print_statement(self):
        """ <print_statement>   ::= "pout(" <identifier>
                                    | <expression>
                                    | <term>")" """
    
    def parse_if_statement(self):
        """ <if_statement>  ::= "if" <condition> <new_line> <block>
                                | "if" <condition> <new_line> <block> <elif_list> <else_clause>"""
    
    def parse_elif_list(self):
        """ <elif_list> ::= "elif" <condition> <new_line> <block>
                        |   "elif" <condition> <new_line> <block> <elif_list>"""
    
    def parse_else_clause(self):
        """ <else_clause> ::= "else" <new_line> <block>"""
    
    def parse_block(self):
        """ <block> ::= <statement_list>"""
    
    def parse_comment(self):
        """ <comment>   ::= "//" <text>
            <text>      ::= <letter_or_digit>* """
    
    def parse_condition(self):
        """ <condition> ::= <expression> <rel_op> <expression>
            <rel_op>    ::= "==" | "!=" | ">" | "<" | ">=" | "<="""
        
        rel_op = ["==", "!=", ">", "<", ">=", "<="]
    
    def parse_expression(self):
        """ <expression> ::= <term> | <term> ("+" | "-") <expression>"""
    
    def parse_term(self):
        """ <term> ::= <factor> | <factor> ("*" | "/") <term>"""
    
    def parse_factor(self):
        """ <factor> ::= <number> | <identifier> | "(" <expression> ")" """
    
    def parse_identifier(self):
        """ <identifier> ::= <letter> <letter_or_digit>*"""
    
    
    def parse_number(self):
        """ <number>    ::= <digit>+
            <digit>     ::= [0-9]"""
    
    def parse_letter_or_digit(self):
        """ <letter_or_digit>   ::= <letter> | <digit>
            <letter>            ::= [a-zA-Z]
            <digit>             ::= [0-9]"""
        sel
