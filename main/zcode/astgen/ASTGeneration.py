from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.declaration()))

    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        return self.visit(ctx.declare()) + self.visit(ctx.declaretail())


    # Visit a parse tree produced by ZCodeParser#declaretail.
    def visitDeclaretail(self, ctx:ZCodeParser.DeclaretailContext):
        if ctx.declare():
            return self.visit(ctx.declare()) + self.visit(ctx.declaretail())
        return []


    # Visit a parse tree produced by ZCodeParser#declare.
    def visitDeclare(self, ctx:ZCodeParser.DeclareContext):
        if ctx.var_declare():
            return [self.visit(ctx.var_declare())]
        return [self.visit(ctx.func_declare())]


    # Visit a parse tree produced by ZCodeParser#var_declare.
    def visitVar_declare(self, ctx:ZCodeParser.Var_declareContext):
        if ctx.normaldeclare():
            return self.visit(ctx.normaldeclare())
        if ctx.arraydeclare():
            return self.visit(ctx.arraydeclare())
        if ctx.vartypedeclare():
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
        if ctx.assignmentexpr():
            return self.visit(ctx.assignmentexpr())
        return None


    # Visit a parse tree produced by ZCodeParser#assignmentexpr.
    def visitAssignmentexpr(self, ctx:ZCodeParser.AssignmentexprContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by ZCodeParser#arraydeclare.
    def visitArraydeclare(self, ctx:ZCodeParser.ArraydeclareContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()),ArrayType(self.visit(ctx.array()),self.visit(ctx.var_type())),None,self.visit(ctx.initialarray()))


    # Visit a parse tree produced by ZCodeParser#array.
    def visitArray(self, ctx:ZCodeParser.ArrayContext):
        return self.visit(ctx.dimension())


    # Visit a parse tree produced by ZCodeParser#dimension.
    def visitDimension(self, ctx:ZCodeParser.DimensionContext):
        return [ctx.NUMLIT().getText()] + self.visit(ctx.dimtail())


    # Visit a parse tree produced by ZCodeParser#dimtail.
    def visitDimtail(self, ctx:ZCodeParser.DimtailContext):
        if ctx.NUMLIT():
            return [ctx.NUMLIT().getText()] + self.visit(ctx.dimtail())
        return []


    # Visit a parse tree produced by ZCodeParser#initialarray.
    def visitInitialarray(self, ctx:ZCodeParser.InitialarrayContext):
        if ctx.ASSIGN():
            return self.visit(ctx.expr())
        return None


    # Visit a parse tree produced by ZCodeParser#vartypedeclare.
    def visitVartypedeclare(self, ctx:ZCodeParser.VartypedeclareContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()),None,ctx.VARTYPE().getText(),self.visit(ctx.assignmentexpr()))


    # Visit a parse tree produced by ZCodeParser#func_declare.
    def visitFunc_declare(self, ctx:ZCodeParser.Func_declareContext):
        if ctx.body():
            return FuncDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.parameters()),self.visit(ctx.body()))
        return FuncDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.parameters()),None)

    # Visit a parse tree produced by ZCodeParser#parameters.
    def visitParameters(self, ctx:ZCodeParser.ParametersContext):
        return self.visit(ctx.param_here())


    # Visit a parse tree produced by ZCodeParser#param_here.
    def visitParam_here(self, ctx:ZCodeParser.Param_hereContext):
        if ctx.param_list():
            return self.visit(ctx.param_list())
        return []


    # Visit a parse tree produced by ZCodeParser#param_list.
    def visitParam_list(self, ctx:ZCodeParser.Param_listContext):
        return self.visit(ctx.para()) + self.visit(ctx.paratail())


    # Visit a parse tree produced by ZCodeParser#paratail.
    def visitParatail(self, ctx:ZCodeParser.ParatailContext):
        if ctx.para():
            return self.visit(ctx.para()) + self.visit(ctx.paratail())
        return []


    # Visit a parse tree produced by ZCodeParser#para.
    def visitPara(self, ctx:ZCodeParser.ParaContext):
        if self.visit(ctx.isarrayindex())==None:
            return [VarDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.var_type()),None,None)]
        return [VarDecl(Id(ctx.IDENTIFIER().getText()),ArrayType(self.visit(ctx.isarrayindex()),self.visit(ctx.var_type())),None,None)]
        
        


    # Visit a parse tree produced by ZCodeParser#isarrayindex.
    def visitIsarrayindex(self, ctx:ZCodeParser.IsarrayindexContext):
        if ctx.arrayindex():
            return self.visit(ctx.arrayindex())
        return None


    # Visit a parse tree produced by ZCodeParser#arrayindex.
    def visitArrayindex(self, ctx:ZCodeParser.ArrayindexContext):
        if ctx.expr():
            return [self.visit(ctx.expr())]
        return []


    # Visit a parse tree produced by ZCodeParser#body.
    def visitBody(self, ctx:ZCodeParser.BodyContext):
        if ctx.return_stm():
            return self.visit(ctx.return_stm())
        if ctx.block():
            return self.visit(ctx.block())
        return None


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        if ctx.var_declare():
            return self.visit(ctx.var_declare())
        if ctx.assignment():
            return self.visit(ctx.assignment())
        if ctx.ifstm():
            return self.visit(ctx.ifstm())
        if ctx.forstm():
            return self.visit(ctx.forstm())
        if ctx.break_stm():
            return self.visit(ctx.break_stm())
        if ctx.continue_stm():
            return self.visit(ctx.continue_stm())
        if ctx.return_stm():
            return self.visit(ctx.return_stm())
        if ctx.func_call_stm():
            return self.visit(ctx.func_call_stm())
        if ctx.block():
            return self.visit(ctx.block()) 

    # Visit a parse tree produced by ZCodeParser#assignment.
    def visitAssignment(self, ctx:ZCodeParser.AssignmentContext):
        return Assign(self.visit(ctx.lhs()),self.visit(ctx.expr()))


    # Visit a parse tree produced by ZCodeParser#ifstm.
    def visitIfstm(self, ctx:ZCodeParser.IfstmContext):
        if ctx.ifstm():
            return If(self.visit(ctx.expr()),self.visit(ctx.ifstm()),[],None)
        if ctx.elifbranch():
            if ctx.elsebranch():
                return If(self.visit(ctx.expr()),self.visit(ctx.statement()),[self.visit(x) for x in ctx.elifbranch()],self.visit(ctx.elsebranch()))
            return If(self.visit(ctx.expr()),self.visit(ctx.statement()),[self.visit(x) for x in ctx.elifbranch()],None)
        if ctx.elsebranch():
            return If(self.visit(ctx.expr()),self.visit(ctx.statement()),[],self.visit(ctx.elsebranch()))
        return If(self.visit(ctx.expr()),self.visit(ctx.statement()),[],None)
    
    # Visit a parse tree produced by ZCodeParser#elifbranch.
    def visitElifbranch(self, ctx:ZCodeParser.ElifbranchContext):
        if ctx.ifstm():
            return (self.visit(ctx.expr()),self.visit(ctx.ifstm()))
        return (self.visit(ctx.expr()),self.visit(ctx.statement()))
    
    # Visit a parse tree produced by ZCodeParser#elsebranch.
    def visitElsebranch(self, ctx:ZCodeParser.ElsebranchContext):
        return self.visit(ctx.statement())


    # Visit a parse tree produced by ZCodeParser#forstm.
    def visitForstm(self, ctx:ZCodeParser.ForstmContext):
        return For(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.expr()),self.visit(ctx.update()),self.visit(ctx.statement()))


    # Visit a parse tree produced by ZCodeParser#update.
    def visitUpdate(self, ctx:ZCodeParser.UpdateContext):
        if ctx.SUBTR():
            return UnaryOp(ctx.SUBTR().getText(),self.visit(ctx.literals()))
        return self.visit(ctx.literals())


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

    # Visit a parse tree produced by ZCodeParser#block.
    def visitBlock(self, ctx:ZCodeParser.BlockContext):
        return Block([self.visit(x) for x in ctx.statement()])

    def visitFunc_call_stm(self, ctx:ZCodeParser.Func_call_stmContext):
        return CallStmt(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.arguments()))

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
        if ctx.SUBTR():
            return BinaryOp(ctx.SUBTR().getText(),self.visit(ctx.expr3()),self.visit(ctx.expr4()))
        return self.visit(ctx.expr4())
        

    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.MULOP():
            return BinaryOp(ctx.MULOP().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        if ctx.DIVOP():
            return BinaryOp(ctx.DIVOP().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        if ctx.MODOP():
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
        if ctx.LB() and ctx.RB():
            return CallExpr(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.arguments()))
        if ctx.LP():
            return ArrayCell(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.expr8()))
        return self.visit(ctx.expr9())

    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr8(self, ctx:ZCodeParser.Expr5Context):
        if ctx.CM():
            return [self.visit(ctx.expr())] + self.visit(ctx.expr8())
        return [self.visit(ctx.expr())]



    # Visit a parse tree produced by ZCodeParser#expr9.
    def visitExpr9(self, ctx:ZCodeParser.Expr9Context):
        return self.visit(ctx.operand())


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        if ctx.literals():
            return self.visit(ctx.literals())
        return self.visit(ctx.expr())
        
        


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        if ctx.expr7():
            return self.visit(ctx.expr7())
        return Id(ctx.IDENTIFIER().getText())


    # Visit a parse tree produced by ZCodeParser#literals.
    def visitLiterals(self, ctx:ZCodeParser.LiteralsContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        if ctx.NUMLIT():
            if ctx.SUBTR():
                return UnaryOp(ctx.SUBTR().getText(),NumberLiteral(float(ctx.NUMLIT().getText())))
            return NumberLiteral(float(ctx.NUMLIT().getText()))
        if ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        if ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())
        return self.visit(ctx.arraylit())


    # Visit a parse tree produced by ZCodeParser#arraylit.
    def visitArraylit(self, ctx:ZCodeParser.ArraylitContext):
        if ctx.arraylit():
            return ArrayLiteral([self.visit(ctx.arraylit())] +self.visit(ctx.arraylittail()))
        if ctx.NUMLIT():
            if ctx.SUBTR():
                return ArrayLiteral([UnaryOp(ctx.SUBTR().getText(),NumberLiteral(float(ctx.NUMLIT().getText())))]+self.visit(ctx.numlittail()))
            return ArrayLiteral([NumberLiteral(float(ctx.NUMLIT().getText()))]+self.visit(ctx.numlittail()))
        if ctx.STRINGLIT():
            return ArrayLiteral([StringLiteral(ctx.STRINGLIT().getText())]+self.visit(ctx.stringlittail()))
        if ctx.BOOLIT():
            return ArrayLiteral([BooleanLiteral(ctx.BOOLIT().getText())]+self.visit(ctx.boolittail()))

    # Visit a parse tree produced by ZCodeParser#numlittail.
    def visitNumlittail(self, ctx:ZCodeParser.NumlittailContext):
        if ctx.NUMLIT():
            if ctx.SUBTR():
                return [UnaryOp(ctx.SUBTR().getText(),NumberLiteral(float(ctx.NUMLIT().getText())))] + self.visit(ctx.numlittail())
            return [NumberLiteral(float(ctx.NUMLIT().getText()))] + self.visit(ctx.numlittail())
        return []


    # Visit a parse tree produced by ZCodeParser#stringlittail.
    def visitStringlittail(self, ctx:ZCodeParser.StringlittailContext):
        if ctx.STRINGLIT():
            return [StringLiteral(ctx.STRINGLIT().getText())] + self.visit(ctx.stringlittail())
        return []


    # Visit a parse tree produced by ZCodeParser#boolittail.
    def visitBoolittail(self, ctx:ZCodeParser.BoolittailContext):
        if ctx.BOOLIT():
            return [BooleanLiteral(ctx.BOOLIT().getText())] + self.visit(ctx.boolittail())
        return []


    # Visit a parse tree produced by ZCodeParser#arraylittail.
    def visitArraylittail(self, ctx:ZCodeParser.ArraylittailContext):
        if ctx.arraylit():
            return [self.visit(ctx.arraylit())]+self.visit(ctx.arraylittail())
        return []


    # Visit a parse tree produced by ZCodeParser#func_call.
    #def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
    #    return CallExpr(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.arguments()))


    # Visit a parse tree produced by ZCodeParser#arguments.
    def visitArguments(self, ctx:ZCodeParser.ArgumentsContext):
        return self.visit(ctx.arg()) + self.visit(ctx.argtail())


    # Visit a parse tree produced by ZCodeParser#arg.
    def visitArg(self, ctx:ZCodeParser.ArgContext):
        if ctx.expr():
            return [self.visit(ctx.expr())]
        return []


    # Visit a parse tree produced by ZCodeParser#argtail.
    def visitArgtail(self, ctx:ZCodeParser.ArgtailContext):
        if ctx.CM():
            return self.visit(ctx.arg()) + self.visit(ctx.argtail())
        return []
