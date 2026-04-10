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


    # Visit a parse tree produced by ProjectGrammarParser#statement.
    def visitStatement(self, ctx:ProjectGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#expr.
    def visitExpr(self, ctx:ProjectGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#expr_list.
    def visitExpr_list(self, ctx:ProjectGrammarParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#assignment.
    def visitAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#logic.
    def visitLogic(self, ctx:ProjectGrammarParser.LogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#equality.
    def visitEquality(self, ctx:ProjectGrammarParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#relation.
    def visitRelation(self, ctx:ProjectGrammarParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#concat.
    def visitConcat(self, ctx:ProjectGrammarParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#add.
    def visitAdd(self, ctx:ProjectGrammarParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#mul.
    def visitMul(self, ctx:ProjectGrammarParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#unary.
    def visitUnary(self, ctx:ProjectGrammarParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#primary.
    def visitPrimary(self, ctx:ProjectGrammarParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#id_list.
    def visitId_list(self, ctx:ProjectGrammarParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#var.
    def visitVar(self, ctx:ProjectGrammarParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#read.
    def visitRead(self, ctx:ProjectGrammarParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#write.
    def visitWrite(self, ctx:ProjectGrammarParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#if.
    def visitIf(self, ctx:ProjectGrammarParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#while.
    def visitWhile(self, ctx:ProjectGrammarParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#condition.
    def visitCondition(self, ctx:ProjectGrammarParser.ConditionContext):
        return self.visitChildren(ctx)



del ProjectGrammarParser