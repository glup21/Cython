# Generated from ProjectGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ProjectGrammarParser import ProjectGrammarParser
else:
    from ProjectGrammarParser import ProjectGrammarParser

# This class defines a complete generic visitor for a parse tree produced by ProjectGrammarParser.

class ProjectGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ProjectGrammarParser#prog.
    def visitProg(self, ctx:ProjectGrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#emptyStatement.
    def visitEmptyStatement(self, ctx:ProjectGrammarParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#declaration.
    def visitDeclaration(self, ctx:ProjectGrammarParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#printExpr.
    def visitPrintExpr(self, ctx:ProjectGrammarParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#read.
    def visitRead(self, ctx:ProjectGrammarParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#write.
    def visitWrite(self, ctx:ProjectGrammarParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#statementsBlock.
    def visitStatementsBlock(self, ctx:ProjectGrammarParser.StatementsBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#ifStatement.
    def visitIfStatement(self, ctx:ProjectGrammarParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#whileStatement.
    def visitWhileStatement(self, ctx:ProjectGrammarParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#mulDivMod.
    def visitMulDivMod(self, ctx:ProjectGrammarParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#negation.
    def visitNegation(self, ctx:ProjectGrammarParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#parens.
    def visitParens(self, ctx:ProjectGrammarParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#comparison.
    def visitComparison(self, ctx:ProjectGrammarParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#bool.
    def visitBool(self, ctx:ProjectGrammarParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#string.
    def visitString(self, ctx:ProjectGrammarParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#addSubConcat.
    def visitAddSubConcat(self, ctx:ProjectGrammarParser.AddSubConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#assignment.
    def visitAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#logicOr.
    def visitLogicOr(self, ctx:ProjectGrammarParser.LogicOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#float.
    def visitFloat(self, ctx:ProjectGrammarParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#int.
    def visitInt(self, ctx:ProjectGrammarParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#relation.
    def visitRelation(self, ctx:ProjectGrammarParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#not.
    def visitNot(self, ctx:ProjectGrammarParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#logicAnd.
    def visitLogicAnd(self, ctx:ProjectGrammarParser.LogicAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#id.
    def visitId(self, ctx:ProjectGrammarParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#primitiveType.
    def visitPrimitiveType(self, ctx:ProjectGrammarParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)



del ProjectGrammarParser