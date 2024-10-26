**Backus-Naur Form (BNF)** representation of the `.lt2` mini-programming language

### BNF Representation:

<program>               ::= <statement_list>
<statement_list>        ::= <statement> | <statement> <statement_list>
<statement>             ::= <variable_declaration> 
                         | <print_statement> 
                         | <if_statement> 
                         | <comment>
<variable_declaration>  ::= <identifier> ":" <expression> 
                         | <identifier1> "," <identifier2> ":" <expression>
<print_statement>       ::= "pout(" <identifier> | <expression> | <term>")"
<if_statement>          ::= "if" <condition> <new_line> <block> 
                         | "if" <condition> <new_line> <block> <elif_list> <else_clause>
<elif_list>             ::= "elif" <condition> <new_line> <block> 
                         | "elif" <condition> <new_line> <block> <elif_list>
<else_clause>           ::= "else" <new_line> <block>
<block>                 ::= <statement_list>
<comment>               ::= "//" <text>
<condition>             ::= <expression> <rel_op> <expression>
<expression>            ::= <term> | <term> ("+" | "-") <expression>
<term>                  ::= <factor> | <factor> ("*" | "/") <term>
<factor>                ::= <number> | <identifier> | "(" <expression> ")"
<identifier>            ::= <letter> <letter_or_digit>*
<number>                ::= <digit>+
<text>                  ::= <letter_or_digit>*
<rel_op>                ::= "==" | "!=" | ">" | "<" | ">=" | "<="
<letter_or_digit>       ::= <letter> | <digit>
<letter>                ::= [a-zA-Z]
<digit>                 ::= [0-9]

### Breakdown:
1. **Program**: A program consists of a list of statements.
2. **Statements**: The types of statements include variable declarations, print statements, if-else conditionals, and comments.
3. **Variable Declaration**: Either one or two variables can be declared with a single expression.
4. **Print Statement**: Prints the value of an identifier.
5. **If-Statement**: Includes conditional blocks with `if`, `elif`, and `else` clauses.
6. **Conditions**: Defined by expressions compared using relational operators (`==`, `!=`, `>`, `<`, `>=`, `<=`).
7. **Expression**: Can be a sum or difference of terms.
8. **Term**: Can be a product or quotient of factors.
9. **Factor**: Can be a number, identifier, or a nested expression.
10. **Identifiers**: Names of variables, consisting of letters and optional digits.
11. **Relational Operators**: Used in conditions for comparison.
12. **Comments**: Ignored in execution, starting with `//`.
