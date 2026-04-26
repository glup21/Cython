# Generated from ProjectGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ProjectGrammarParser import ProjectGrammarParser
else:
    from ProjectGrammarParser import ProjectGrammarParser
from enum import Enum

class Type(Enum):
    INT = 0
    FLOAT = 1
    STRING = 2
    BOOL = 3

    @staticmethod
    def stringToType(s):
        if s == 'int':
            return Type.INT
        if s == 'float':
            return Type.FLOAT
        if s == 'string':
            return Type.STRING
        if s == 'bool':
            return Type.BOOL

        raise Exception(f"Unknown type: {s}")
    
def parseType(v):
    if type(v) == float:
        return Type.FLOAT
    if type(v) == int:
        return Type.INT
    if type(v) == str:
        return Type.STRING
    if type(v) == bool:
        return Type.BOOL

# This class defines a complete listener for a parse tree produced by ProjectGrammarParser.
class ProjectGrammarListener(ParseTreeListener):

    def __init__(self):
        # For variable types - string : enum 
        self.types_table = {}

        # For variable values - string : object
        self.var_values = {}

        # For nodes types - ctx : enum
        self.nodes_table = {}

        # For nodes values - ctx : object
        self.nodes_values = {}

        # Output instructions
        self.result = ''

        self.type_exceptions = {}


    # Enter a parse tree produced by ProjectGrammarParser#prog.
    def enterProg(self, ctx:ProjectGrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#prog.
    def exitProg(self, ctx:ProjectGrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#emptyStatement.
    def enterEmptyStatement(self, ctx:ProjectGrammarParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#emptyStatement.
    def exitEmptyStatement(self, ctx:ProjectGrammarParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#declaration.
    def enterDeclaration(self, ctx:ProjectGrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#declaration.
    def exitDeclaration(self, ctx:ProjectGrammarParser.DeclarationContext):
        type = Type.stringToType(ctx.primitiveType().getText())
        name = ctx.getText()

        if name in self.types_table:
            self.errors.append(f'{ctx.start.line}:{ctx.start.column} Variable {name} is already declared!')
            return 

        for id in ctx.IDENTIFIER():
            id_type = Type.parseType(id.getText())


    # Enter a parse tree produced by ProjectGrammarParser#printExpr.
    def enterPrintExpr(self, ctx:ProjectGrammarParser.PrintExprContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#printExpr.
    def exitPrintExpr(self, ctx:ProjectGrammarParser.PrintExprContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#read.
    def enterRead(self, ctx:ProjectGrammarParser.ReadContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#read.
    def exitRead(self, ctx:ProjectGrammarParser.ReadContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#write.
    def enterWrite(self, ctx:ProjectGrammarParser.WriteContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#write.
    def exitWrite(self, ctx:ProjectGrammarParser.WriteContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#statementsBlock.
    def enterStatementsBlock(self, ctx:ProjectGrammarParser.StatementsBlockContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#statementsBlock.
    def exitStatementsBlock(self, ctx:ProjectGrammarParser.StatementsBlockContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#ifStatement.
    def enterIfStatement(self, ctx:ProjectGrammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#ifStatement.
    def exitIfStatement(self, ctx:ProjectGrammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#whileStatement.
    def enterWhileStatement(self, ctx:ProjectGrammarParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#whileStatement.
    def exitWhileStatement(self, ctx:ProjectGrammarParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#mulDivMod.
    def enterMulDivMod(self, ctx:ProjectGrammarParser.MulDivModContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#mulDivMod.
    def exitMulDivMod(self, ctx:ProjectGrammarParser.MulDivModContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#negation.
    def enterNegation(self, ctx:ProjectGrammarParser.NegationContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#negation.
    def exitNegation(self, ctx:ProjectGrammarParser.NegationContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#parens.
    def enterParens(self, ctx:ProjectGrammarParser.ParensContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#parens.
    def exitParens(self, ctx:ProjectGrammarParser.ParensContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#comparison.
    def enterComparison(self, ctx:ProjectGrammarParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#comparison.
    def exitComparison(self, ctx:ProjectGrammarParser.ComparisonContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#bool.
    def enterBool(self, ctx:ProjectGrammarParser.BoolContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#bool.
    def exitBool(self, ctx:ProjectGrammarParser.BoolContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#string.
    def enterString(self, ctx:ProjectGrammarParser.StringContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#string.
    def exitString(self, ctx:ProjectGrammarParser.StringContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#addSubConcat.
    def enterAddSubConcat(self, ctx:ProjectGrammarParser.AddSubConcatContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#addSubConcat.
    def exitAddSubConcat(self, ctx:ProjectGrammarParser.AddSubConcatContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#assignment.
    def enterAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#assignment.
    def exitAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#logicOr.
    def enterLogicOr(self, ctx:ProjectGrammarParser.LogicOrContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#logicOr.
    def exitLogicOr(self, ctx:ProjectGrammarParser.LogicOrContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#float.
    def enterFloat(self, ctx:ProjectGrammarParser.FloatContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#float.
    def exitFloat(self, ctx:ProjectGrammarParser.FloatContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#int.
    def enterInt(self, ctx:ProjectGrammarParser.IntContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#int.
    def exitInt(self, ctx:ProjectGrammarParser.IntContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#relation.
    def enterRelation(self, ctx:ProjectGrammarParser.RelationContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#relation.
    def exitRelation(self, ctx:ProjectGrammarParser.RelationContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#not.
    def enterNot(self, ctx:ProjectGrammarParser.NotContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#not.
    def exitNot(self, ctx:ProjectGrammarParser.NotContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#logicAnd.
    def enterLogicAnd(self, ctx:ProjectGrammarParser.LogicAndContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#logicAnd.
    def exitLogicAnd(self, ctx:ProjectGrammarParser.LogicAndContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#id.
    def enterId(self, ctx:ProjectGrammarParser.IdContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#id.
    def exitId(self, ctx:ProjectGrammarParser.IdContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#primitiveType.
    def enterPrimitiveType(self, ctx:ProjectGrammarParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#primitiveType.
    def exitPrimitiveType(self, ctx:ProjectGrammarParser.PrimitiveTypeContext):
        pass



del ProjectGrammarParser