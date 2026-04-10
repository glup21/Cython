# Generated from ProjectGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ProjectGrammarParser import ProjectGrammarParser
else:
    from ProjectGrammarParser import ProjectGrammarParser

# This class defines a complete listener for a parse tree produced by ProjectGrammarParser.
class ProjectGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ProjectGrammarParser#prog.
    def enterProg(self, ctx:ProjectGrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#prog.
    def exitProg(self, ctx:ProjectGrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#statement.
    def enterStatement(self, ctx:ProjectGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#statement.
    def exitStatement(self, ctx:ProjectGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#expr.
    def enterExpr(self, ctx:ProjectGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#expr.
    def exitExpr(self, ctx:ProjectGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#expr_list.
    def enterExpr_list(self, ctx:ProjectGrammarParser.Expr_listContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#expr_list.
    def exitExpr_list(self, ctx:ProjectGrammarParser.Expr_listContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#assignment.
    def enterAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#assignment.
    def exitAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#logic.
    def enterLogic(self, ctx:ProjectGrammarParser.LogicContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#logic.
    def exitLogic(self, ctx:ProjectGrammarParser.LogicContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#equality.
    def enterEquality(self, ctx:ProjectGrammarParser.EqualityContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#equality.
    def exitEquality(self, ctx:ProjectGrammarParser.EqualityContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#relation.
    def enterRelation(self, ctx:ProjectGrammarParser.RelationContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#relation.
    def exitRelation(self, ctx:ProjectGrammarParser.RelationContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#concat.
    def enterConcat(self, ctx:ProjectGrammarParser.ConcatContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#concat.
    def exitConcat(self, ctx:ProjectGrammarParser.ConcatContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#add.
    def enterAdd(self, ctx:ProjectGrammarParser.AddContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#add.
    def exitAdd(self, ctx:ProjectGrammarParser.AddContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#mul.
    def enterMul(self, ctx:ProjectGrammarParser.MulContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#mul.
    def exitMul(self, ctx:ProjectGrammarParser.MulContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#unary.
    def enterUnary(self, ctx:ProjectGrammarParser.UnaryContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#unary.
    def exitUnary(self, ctx:ProjectGrammarParser.UnaryContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#primary.
    def enterPrimary(self, ctx:ProjectGrammarParser.PrimaryContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#primary.
    def exitPrimary(self, ctx:ProjectGrammarParser.PrimaryContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#id_list.
    def enterId_list(self, ctx:ProjectGrammarParser.Id_listContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#id_list.
    def exitId_list(self, ctx:ProjectGrammarParser.Id_listContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#var.
    def enterVar(self, ctx:ProjectGrammarParser.VarContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#var.
    def exitVar(self, ctx:ProjectGrammarParser.VarContext):
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


    # Enter a parse tree produced by ProjectGrammarParser#if.
    def enterIf(self, ctx:ProjectGrammarParser.IfContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#if.
    def exitIf(self, ctx:ProjectGrammarParser.IfContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#while.
    def enterWhile(self, ctx:ProjectGrammarParser.WhileContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#while.
    def exitWhile(self, ctx:ProjectGrammarParser.WhileContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#condition.
    def enterCondition(self, ctx:ProjectGrammarParser.ConditionContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#condition.
    def exitCondition(self, ctx:ProjectGrammarParser.ConditionContext):
        pass



del ProjectGrammarParser