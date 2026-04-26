# Generated from ProjectGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,119,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,1,1,1,1,1,1,
        1,1,1,1,5,1,43,8,1,10,1,12,1,46,9,1,1,1,1,1,1,1,1,1,4,1,52,8,1,11,
        1,12,1,53,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,65,8,1,1,1,1,1,
        1,1,1,1,1,1,1,1,3,1,73,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,92,8,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,112,8,2,10,2,
        12,2,115,9,2,1,3,1,3,1,3,0,1,4,4,0,2,4,6,0,5,1,0,19,21,2,0,17,18,
        22,22,1,0,23,24,1,0,25,26,1,0,13,16,141,0,9,1,0,0,0,2,72,1,0,0,0,
        4,91,1,0,0,0,6,116,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,
        0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,73,5,1,0,0,14,15,3,
        6,3,0,15,20,5,34,0,0,16,17,5,2,0,0,17,19,5,34,0,0,18,16,1,0,0,0,
        19,22,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,23,1,0,0,0,22,20,1,
        0,0,0,23,24,5,1,0,0,24,73,1,0,0,0,25,26,3,4,2,0,26,27,5,1,0,0,27,
        73,1,0,0,0,28,29,5,3,0,0,29,34,5,34,0,0,30,31,5,2,0,0,31,33,5,34,
        0,0,32,30,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,
        1,0,0,0,36,34,1,0,0,0,37,73,5,1,0,0,38,39,5,4,0,0,39,44,3,4,2,0,
        40,41,5,2,0,0,41,43,3,4,2,0,42,40,1,0,0,0,43,46,1,0,0,0,44,42,1,
        0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,47,48,5,1,0,0,48,
        73,1,0,0,0,49,51,5,5,0,0,50,52,3,2,1,0,51,50,1,0,0,0,52,53,1,0,0,
        0,53,51,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,6,0,0,56,73,
        1,0,0,0,57,58,5,7,0,0,58,59,5,8,0,0,59,60,3,4,2,0,60,61,5,9,0,0,
        61,64,3,2,1,0,62,63,5,10,0,0,63,65,3,2,1,0,64,62,1,0,0,0,64,65,1,
        0,0,0,65,73,1,0,0,0,66,67,5,11,0,0,67,68,5,8,0,0,68,69,3,4,2,0,69,
        70,5,9,0,0,70,71,3,2,1,0,71,73,1,0,0,0,72,13,1,0,0,0,72,14,1,0,0,
        0,72,25,1,0,0,0,72,28,1,0,0,0,72,38,1,0,0,0,72,49,1,0,0,0,72,57,
        1,0,0,0,72,66,1,0,0,0,73,3,1,0,0,0,74,75,6,2,-1,0,75,76,5,18,0,0,
        76,92,3,4,2,15,77,78,5,27,0,0,78,92,3,4,2,14,79,80,5,34,0,0,80,81,
        5,12,0,0,81,92,3,4,2,7,82,83,5,8,0,0,83,84,3,4,2,0,84,85,5,9,0,0,
        85,92,1,0,0,0,86,92,5,31,0,0,87,92,5,30,0,0,88,92,5,32,0,0,89,92,
        5,33,0,0,90,92,5,34,0,0,91,74,1,0,0,0,91,77,1,0,0,0,91,79,1,0,0,
        0,91,82,1,0,0,0,91,86,1,0,0,0,91,87,1,0,0,0,91,88,1,0,0,0,91,89,
        1,0,0,0,91,90,1,0,0,0,92,113,1,0,0,0,93,94,10,13,0,0,94,95,7,0,0,
        0,95,112,3,4,2,14,96,97,10,12,0,0,97,98,7,1,0,0,98,112,3,4,2,13,
        99,100,10,11,0,0,100,101,7,2,0,0,101,112,3,4,2,12,102,103,10,10,
        0,0,103,104,7,3,0,0,104,112,3,4,2,11,105,106,10,9,0,0,106,107,5,
        28,0,0,107,112,3,4,2,10,108,109,10,8,0,0,109,110,5,29,0,0,110,112,
        3,4,2,9,111,93,1,0,0,0,111,96,1,0,0,0,111,99,1,0,0,0,111,102,1,0,
        0,0,111,105,1,0,0,0,111,108,1,0,0,0,112,115,1,0,0,0,113,111,1,0,
        0,0,113,114,1,0,0,0,114,5,1,0,0,0,115,113,1,0,0,0,116,117,7,4,0,
        0,117,7,1,0,0,0,10,11,20,34,44,53,64,72,91,111,113
    ]

class ProjectGrammarParser ( Parser ):

    grammarFileName = "ProjectGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'read'", "'write'", "'{'", 
                     "'}'", "'if'", "'('", "')'", "'else'", "'while'", "'='", 
                     "'int'", "'float'", "'bool'", "'string'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'.'", "'>'", "'<'", "'=='", "'!='", 
                     "'!'", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ADD", "SUB", "MUL", "DIV", "MOD", "CONCAT", 
                      "GREATER", "LESSER", "EQUAL", "NOT_EQUAL", "NOT", 
                      "AND", "OR", "FLOAT", "INT", "BOOL", "STRING", "IDENTIFIER", 
                      "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_primitiveType = 3

    ruleNames =  [ "prog", "statement", "expr", "primitiveType" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    ADD=17
    SUB=18
    MUL=19
    DIV=20
    MOD=21
    CONCAT=22
    GREATER=23
    LESSER=24
    EQUAL=25
    NOT_EQUAL=26
    NOT=27
    AND=28
    OR=29
    FLOAT=30
    INT=31
    BOOL=32
    STRING=33
    IDENTIFIER=34
    COMMENT=35
    WS=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ProjectGrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33420601786) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)

        def statement(self):
            return self.getTypedRuleContext(ProjectGrammarParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)


    class EmptyStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStatement" ):
                return visitor.visitEmptyStatement(self)
            else:
                return visitor.visitChildren(self)


    class ReadContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectGrammarParser.IDENTIFIER)
            else:
                return self.getToken(ProjectGrammarParser.IDENTIFIER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)


    class StatementsBlockContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementsBlock" ):
                listener.enterStatementsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementsBlock" ):
                listener.exitStatementsBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementsBlock" ):
                return visitor.visitStatementsBlock(self)
            else:
                return visitor.visitChildren(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitiveType(self):
            return self.getTypedRuleContext(ProjectGrammarParser.PrimitiveTypeContext,0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectGrammarParser.IDENTIFIER)
            else:
                return self.getToken(ProjectGrammarParser.IDENTIFIER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class WriteContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = ProjectGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = ProjectGrammarParser.EmptyStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(ProjectGrammarParser.T__0)
                pass
            elif token in [13, 14, 15, 16]:
                localctx = ProjectGrammarParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.primitiveType()
                self.state = 15
                self.match(ProjectGrammarParser.IDENTIFIER)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 16
                    self.match(ProjectGrammarParser.T__1)
                    self.state = 17
                    self.match(ProjectGrammarParser.IDENTIFIER)
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 23
                self.match(ProjectGrammarParser.T__0)
                pass
            elif token in [8, 18, 27, 30, 31, 32, 33, 34]:
                localctx = ProjectGrammarParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.expr(0)
                self.state = 26
                self.match(ProjectGrammarParser.T__0)
                pass
            elif token in [3]:
                localctx = ProjectGrammarParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.match(ProjectGrammarParser.T__2)
                self.state = 29
                self.match(ProjectGrammarParser.IDENTIFIER)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 30
                    self.match(ProjectGrammarParser.T__1)
                    self.state = 31
                    self.match(ProjectGrammarParser.IDENTIFIER)
                    self.state = 36
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 37
                self.match(ProjectGrammarParser.T__0)
                pass
            elif token in [4]:
                localctx = ProjectGrammarParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 38
                self.match(ProjectGrammarParser.T__3)
                self.state = 39
                self.expr(0)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 40
                    self.match(ProjectGrammarParser.T__1)
                    self.state = 41
                    self.expr(0)
                    self.state = 46
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 47
                self.match(ProjectGrammarParser.T__0)
                pass
            elif token in [5]:
                localctx = ProjectGrammarParser.StatementsBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 49
                self.match(ProjectGrammarParser.T__4)
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 50
                    self.statement()
                    self.state = 53 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33420601786) != 0)):
                        break

                self.state = 55
                self.match(ProjectGrammarParser.T__5)
                pass
            elif token in [7]:
                localctx = ProjectGrammarParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 57
                self.match(ProjectGrammarParser.T__6)
                self.state = 58
                self.match(ProjectGrammarParser.T__7)
                self.state = 59
                self.expr(0)
                self.state = 60
                self.match(ProjectGrammarParser.T__8)
                self.state = 61
                self.statement()
                self.state = 64
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 62
                    self.match(ProjectGrammarParser.T__9)
                    self.state = 63
                    self.statement()


                pass
            elif token in [11]:
                localctx = ProjectGrammarParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 66
                self.match(ProjectGrammarParser.T__10)
                self.state = 67
                self.match(ProjectGrammarParser.T__7)
                self.state = 68
                self.expr(0)
                self.state = 69
                self.match(ProjectGrammarParser.T__8)
                self.state = 70
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def MUL(self):
            return self.getToken(ProjectGrammarParser.MUL, 0)
        def DIV(self):
            return self.getToken(ProjectGrammarParser.DIV, 0)
        def MOD(self):
            return self.getToken(ProjectGrammarParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivMod" ):
                listener.enterMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivMod" ):
                listener.exitMulDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivMod" ):
                return visitor.visitMulDivMod(self)
            else:
                return visitor.visitChildren(self)


    class NegationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(ProjectGrammarParser.SUB, 0)
        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation" ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation" ):
                listener.exitNegation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation" ):
                return visitor.visitNegation(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def EQUAL(self):
            return self.getToken(ProjectGrammarParser.EQUAL, 0)
        def NOT_EQUAL(self):
            return self.getToken(ProjectGrammarParser.NOT_EQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(ProjectGrammarParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ProjectGrammarParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class AddSubConcatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def ADD(self):
            return self.getToken(ProjectGrammarParser.ADD, 0)
        def SUB(self):
            return self.getToken(ProjectGrammarParser.SUB, 0)
        def CONCAT(self):
            return self.getToken(ProjectGrammarParser.CONCAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubConcat" ):
                listener.enterAddSubConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubConcat" ):
                listener.exitAddSubConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubConcat" ):
                return visitor.visitAddSubConcat(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ProjectGrammarParser.IDENTIFIER, 0)
        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class LogicOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def OR(self):
            return self.getToken(ProjectGrammarParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicOr" ):
                listener.enterLogicOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicOr" ):
                listener.exitLogicOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOr" ):
                return visitor.visitLogicOr(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(ProjectGrammarParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ProjectGrammarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class RelationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def GREATER(self):
            return self.getToken(ProjectGrammarParser.GREATER, 0)
        def LESSER(self):
            return self.getToken(ProjectGrammarParser.LESSER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)


    class NotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(ProjectGrammarParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class LogicAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def AND(self):
            return self.getToken(ProjectGrammarParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicAnd" ):
                listener.enterLogicAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicAnd" ):
                listener.exitLogicAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicAnd" ):
                return visitor.visitLogicAnd(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ProjectGrammarParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ProjectGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = ProjectGrammarParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 75
                self.match(ProjectGrammarParser.SUB)
                self.state = 76
                self.expr(15)
                pass

            elif la_ == 2:
                localctx = ProjectGrammarParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 77
                self.match(ProjectGrammarParser.NOT)
                self.state = 78
                self.expr(14)
                pass

            elif la_ == 3:
                localctx = ProjectGrammarParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 79
                self.match(ProjectGrammarParser.IDENTIFIER)
                self.state = 80
                self.match(ProjectGrammarParser.T__11)
                self.state = 81
                self.expr(7)
                pass

            elif la_ == 4:
                localctx = ProjectGrammarParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 82
                self.match(ProjectGrammarParser.T__7)
                self.state = 83
                self.expr(0)
                self.state = 84
                self.match(ProjectGrammarParser.T__8)
                pass

            elif la_ == 5:
                localctx = ProjectGrammarParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 86
                self.match(ProjectGrammarParser.INT)
                pass

            elif la_ == 6:
                localctx = ProjectGrammarParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 87
                self.match(ProjectGrammarParser.FLOAT)
                pass

            elif la_ == 7:
                localctx = ProjectGrammarParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 88
                self.match(ProjectGrammarParser.BOOL)
                pass

            elif la_ == 8:
                localctx = ProjectGrammarParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 89
                self.match(ProjectGrammarParser.STRING)
                pass

            elif la_ == 9:
                localctx = ProjectGrammarParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 90
                self.match(ProjectGrammarParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 113
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 111
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = ProjectGrammarParser.MulDivModContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 93
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 94
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 95
                        self.expr(14)
                        pass

                    elif la_ == 2:
                        localctx = ProjectGrammarParser.AddSubConcatContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 96
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 97
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4587520) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 98
                        self.expr(13)
                        pass

                    elif la_ == 3:
                        localctx = ProjectGrammarParser.RelationContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 99
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 100
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 101
                        self.expr(12)
                        pass

                    elif la_ == 4:
                        localctx = ProjectGrammarParser.ComparisonContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 102
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 103
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 104
                        self.expr(11)
                        pass

                    elif la_ == 5:
                        localctx = ProjectGrammarParser.LogicAndContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 105
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 106
                        self.match(ProjectGrammarParser.AND)
                        self.state = 107
                        self.expr(10)
                        pass

                    elif la_ == 6:
                        localctx = ProjectGrammarParser.LogicOrContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 108
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 109
                        self.match(ProjectGrammarParser.OR)
                        self.state = 110
                        self.expr(9)
                        pass

             
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = ProjectGrammarParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         




