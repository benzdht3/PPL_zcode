from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program([self.visit(declare) for declare in ctx.declaration()])

    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        if ctx.var_declare():
            return self.visit(ctx.var_declare())
        return self.visit(ctx.func_declare())

    # Visit a parse tree produced by ZCodeParser#var_declare.
    def visitVar_declare(self, ctx:ZCodeParser.Var_declareContext):
        if ctx.normaldeclare():
            return self.visit(ctx.normaldeclare())
        elif ctx.arraydeclare():
            return self.visit(ctx.arraydeclare())
        return self.visit(ctx.vartypedeclare())

    # Visit a parse tree produced by ZCodeParser#normaldeclare.
    def visitNormaldeclare(self, ctx:ZCodeParser.NormaldeclareContext):
        if ctx.DYNTYPE():
            return VarDecl(Id(ctx.IDENTIFIER().getText()),None,ctx.DYNTYPE().getText(),self.visit(ctx.initialnormal()))
        return VarDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.var_type()),None,self.visit(ctx.initialnormal()))

    # Visit a parse tree produced by ZCodeParser#var_type.
    def visitVar_type(self, ctx:ZCodeParser.Var_typeContext):
        if ctx.NUMBER_TYPE():
            return NumberType()
        if ctx.STR_TYPE():
            return StringType()
        if ctx.BOOL_TYPE():
            return BoolType()

    # Visit a parse tree produced by ZCodeParser#initialnormal.
    def visitInitialnormal(self, ctx:ZCodeParser.InitialnormalContext):
        if ctx.ASSIGN():
            return self.visit(ctx.expr())
        return None

    # Visit a parse tree produced by ZCodeParser#arraydeclare.
    def visitArraydeclare(self, ctx:ZCodeParser.ArraydeclareContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()),ArrayType(self.visit(ctx.array()),self.visit(ctx.var_type())),None,self.visit(ctx.initialarray()))

    # Visit a parse tree produced by ZCodeParser#array.
    def visitArray(self, ctx:ZCodeParser.ArrayContext):
        return self.visit(ctx.dimension())

    # Visit a parse tree produced by ZCodeParser#dimension.
    def visitDimension(self, ctx:ZCodeParser.DimensionContext):
        return [NumberLiteral(ctx.NUMLIT().getText())] + self.visit(ctx.dimtail())

    # Visit a parse tree produced by ZCodeParser#dimtail.
    def visitDimtail(self, ctx:ZCodeParser.DimtailContext):
        if ctx.NUMLIT():
            return [NumberLiteral(ctx.NUMLIT().getText())] + self.visit(ctx.dimtail())
        return []

    # Visit a parse tree produced by ZCodeParser#initialarray.
    def visitInitialarray(self, ctx:ZCodeParser.InitialarrayContext):
        if ctx.ASSIGN():
            return self.visit(ctx.expr())
        return None
    
    # Visit a parse tree produced by ZCodeParser#arraylit.
    def visitArraylit(self, ctx:ZCodeParser.ArraylitContext):
        if ctx.literals():
            return ArrayLiteral([self.visit(ctx.literals())] + self.visit(ctx.arraylittail()))
        return ArrayLiteral([])

    # Visit a parse tree produced by ZCodeParser#arraylittail.
    def visitArraylittail(self, ctx:ZCodeParser.ArraylittailContext):
        if ctx.literals():
            return [self.visit(ctx.literals())] + self.visit(ctx.arraylittail())
        return []
        
    # Visit a parse tree produced by ZCodeParser#literals.
    def visitLiterals(self, ctx:ZCodeParser.LiteralsContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.NUMLIT():
            if ctx.SUBTR():
                return UnaryOp(ctx.SUBTR().getText(),NumberLiteral(float(ctx.NUMLIT().getText())))
            return NumberLiteral(float(ctx.NUMLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLIT():
            if ctx.BOOLIT().getText() == 'true':
                return BooleanLiteral(True)
            return BooleanLiteral(False)
        return self.visit(ctx.arraylit())

    # Visit a parse tree produced by ZCodeParser#vartypedeclare.
    def visitVartypedeclare(self, ctx:ZCodeParser.VartypedeclareContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()),None,ctx.VARTYPE().getText(),self.visit(ctx.expr()))

    # Visit a parse tree produced by ZCodeParser#func_declare.
    def visitFunc_declare(self, ctx:ZCodeParser.Func_declareContext):
        return FuncDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.param_here()),self.visit(ctx.bodyhere()))       

    # Visit a parse tree produced by ZCodeParser#param_here.
    def visitParam_here(self, ctx:ZCodeParser.Param_hereContext):
        if ctx.param_list():
            return self.visit(ctx.param_list())
        return []

    # Visit a parse tree produced by ZCodeParser#param_list.
    def visitParam_list(self, ctx:ZCodeParser.Param_listContext):
        return [self.visit(ctx.para())] + self.visit(ctx.paratail())

    # Visit a parse tree produced by ZCodeParser#paratail.
    def visitParatail(self, ctx:ZCodeParser.ParatailContext):
        if ctx.para():
            return [self.visit(ctx.para())] + self.visit(ctx.paratail())
        return []


    # Visit a parse tree produced by ZCodeParser#para.
    def visitPara(self, ctx:ZCodeParser.ParaContext):
        if ctx.array():
            return VarDecl(Id(ctx.IDENTIFIER().getText()),ArrayType(self.visit(ctx.array()),self.visit(ctx.var_type())),None,None)
        return VarDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.var_type()),None,None)

    # Visit a parse tree produced by ZCodeParser#bodyhere.
    def visitBodyhere(self, ctx:ZCodeParser.BodyhereContext):
        if ctx.body():
            return self.visit(ctx.body())
        return None

    # Visit a parse tree produced by ZCodeParser#body.
    def visitBody(self, ctx:ZCodeParser.BodyContext):
        if ctx.return_stm():
            return self.visit(ctx.return_stm())
        return self.visit(ctx.block())

    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        if ctx.var_declare():
            return self.visit(ctx.var_declare())
        elif ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.ifstm():
            return self.visit(ctx.ifstm())
        elif ctx.forstm():
            return self.visit(ctx.forstm())
        elif ctx.break_stm():
            return self.visit(ctx.break_stm())
        elif ctx.continue_stm():
            return self.visit(ctx.continue_stm())
        elif ctx.return_stm():
            return self.visit(ctx.return_stm())
        elif ctx.func_call_stm():
            return self.visit(ctx.func_call_stm())
        return self.visit(ctx.block())

    # Visit a parse tree produced by ZCodeParser#assignment.
    def visitAssignment(self, ctx:ZCodeParser.AssignmentContext):
        return Assign(self.visit(ctx.lhs()),self.visit(ctx.expr()))
    
    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        if ctx.arrayindex():
            return self.visit(ctx.arrayindex())
        return Id(ctx.IDENTIFIER().getText())
        
    # Visit a parse tree produced by ZCodeParser#arrayindex.
    def visitArrayindex(self, ctx:ZCodeParser.ArrayindexContext):
        return ArrayCell(self.visit(ctx.arr_expr()), self.visit(ctx.cell()))
    
    # Visit a parse tree produced by ZCodeParser#arr_expr.
    def visitArr_expr(self, ctx:ZCodeParser.Arr_exprContext):
        if ctx.func_call_expr():
            return self.visit(ctx.func_call_expr())
        return Id(ctx.IDENTIFIER().getText())
    
    # Visit a parse tree produced by ZCodeParser#cell.
    def visitCell(self, ctx:ZCodeParser.CellContext):
        return [self.visit(ctx.expr())] + self.visit(ctx.exprtail())
    
    # Visit a parse tree produced by ZCodeParser#cell.
    def visitExprtail(self, ctx:ZCodeParser.ExprtailContext):
        if ctx.expr():
            return [self.visit(ctx.expr())] + self.visit(ctx.exprtail())
        return []

    # Visit a parse tree produced by ZCodeParser#ifstm.
    def visitIfstm(self, ctx:ZCodeParser.IfstmContext):
        return If(self.visit(ctx.expr()),self.visit(ctx.statement()),self.visit(ctx.elif_here()),self.visit(ctx.else_here()))
    
    def visitElif_here(self, ctx:ZCodeParser.Elif_hereContext):
        if ctx.elifbranch():
            return self.visit(ctx.elifbranch())
        return []
    
    def visitElse_here(self, ctx:ZCodeParser.Else_hereContext):
        if ctx.elsebranch():
            return self.visit(ctx.elsebranch())
        return None

    # Visit a parse tree produced by ZCodeParser#elifbranch.
    def visitElifbranch(self, ctx:ZCodeParser.ElifbranchContext):
        return [(self.visit(ctx.expr()),self.visit(ctx.statement()))] + self.visit(ctx.eliftail())

    # Visit a parse tree produced by ZCodeParser#eliftail.
    def visitEliftail(self, ctx:ZCodeParser.EliftailContext):
        if ctx.elifbranch():
            return self.visit(ctx.elifbranch())
        return []

    #  Visit a parse tree produced by ZCodeParser#elsebranch.
    def visitElsebranch(self, ctx:ZCodeParser.ElsebranchContext):
        return self.visit(ctx.statement())

    # Visit a parse tree produced by ZCodeParser#forstm.
    def visitForstm(self, ctx:ZCodeParser.ForstmContext):
        return For(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.cond_expr()),self.visit(ctx.update_expr()),self.visit(ctx.statement()))

    # Visit a parse tree produced by ZCodeParser#cond_expr.
    def visitCond_expr(self, ctx:ZCodeParser.Cond_exprContext):
        return self.visit(ctx.expr())
    
    # Visit a parse tree produced by ZCodeParser#update_expr.
    def visitUpdate_expr(self, ctx:ZCodeParser.Update_exprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by ZCodeParser#break_stm.
    def visitBreak_stm(self, ctx:ZCodeParser.Break_stmContext):
        return Break()

    # Visit a parse tree produced by ZCodeParser#continue_stm.
    def visitContinue_stm(self, ctx:ZCodeParser.Continue_stmContext):
        return Continue()

    # Visit a parse tree produced by ZCodeParser#return_stm.
    def visitReturn_stm(self, ctx:ZCodeParser.Return_stmContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return()
    
    def visitFunc_call_stm(self, ctx:ZCodeParser.Func_call_stmContext):
        return CallStmt(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.argumentlist()))

    # Visit a parse tree produced by ZCodeParser#argumentlist.
    def visitArgumentlist(self, ctx:ZCodeParser.ArgumentlistContext):
        if ctx.arguments():
            return self.visit(ctx.arguments())
        return []

    # Visit a parse tree produced by ZCodeParser#arguments.
    def visitArguments(self, ctx:ZCodeParser.ArgumentsContext):
        return [self.visit(ctx.expr())] + self.visit(ctx.argtail())

    # Visit a parse tree produced by ZCodeParser#argtail.
    def visitArgtail(self, ctx:ZCodeParser.ArgtailContext):
        if ctx.CM():
            return [self.visit(ctx.expr())] + self.visit(ctx.argtail())
        return []
    
    # Visit a parse tree produced by ZCodeParser#block.
    def visitBlock(self, ctx:ZCodeParser.BlockContext):
        return Block([self.visit(x) for x in ctx.statement()])

    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        if ctx.CONCAT():
            return BinaryOp(ctx.CONCAT().getText(),self.visit(ctx.expr()),self.visit(ctx.expr1()))
        return self.visit(ctx.expr1())

    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if ctx.ANDOR():
            return BinaryOp(ctx.ANDOR().getText(),self.visit(ctx.expr1()),self.visit(ctx.expr2()))
        return self.visit(ctx.expr2())

    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if ctx.RELATION():
            return BinaryOp(ctx.RELATION().getText(),self.visit(ctx.expr2()),self.visit(ctx.expr3()))
        return self.visit(ctx.expr3())

    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if ctx.ADDOP():
            return BinaryOp(ctx.ADDOP().getText(),self.visit(ctx.expr3()),self.visit(ctx.expr4()))
        elif ctx.SUBTR():
            return BinaryOp(ctx.SUBTR().getText(),self.visit(ctx.expr3()),self.visit(ctx.expr4()))
        return self.visit(ctx.expr4())


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.MULOP():
            return BinaryOp(ctx.MULOP().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        elif ctx.DIVOP():
            return BinaryOp(ctx.DIVOP().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        elif ctx.MODOP():
            return BinaryOp(ctx.MODOP().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        return self.visit(ctx.expr5())


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if ctx.NOTOP():
            return UnaryOp(ctx.NOTOP().getText(),self.visit(ctx.expr6()))
        return self.visit(ctx.expr6())


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.SUBTR():
            return UnaryOp(ctx.SUBTR().getText(),self.visit(ctx.expr7()))
        return self.visit(ctx.expr7())

    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        if ctx.func_call_expr():
            return self.visit(ctx.func_call_expr())
        if ctx.arrayindex():
            return self.visit(ctx.arrayindex())
        return self.visit(ctx.operand())
    
    def visitFunc_call_expr(self, ctx:ZCodeParser.Func_call_exprContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.argumentlist()))

    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        if ctx.literals():
            return self.visit(ctx.literals())
        return self.visit(ctx.expr())
