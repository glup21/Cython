# Generated from ProjectGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ProjectGrammarParser import ProjectGrammarParser
else:
    from ProjectGrammarParser import ProjectGrammarParser

from VariableTypes import Type

# This class defines a complete listener for a parse tree produced by ProjectGrammarParser.
class TypeCheckListener(ParseTreeListener):

    def __init__(self):
        # For variable types - string : enum 
        self.types_table = {}

        # For variable values - string : object
        self.var_values = {}

        # For nodes types - ctx : enum
        self.nodes_table = {}

        # For nodes values - ctx : object
        self.nodes_values = {}

        self.errors = []

    def addError(self, ctx, message):
        self.errors.append(f'{ctx.start.line}:{ctx.start.column} {message}')

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
        for id in ctx.IDENTIFIER():
            name = id.getText()
            if name in self.types_table:
                self.addError(ctx, f'Variable {name} is already declared.')
            else:
                self.types_table[name] = type
                self.nodes_table[ctx] = type

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
        cond_type = self.nodes_table.get(ctx.expr())
        if cond_type != Type.BOOL:
            self.addError(ctx, 'If condition must be bool.')


    # Enter a parse tree produced by ProjectGrammarParser#whileStatement.
    def enterWhileStatement(self, ctx:ProjectGrammarParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#whileStatement.
    def exitWhileStatement(self, ctx:ProjectGrammarParser.WhileStatementContext):
        cond_type = self.nodes_table.get(ctx.expr())
        if cond_type != Type.BOOL:
            self.addError(ctx, 'While condition must be bool.')


    # Enter a parse tree produced by ProjectGrammarParser#mulDivMod.
    def enterMulDivMod(self, ctx:ProjectGrammarParser.MulDivModContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#mulDivMod.
    def exitMulDivMod(self, ctx:ProjectGrammarParser.MulDivModContext):
        left = ctx.expr()[0]
        right = ctx.expr()[1]

        left_type = self.nodes_table[left]
        right_type = self.nodes_table[right]

        if ctx.op.text == '%':
            if left_type != Type.INT or right_type != Type.INT:
                self.addError(ctx, 'Operands in MOD operation must be integers.')
        elif not left_type.isNumeric() or not right_type.isNumeric():
            self.addError(ctx, 'Operands in mathematical expressions must be numeric.')

        res_type = Type.INT if left_type == Type.INT and right_type == Type.INT else Type.FLOAT
        self.nodes_table[ctx] = res_type


    # Enter a parse tree produced by ProjectGrammarParser#negation.
    def enterNegation(self, ctx:ProjectGrammarParser.NegationContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#negation.
    def exitNegation(self, ctx:ProjectGrammarParser.NegationContext):
        expr_type = self.nodes_table.get(ctx.expr())  

        if not expr_type.isNumeric():
            self.addError(ctx, 'Negation can only be applied to numeric expressions.')

        self.nodes_table[ctx] = expr_type


    # Enter a parse tree produced by ProjectGrammarParser#parens.
    def enterParens(self, ctx:ProjectGrammarParser.ParensContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#parens.
    def exitParens(self, ctx:ProjectGrammarParser.ParensContext):
        self.nodes_table[ctx] = self.nodes_table[ctx.expr()]


    # Enter a parse tree produced by ProjectGrammarParser#comparison.
    def enterComparison(self, ctx:ProjectGrammarParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#comparison.
    def exitComparison(self, ctx:ProjectGrammarParser.ComparisonContext):
        left_type = self.nodes_table.get(ctx.expr(0))
        right_type = self.nodes_table.get(ctx.expr(1))
        
        allowed = (Type.INT, Type.FLOAT, Type.STRING)
        if left_type not in allowed or right_type not in allowed:
            self.addError(ctx, 'Comparison operands must be int, float or string.')

        if left_type != right_type:
            # allow int vs float
            if not ({left_type, right_type} == {Type.INT, Type.FLOAT} or {left_type, right_type} == {Type.FLOAT, Type.INT}):
                self.addError(ctx, 'Comparison operands must be the same type.')
        
        self.nodes_table[ctx] = Type.BOOL   


    # Enter a parse tree produced by ProjectGrammarParser#bool.
    def enterBool(self, ctx:ProjectGrammarParser.BoolContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#bool.
    def exitBool(self, ctx:ProjectGrammarParser.BoolContext):
        self.nodes_table[ctx] = Type.BOOL


    # Enter a parse tree produced by ProjectGrammarParser#string.
    def enterString(self, ctx:ProjectGrammarParser.StringContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#string.
    def exitString(self, ctx:ProjectGrammarParser.StringContext):
        self.nodes_table[ctx] = Type.STRING


    # Enter a parse tree produced by ProjectGrammarParser#addSubConcat.
    def enterAddSubConcat(self, ctx:ProjectGrammarParser.AddSubConcatContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#addSubConcat.
    def exitAddSubConcat(self, ctx:ProjectGrammarParser.AddSubConcatContext):
        left_type = self.nodes_table.get(ctx.expr(0))
        right_type = self.nodes_table.get(ctx.expr(1))
        op = ctx.op.text

        if op == '.':
            if left_type != Type.STRING or right_type != Type.STRING:
                self.addError(ctx, 'Concatenation requires string operands.')
            self.nodes_table[ctx] = Type.STRING
        else: 
            if not left_type.isNumeric() or not right_type.isNumeric():
                self.addError(ctx, 'Arithmetic requires numeric operands.')
            res_type = Type.FLOAT if Type.FLOAT in (left_type, right_type) else Type.INT
            self.nodes_table[ctx] = res_type


    # Enter a parse tree produced by ProjectGrammarParser#assignment.
    def enterAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#assignment.
    def exitAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        name = ctx.IDENTIFIER().getText()
        if name not in self.types_table:
            self.addError(ctx, f'Variable {name} is not declared.')
            return
        
        var_type = self.types_table[name]
        expr_type = self.nodes_table[ctx.expr()]
        
        if not (var_type == expr_type or (var_type == Type.FLOAT and expr_type == Type.INT)):
            self.addError(ctx, f'Cannot assign {expr_type} to variable of type {var_type}.')
        
        self.nodes_table[ctx] = var_type

    # Enter a parse tree produced by ProjectGrammarParser#logicOr.
    def enterLogicOr(self, ctx:ProjectGrammarParser.LogicOrContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#logicOr.
    def exitLogicOr(self, ctx:ProjectGrammarParser.LogicOrContext):
        left = ctx.expr()[0]
        right = ctx.expr()[1]

        left_type = self.nodes_table[left]
        right_type = self.nodes_table[right]

        if left_type != Type.BOOL or right_type != Type.BOOL:
            self.addError(ctx, 'Operands in boolean expressions must be bool.')

        self.nodes_table[ctx] = Type.BOOL


    # Enter a parse tree produced by ProjectGrammarParser#float.
    def enterFloat(self, ctx:ProjectGrammarParser.FloatContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#float.
    def exitFloat(self, ctx:ProjectGrammarParser.FloatContext):
        self.nodes_table[ctx] = Type.FLOAT


    # Enter a parse tree produced by ProjectGrammarParser#int.
    def enterInt(self, ctx:ProjectGrammarParser.IntContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#int.
    def exitInt(self, ctx:ProjectGrammarParser.IntContext):
        self.nodes_table[ctx] = Type.INT


    # Enter a parse tree produced by ProjectGrammarParser#relation.
    def enterRelation(self, ctx:ProjectGrammarParser.RelationContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#relation.
    def exitRelation(self, ctx:ProjectGrammarParser.RelationContext):
        left = ctx.expr()[0]
        right = ctx.expr()[1]

        left_type = self.nodes_table[left]
        right_type = self.nodes_table[right]

        if not left_type.isNumeric() or not right_type.isNumeric():
            self.addError(ctx, 'Operands in boolean expressions must be bool.')

        self.nodes_table[ctx] = Type.BOOL


    # Enter a parse tree produced by ProjectGrammarParser#not.
    def enterNot(self, ctx:ProjectGrammarParser.NotContext):
        pass


    # Exit a parse tree produced by ProjectGrammarParser#not.
    def exitNot(self, ctx:ProjectGrammarParser.NotContext):
        expr_type = self.nodes_table[ctx.expr().getText()]

        if expr_type != Type.BOOL:
            self.addError(ctx, 'Bool NOT operation is only applicable to boolean expressions.')

        self.nodes_table[ctx] = Type.BOOL


    # Enter a parse tree produced by ProjectGrammarParser#logicAnd.
    def enterLogicAnd(self, ctx:ProjectGrammarParser.LogicAndContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#logicAnd.
    def exitLogicAnd(self, ctx:ProjectGrammarParser.LogicAndContext):
        left = ctx.expr()[0]
        right = ctx.expr()[1]

        left_type = self.nodes_table[left]
        right_type = self.nodes_table[right]

        if left_type != Type.BOOL or right_type != Type.BOOL:
            self.addError(ctx, 'Operands in boolean expressions must be bool.')

        self.nodes_table[ctx] = Type.BOOL


    # Enter a parse tree produced by ProjectGrammarParser#id.
    def enterId(self, ctx:ProjectGrammarParser.IdContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#id.
    def exitId(self, ctx:ProjectGrammarParser.IdContext):
        name = ctx.IDENTIFIER().getText()
        if name not in self.types_table:
            self.addError(ctx, f'Variable {name} is not declared.')
            return
        self.nodes_table[ctx] = self.types_table[name]


    # Enter a parse tree produced by ProjectGrammarParser#primitiveType.
    def enterPrimitiveType(self, ctx:ProjectGrammarParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#primitiveType.
    def exitPrimitiveType(self, ctx:ProjectGrammarParser.PrimitiveTypeContext):
        pass



del ProjectGrammarParser