from antlr4 import *
from ProjectGrammarLexer import ProjectGrammarLexer
from ProjectGrammarParser import ProjectGrammarParser
from ProjectGrammarVisitor import ProjectGrammarVisitor
from TypeCheckListener import TypeCheckListener
from CodeGenListener import CodeGenListener
import sys

def main():

    with open(sys.argv[1], 'r') as f: 
        input_text = f.read()

    input_stream = InputStream(input_text)
    lexer = ProjectGrammarLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ProjectGrammarParser(tokens)

    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors found, stopping.")
        sys.exit(1)

    listener = TypeCheckListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    for error in listener.errors:
        print('\033[91m', 'Type error:', error )

    if len(listener.errors) <= 0:
        listener = CodeGenListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        output = open('instructions.txt', 'w')
        output.write(listener.result)
        output.close()

if __name__ == '__main__':
    main()
