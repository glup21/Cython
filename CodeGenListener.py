# Generated from ProjectGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ProjectGrammarParser import ProjectGrammarParser
else:
    from ProjectGrammarParser import ProjectGrammarParser
from VariableTypes import Type

# This class defines a complete listener for a parse tree produced by ProjectGrammarParser.
class CodeGenListener(ParseTreeListener):

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

        self.label_id = 0
        self.if_stack = []
        self.pending = {}

    def addLine(self, s : str):
        self.result += s + '\n'

    def getLabelId(self):
        res = self.label_id
        self.label_id += 1

        return res

    def enterEveryRule(self, ctx):
        if ctx in self.pending:
            for line in self.pending[ctx]:
                self.addLine(line)
            del self.pending[ctx]
        return super().enterEveryRule(ctx)

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
        res_type = Type.stringToType(ctx.primitiveType().getText())
        value = res_type.getDefaultValue()

        if res_type == Type.BOOL:
            value = 'true' if value == True else 'false'

        for id in ctx.IDENTIFIER():
            name = id.getText()
            self.types_table[name] = res_type 
            
            self.addLine(f'push {res_type.toSuffix()} {value}')
            self.addLine(f'save {name}')


    # Enter a parse tree produced by ProjectGrammarParser#printExpr.
    def enterPrintExpr(self, ctx:ProjectGrammarParser.PrintExprContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#printExpr.
    def exitPrintExpr(self, ctx:ProjectGrammarParser.PrintExprContext):
        self.addLine(f'pop')


    # Enter a parse tree produced by ProjectGrammarParser#read.
    def enterRead(self, ctx:ProjectGrammarParser.ReadContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#read.
    def exitRead(self, ctx:ProjectGrammarParser.ReadContext):
        for id in ctx.IDENTIFIER():
            self.addLine(f'read {self.types_table[id.getText()].toSuffix()}')
            self.addLine(f'save {id.getText()}')


    # Enter a parse tree produced by ProjectGrammarParser#write.
    def enterWrite(self, ctx:ProjectGrammarParser.WriteContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#write.
    def exitWrite(self, ctx:ProjectGrammarParser.WriteContext):
        self.addLine(f'print {len(ctx.expr())}')
            


    # Enter a parse tree produced by ProjectGrammarParser#statementsBlock.
    def enterStatementsBlock(self, ctx:ProjectGrammarParser.StatementsBlockContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#statementsBlock.
    def exitStatementsBlock(self, ctx:ProjectGrammarParser.StatementsBlockContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#ifStatement.
    def enterIfStatement(self, ctx:ProjectGrammarParser.IfStatementContext):
        false_id = self.getLabelId()
        end_id = self.getLabelId()
        self.if_stack.append((false_id, end_id))
        has_else = ctx.statement(1) is not None
        self.pending[ctx.statement(0)] = [f'fjmp {false_id}']
        if has_else:
            self.pending[ctx.statement(1)] = [f'jmp {end_id}', f'label {false_id}']

    # Exit a parse tree produced by ProjectGrammarParser#ifStatement.
    def exitIfStatement(self, ctx:ProjectGrammarParser.IfStatementContext):
        false_id, end_id = self.if_stack.pop()
        has_else = ctx.statement(1) is not None
        if has_else:
            self.addLine(f'label {end_id}')
        else:
            self.addLine(f'jmp {end_id}')
            self.addLine(f'label {false_id}')
            self.addLine(f'label {end_id}')

    # Enter a parse tree produced by ProjectGrammarParser#whileStatement.
    def enterWhileStatement(self, ctx:ProjectGrammarParser.WhileStatementContext):
        start_id = self.getLabelId()
        end_id = self.getLabelId()
        self.if_stack.append((start_id, end_id))

        self.addLine(f'label {start_id}')
       
        self.pending[ctx.statement()] = [f'fjmp {end_id}']

    def exitWhileStatement(self, ctx:ProjectGrammarParser.WhileStatementContext):
        start_id, end_id = self.if_stack.pop()
        self.addLine(f'jmp {start_id}')
        self.addLine(f'label {end_id}')


    # Enter a parse tree produced by ProjectGrammarParser#mulDivMod.
    def enterMulDivMod(self, ctx:ProjectGrammarParser.MulDivModContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#mulDivMod.
    def exitMulDivMod(self, ctx:ProjectGrammarParser.MulDivModContext):
        left = ctx.expr()[0]
        right = ctx.expr()[1]

        res_type = Type.FLOAT
        if self.nodes_table[left] == Type.INT and self.nodes_table[right] == Type.FLOAT:
            # Save Right to a variable
            self.addLine('save _tmp')

            # Convert Left to float
            self.addLine('itof')

            # Return Right back to stack
            self.addLine('load _tmp')

            res_type = Type.FLOAT

        elif self.nodes_table[left] == Type.FLOAT and self.nodes_table[right] == Type.INT:
            # Convert Right to float
            self.addLine('itof')
            res_type = Type.FLOAT

        elif self.nodes_table[left] == Type.INT and self.nodes_table[right] == Type.INT:
            res_type = Type.INT

        if ctx.op.text == '*':
            self.addLine(f'mul {res_type.toSuffix()}')
        elif ctx.op.text == '/':
            self.addLine(f'div {res_type.toSuffix()}')
        elif ctx.op.text == '%':
            self.addLine('mod')
            res_type = Type.INT

        self.nodes_table[ctx] = res_type


    # Enter a parse tree produced by ProjectGrammarParser#negation.
    def enterNegation(self, ctx:ProjectGrammarParser.NegationContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#negation.
    def exitNegation(self, ctx:ProjectGrammarParser.NegationContext):
        res_type = self.nodes_table[ctx.expr()]
        self.addLine(f'uminus {res_type.toSuffix()}')
        self.nodes_table[ctx] = res_type



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
        left = ctx.expr()[0]
        right = ctx.expr()[1]

        res_type = Type.FLOAT
        if self.nodes_table[left] == Type.INT and self.nodes_table[right] == Type.FLOAT:
            # Save Right to a variable
            self.addLine('save _tmp')

            # Convert Left to float
            self.addLine('itof')

            # Return Right back to stack
            self.addLine('load _tmp')

            res_type = Type.FLOAT

        elif self.nodes_table[left] == Type.FLOAT and self.nodes_table[right] == Type.INT:
            # Convert Right to float
            self.addLine('itof')
            res_type = Type.FLOAT

        elif self.nodes_table[left] == Type.INT and self.nodes_table[right] == Type.INT:
            res_type = Type.INT

        elif self.nodes_table[left] == Type.STRING and self.nodes_table[right] == Type.STRING:
            res_type = Type.STRING

        self.addLine(f'eq {res_type.toSuffix()}')
        if ctx.op.text == '!=':
            self.addLine('not')

        self.nodes_table[ctx] = Type.BOOL


    # Enter a parse tree produced by ProjectGrammarParser#bool.
    def enterBool(self, ctx:ProjectGrammarParser.BoolContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#bool.
    def exitBool(self, ctx:ProjectGrammarParser.BoolContext):
        value = ctx.getText()

        self.addLine(f'push B {value}')
        self.nodes_table[ctx] = Type.BOOL


    # Enter a parse tree produced by ProjectGrammarParser#string.
    def enterString(self, ctx:ProjectGrammarParser.StringContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#string.
    def exitString(self, ctx:ProjectGrammarParser.StringContext):
        value = ctx.getText()
        self.addLine(f'push S {value}')
        self.nodes_table[ctx] = Type.STRING


    # Enter a parse tree produced by ProjectGrammarParser#addSubConcat.
    def enterAddSubConcat(self, ctx:ProjectGrammarParser.AddSubConcatContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#addSubConcat.
    def exitAddSubConcat(self, ctx:ProjectGrammarParser.AddSubConcatContext):
        left = ctx.expr()[0]
        right = ctx.expr()[1]

        res_type = Type.FLOAT
        if self.nodes_table[left] == Type.INT and self.nodes_table[right] == Type.FLOAT:
            # Save Right to a variable
            self.addLine('save _tmp')

            # Convert Left to float
            self.addLine('itof')

            # Return Right back to stack
            self.addLine('load _tmp')

            res_type = Type.FLOAT

        elif self.nodes_table[left] == Type.FLOAT and self.nodes_table[right] == Type.INT:
            # Convert Right to float
            self.addLine('itof')
            res_type = Type.FLOAT

        elif self.nodes_table[left] == Type.INT and self.nodes_table[right] == Type.INT:
            res_type = Type.INT

        elif self.nodes_table[left] == Type.STRING and self.nodes_table[right] == Type.STRING:
            res_type = Type.STRING

        if res_type.isNumeric():
            if ctx.op.text == '+':
                self.addLine(f'add {res_type.toSuffix()}')
            elif ctx.op.text == '-':
                self.addLine(f'sub {res_type.toSuffix()}')
        elif res_type == Type.STRING:
            self.addLine(f'concat')

        self.nodes_table[ctx] = res_type


    # Enter a parse tree produced by ProjectGrammarParser#assignment.
    def enterAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#assignment.
    def exitAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        name = ctx.IDENTIFIER().getText()
        var_type = self.types_table[name]
        expr_type = self.nodes_table.get(ctx.expr())
        
        if var_type == Type.FLOAT and expr_type == Type.INT:
            self.addLine('itof')
        
        self.nodes_table[ctx] = var_type
        self.addLine(f'save {name}')
        self.addLine(f'load {name}') 
        


    # Enter a parse tree produced by ProjectGrammarParser#logicOr.
    def enterLogicOr(self, ctx:ProjectGrammarParser.LogicOrContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#logicOr.
    def exitLogicOr(self, ctx:ProjectGrammarParser.LogicOrContext):
        self.addLine('or')
        self.nodes_table[ctx] = Type.BOOL


    # Enter a parse tree produced by ProjectGrammarParser#float.
    def enterFloat(self, ctx:ProjectGrammarParser.FloatContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#float.
    def exitFloat(self, ctx:ProjectGrammarParser.FloatContext):
        value = float(ctx.getText())
        self.addLine(f'push F {value}')
        self.nodes_table[ctx] = Type.FLOAT


    # Enter a parse tree produced by ProjectGrammarParser#int.
    def enterInt(self, ctx:ProjectGrammarParser.IntContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#int.
    def exitInt(self, ctx:ProjectGrammarParser.IntContext):
        value = int(ctx.getText())
        self.addLine(f'push I {value}')
        self.nodes_table[ctx] = Type.INT


    # Enter a parse tree produced by ProjectGrammarParser#relation.
    def enterRelation(self, ctx:ProjectGrammarParser.RelationContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#relation.
    def exitRelation(self, ctx:ProjectGrammarParser.RelationContext):
        left = ctx.expr()[0]
        right = ctx.expr()[1]

        res_type = Type.FLOAT
        if self.nodes_table[left] == Type.INT and self.nodes_table[right] == Type.FLOAT:
            # Save Right to a variable
            self.addLine('save _tmp')

            # Convert Left to float
            self.addLine('itof')

            # Return Right back to stack
            self.addLine('load _tmp')

        elif self.nodes_table[left] == Type.FLOAT and self.nodes_table[right] == Type.INT:
            # Convert Right to float
            self.addLine('itof')
        elif self.nodes_table[left] == Type.INT and self.nodes_table[right] == Type.INT:
            res_type = Type.INT

        if ctx.op.text == '<':
            self.addLine(f'lt {res_type.toSuffix()}')

        if ctx.op.text == '>':
            self.addLine(f'gt {res_type.toSuffix()}')

        self.nodes_table[ctx] = Type.BOOL
        


    # Enter a parse tree produced by ProjectGrammarParser#not.
    def enterNot(self, ctx:ProjectGrammarParser.NotContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#not.
    def exitNot(self, ctx:ProjectGrammarParser.NotContext):
        self.nodes_table[ctx] = Type.BOOL
        self.addLine(f'not')

    # Enter a parse tree produced by ProjectGrammarParser#logicAnd.
    def enterLogicAnd(self, ctx:ProjectGrammarParser.LogicAndContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#logicAnd.
    def exitLogicAnd(self, ctx:ProjectGrammarParser.LogicAndContext):
        self.nodes_table[ctx] = Type.BOOL
        self.addLine(f'and')


    # Enter a parse tree produced by ProjectGrammarParser#id.
    def enterId(self, ctx:ProjectGrammarParser.IdContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#id.
    def exitId(self, ctx:ProjectGrammarParser.IdContext):
        name = ctx.IDENTIFIER().getText()
        self.nodes_table[ctx] = self.types_table[name]
        self.addLine(f'load {name}')


    # Enter a parse tree produced by ProjectGrammarParser#primitiveType.
    def enterPrimitiveType(self, ctx:ProjectGrammarParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#primitiveType.
    def exitPrimitiveType(self, ctx:ProjectGrammarParser.PrimitiveTypeContext):
        self.nodes_table[ctx] = Type.stringToType(ctx.type_.text)



del ProjectGrammarParser