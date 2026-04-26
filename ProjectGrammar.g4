grammar ProjectGrammar;

prog: statement+;

statement
    : ';'                                               # emptyStatement
    | primitiveType IDENTIFIER (',' IDENTIFIER)* ';'    # declaration
    | expr ';'                                          # printExpr
    | 'read' IDENTIFIER (',' IDENTIFIER)* ';'           # read
    | 'write' expr (',' expr)* ';'                      # write
    | '{' (statement)+ '}'                              # statementsBlock
    | 'if' '(' expr ')' statement ('else' statement)?   # ifStatement
    | 'while' '(' expr ')' statement # whileStatement
    ;

expr
    : SUB expr                                      # negation    
    | NOT expr                                      # not
    | expr op=(MUL|DIV|MOD) expr                    # mulDivMod
    | expr op=(ADD|SUB|CONCAT) expr                 # addSubConcat
    | expr op=(GREATER|LESSER) expr                 # relation
    | expr op=(EQUAL|NOT_EQUAL) expr                # comparison
    | expr AND expr                                 # logicAnd
    | expr OR expr                                  # logicOr
    | <assoc=right> IDENTIFIER '=' expr             # assignment  
    | '(' expr ')'                                  # parens      
    | INT                                           # int
    | FLOAT                                         # float
    | BOOL                                          # bool
    | STRING                                        # string
    | IDENTIFIER                                    # id
    ;

primitiveType
    : type='int'
    | type='float'
    | type='bool'
    | type='string'
    ;

// Terminals

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
CONCAT: '.';
GREATER: '>';
LESSER: '<';
EQUAL: '==';
NOT_EQUAL: '!=';
NOT: '!';
AND: '&&';
OR: '||';
  
FLOAT: [0-9]+ '.' [0-9]+;
INT: [0-9]+;
BOOL: 'true' | 'false';
STRING: '"' (~["'\\\r\n])* '"';
IDENTIFIER: [a-zA-Z][a-zA-Z0-9]*;

COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\n\r]+ -> skip;
