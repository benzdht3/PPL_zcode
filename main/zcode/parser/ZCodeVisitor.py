# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration.
    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_declare.
    def visitVar_declare(self, ctx:ZCodeParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#normaldeclare.
    def visitNormaldeclare(self, ctx:ZCodeParser.NormaldeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_type.
    def visitVar_type(self, ctx:ZCodeParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#initialnormal.
    def visitInitialnormal(self, ctx:ZCodeParser.InitialnormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraydeclare.
    def visitArraydeclare(self, ctx:ZCodeParser.ArraydeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array.
    def visitArray(self, ctx:ZCodeParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dimension.
    def visitDimension(self, ctx:ZCodeParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dimtail.
    def visitDimtail(self, ctx:ZCodeParser.DimtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#initialarray.
    def visitInitialarray(self, ctx:ZCodeParser.InitialarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraylit.
    def visitArraylit(self, ctx:ZCodeParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraylittail.
    def visitArraylittail(self, ctx:ZCodeParser.ArraylittailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literals.
    def visitLiterals(self, ctx:ZCodeParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vartypedeclare.
    def visitVartypedeclare(self, ctx:ZCodeParser.VartypedeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_declare.
    def visitFunc_declare(self, ctx:ZCodeParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_here.
    def visitParam_here(self, ctx:ZCodeParser.Param_hereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_list.
    def visitParam_list(self, ctx:ZCodeParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paratail.
    def visitParatail(self, ctx:ZCodeParser.ParatailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#para.
    def visitPara(self, ctx:ZCodeParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#bodyhere.
    def visitBodyhere(self, ctx:ZCodeParser.BodyhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#body.
    def visitBody(self, ctx:ZCodeParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment.
    def visitAssignment(self, ctx:ZCodeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayindex.
    def visitArrayindex(self, ctx:ZCodeParser.ArrayindexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_expr.
    def visitArr_expr(self, ctx:ZCodeParser.Arr_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#cell.
    def visitCell(self, ctx:ZCodeParser.CellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprtail.
    def visitExprtail(self, ctx:ZCodeParser.ExprtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifstm.
    def visitIfstm(self, ctx:ZCodeParser.IfstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_here.
    def visitElif_here(self, ctx:ZCodeParser.Elif_hereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_here.
    def visitElse_here(self, ctx:ZCodeParser.Else_hereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifbranch.
    def visitElifbranch(self, ctx:ZCodeParser.ElifbranchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#eliftail.
    def visitEliftail(self, ctx:ZCodeParser.EliftailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elsebranch.
    def visitElsebranch(self, ctx:ZCodeParser.ElsebranchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forstm.
    def visitForstm(self, ctx:ZCodeParser.ForstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#cond_expr.
    def visitCond_expr(self, ctx:ZCodeParser.Cond_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#update_expr.
    def visitUpdate_expr(self, ctx:ZCodeParser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stm.
    def visitBreak_stm(self, ctx:ZCodeParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stm.
    def visitContinue_stm(self, ctx:ZCodeParser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stm.
    def visitReturn_stm(self, ctx:ZCodeParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call_stm.
    def visitFunc_call_stm(self, ctx:ZCodeParser.Func_call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argumentlist.
    def visitArgumentlist(self, ctx:ZCodeParser.ArgumentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arguments.
    def visitArguments(self, ctx:ZCodeParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argtail.
    def visitArgtail(self, ctx:ZCodeParser.ArgtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block.
    def visitBlock(self, ctx:ZCodeParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call_expr.
    def visitFunc_call_expr(self, ctx:ZCodeParser.Func_call_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        return self.visitChildren(ctx)



del ZCodeParser