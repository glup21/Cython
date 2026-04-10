grammar ProjectGrammar;

prog: statement+;

// Statement
statement: SEMI
    | var       // match variable definition
    | expr SEMI
    | read
    | write
    | '{' statement+ '}'
    | if
    | while
    ;

// Expression
expr: assignment;
expr_list: expr (',' expr)*;

assignment: ID ASSIGN assignment
    | logic
    ;

logic: logic LOG_OP equality
    | equality
    ;

equality: equality COMP_OP relation
    | relation
    ;

relation: relation REL_OP concat
    | add
    ;

concat
    : concat '.' add
    | add
    ;

add: add ('+' | '-') mul
    | mul
    ;

mul: mul ('*' | '/' | '%') unary
    | unary
    ;

unary: NOT unary
    | '-' unary
    | primary
    ;

primary: INT
    | FLOAT
    | STRING
    | BOOL
    | ID
    | '(' expr ')'
    ;

ARM_OP: '+' | '-' | '/' | '*';
MOD: '%';
CONCAT_STR: '.';
REL_OP: '<' | '>';
COMP_OP: '==' | '!=';
LOG_OP: '&&' | '||';
NOT: '!';
ASSIGN: '=';

// Variables and IDs
TYPE: 'int'
        | 'float'
        | 'bool'
        | 'string'
        ;

ID: [a-zA-Z][a-zA-Z0-9]*; // match identifiers
id_list: ID (','ID)*;
var: TYPE id_list SEMI;

// Commands
read: 'read' id_list SEMI;  
write: 'write' expr_list SEMI;
if: 'if' '(' condition ')' statement ('else' statement)?;
while: 'while' '(' condition ')' statement;
condition: expr; 

// Terminals
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' (~["'\\\r\n])* '"';
BOOL: 'true' | 'false';
SEMI: ';';
COMMENT: '//' ~[\r\n]* -> skip;
WS: [\t\n\r]+ -> skip;
