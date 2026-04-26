from antlr4 import *
from ProjectGrammarLexer import ProjectGrammarLexer
from ProjectGrammarParser import ProjectGrammarParser
from ProjectGrammarVisitor import ProjectGrammarVisitor
from ProjectGrammarListener import ProjectGrammarListener
import sys

def main():

    with open(sys.argv[1], 'r') as f: 
        input_text = f.read()

    input_stream = InputStream(input_text)
    lexer = ProjectGrammarLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ProjectGrammarParser(tokens)

    tree = parser.prog()
    # visitor = PLC_Lab8_exprVisitor()
    # results = visitor.visit(tree)

    # for r in results:
    #     print(r)

    listener = ProjectGrammarListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # for key, value in listener.variables.items():
    #     print(f"{key}: {value}")

    print(listener.result)

    output = open('instructions.txt', 'w')
    output.write(listener.result)
    output.close()

if __name__ == '__main__':
    main()
