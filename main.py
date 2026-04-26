from antlr4 import *
from ProjectGrammarLexer import ProjectGrammarLexer
from ProjectGrammarParser import ProjectGrammarParser
from ProjectGrammarVisitor import ProjectGrammarVisitor
from TypeCheckListener import TypeCheckListener
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

    print(listener.errors)

    output = open('instructions.txt', 'w')
    output.write(listener.result)
    output.close()

if __name__ == '__main__':
    main()
