from array import ArrayType
from tokenize import Number
from unicodedata import name
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.ast = ast
        self.param = dict()
        self.scope = 0

    def check(self):
        self.visitProgram(self.ast,self.param)

    def visitProgram(self, ast, param):
        for x in ast.decl:
            self.visit(x,param)
        if 'main' in param:
            if param['main'][0][0] == 'func':
                if param['main'][0][1] == []:
                    if param['main'][0][2] != 'none' and param['main'][0][2] != 'void' and param['main'][0][2] != 'v':
                        raise NoEntryPoint()
                else:
                    raise NoEntryPoint()
            else:
                raise NoEntryPoint()
        else:
            raise NoEntryPoint()
        for x in param:
            if param[x][0][0] == 'func':
                if param[x][0][2]== 'none':
                    if x != 'main':
                        raise NoDefinition(x)

    def visitVarDecl(self, ast, param):
        id, scope, name =self.visit(ast.name,param)
        if id[0] != 'undecl':
            if self.scope <= scope:
                if type(self.scope) is not int and self.scope!=0:
                    raise Redeclared(Parameter(),name)
                raise Redeclared(Variable(),name)
        if ast.varType is None:
            if ast.modifier == 'dynamic':
                param[name]= (['none'],self.scope)
            elif ast.modifier == 'var':
                if ast.varInit is None:
                    raise TypeMismatchInStatement(ast)
                ityp,scope,iname=self.visit(ast.varInit,param)
                if ityp[0] == 'none':
                    raise TypeCannotBeInferred(ast)
                if ityp[0] == 'undecl':
                    raise Undeclared(Identifier(),iname)
                if ityp[0] == 'array':
                    raise TypeMismatchInStatement(ast)
                param[name] = (ityp,self.scope)
            else:
                raise TypeMismatchInStatement(ast)
        else:
            param[name] = (self.visit(ast.varType,param),self.scope)
        if ast.varInit is not None:
            ityp, scope, iname = self.visit(ast.varInit,param)
            if ityp[0] == 'undecl':
                raise Undeclared(Identifier(),iname)
            if ityp[0] == 'func':
                if len(ityp[2])==3:
                    ityp[0]=ityp[2][0]
                    ityp=ityp[2]
                else:
                    ityp[0]=ityp[2]
            if ityp[0] == 'none':
                if param[name][0][0] == 'none':
                    raise TypeCannotBeInferred(ast)
                if iname != '':
                    if param[iname][0][0] == 'func':
                        param[iname][0][2]=param[name][0][0]
                    else:
                        param[iname][0][0]=param[name][0][0]
            elif param[name][0][0] == 'none':
                param[name][0][0] = ityp[0]
            elif ityp[0] == 'array' and ityp[0]==param[name][0][0]:
                li=ityp[1]
                lp=param[name][0][1]
                if li[0][1]!=lp[0][1]:
                    raise TypeMismatchInStatement(ast)
                if ityp[2]!=param[name][0][2]:
                    raise TypeMismatchInStatement(ast)
            elif ityp[0] != param[name][0][0]:
                raise TypeMismatchInStatement(ast)


    def visitFuncDecl(self, ast, param):
        id, scope, name=self.visit(ast.name,param)
        if id[0] != 'undecl':
            if name == 'main':
                raise Redeclared(Function(),name)
            if self.scope == scope: 
                if param[name][0][2] != 'none' and name != 'main':
                    raise Redeclared(Function(),name)
        self.scope = 1.5
        paramfunc = dict()
        paramlist =[]
        for x in ast.param:
            self.visit(x,paramfunc)
        for x in paramfunc:
            paramlist.append(paramfunc[x][0][0])
        self.scope=0
        if ast.body is None:
            param[name] = (['func',paramlist,'none'],self.scope)
        else:
            for x in param:
                if x not in paramfunc:
                    paramfunc[x]=param[x]
            bodytyp = self.visit(ast.body,paramfunc)
            rmkey=[]
            self.scope=0
            for x in param:
                if param[x][1] > self.scope:
                    rmkey.append(x)
            for x in rmkey:
                param.pop(x,None)
            if bodytyp is not None:
                param[name] = (['func',paramlist,bodytyp[0][0]],self.scope)
            else:
                param[name] = (['func',paramlist,'void'],self.scope)
        
        
    def visitNumberType(self, ast, param):
        return ['number']

    def visitBoolType(self, ast, param):
        return ['bool']

    def visitStringType(self, ast, param):
        return ['string']

    def visitArrayType(self, ast, param):
        return ['array',[self.visit(x,param) for x in ast.size],self.visit(ast.eleType,param)]

    def visitBinaryOp(self, ast, param):
        ltyp,lscope,lname = self.visit(ast.left,param)
        rtyp,rscope,rname = self.visit(ast.right,param)
        
        if ltyp[0] == 'undecl':
            raise Undeclared(Identifier(),lname)
        if rtyp[0] == 'undecl':
            raise Undeclared(Identifier(),rname)
        if ltyp[0] == 'func':
            ltyp[0] = ltyp[2]
        if rtyp[0] == 'func':
            rtyp[0] = rtyp[2]
        if ast.op in ['+','-','*','/','%','=','!=','<','>','<=','>=']:
            if ltyp[0] == 'none':
                if rtyp[0] == 'none':
                    if param[rname][0][0] == 'func':
                        param[rname][0][2] = 'number'
                    else:
                        param[rname][0][0]= 'number'
                    rtyp[0]= 'number'
                if rtyp[0] != 'number':
                    raise TypeMismatchInExpression(ast)
                if param[lname][0][0] == 'func':
                    param[lname][0][2] = 'number'
                else:
                    param[lname][0][0]= 'number'
                return ['number'],self.scope,''
            elif rtyp[0] == 'none':
                if ltyp[0] != 'number':
                    raise TypeMismatchInExpression(ast)
                if param[rname][0][0] == 'func':
                    param[rname][0][2] = 'number'
                else:
                    param[rname][0][0]= 'number'
                
                return ['number'],self.scope,''
            elif ltyp[0] != 'number' or rtyp[0] != 'number':
                raise TypeMismatchInExpression(ast)
            if ast.op in ['+','-','*','/','%']:
                return ['number'],self.scope,''
            return ['bool'],self.scope,''
        if ast.op in ['and','or']:
            if ltyp[0] == 'none':
                if rtyp[0] == 'none':
                    if param[rname][0][0] == 'func':
                        param[rname][0][2] = 'bool'
                    else:
                        param[rname][0][0]= 'bool'
                    rtyp[0] = 'bool'
                if rtyp[0] != 'bool':
                    raise TypeMismatchInExpression(ast)
                if param[lname][0][0] == 'func':
                    param[lname][0][2] = 'bool'
                else:
                    param[lname][0][0]= 'bool'
                return ['bool'],self.scope,''
            elif rtyp[0] == 'none':
                if ltyp[0] != 'bool':
                    raise TypeMismatchInExpression(ast)
                if param[rname][0][0] == 'func':
                    param[rname][0][2] = 'bool'
                else:
                    param[rname][0][0]= 'bool'
                return ['bool'],self.scope,''
            if ltyp[0] != 'bool' or rtyp[0] != 'bool':
                raise TypeMismatchInExpression(ast)
            return ['bool'],self.scope,''
        if ast.op in ['...','==']:
            if ltyp[0] == 'none':
                if rtyp[0] == 'none':
                    if param[rname][0][0] == 'func':
                        param[rname][0][2] = 'string'
                    else:
                        param[rname][0][0]= 'string'
                    rtyp[0] = 'string'
                if rtyp[0] != 'string':
                    raise TypeMismatchInExpression(ast)
                if param[lname][0][0] == 'func':
                    param[lname][0][2] = 'string'
                else:
                    param[lname][0][0]= 'string'
                return ['string'],self.scope,''
            elif rtyp[0] == 'none':
                if ltyp[0] != 'string':
                    raise TypeMismatchInExpression(ast)
                if param[rname][0][0] == 'func':
                    param[rname][0][2] = 'string'
                else:
                    param[rname][0][0]= 'string'
                return ['string'],self.scope,''
            if ltyp[0] != 'string' or rtyp[0] != 'string':
                raise TypeMismatchInExpression(ast)
            if ast.op == '...':
                return ['string'],self.scope,''
            return ['bool'],self.scope,''

    def visitUnaryOp(self, ast, param):
        typ,scope,name = self.visit(ast.operand,param)
        if typ[0] == 'undecl':
            raise Undeclared(Identifier(),name)
        if typ[0] == 'func':
            typ[0]=typ[2]
        if ast.op == '-':
            if typ[0] == 'none':
                if param[name][0][0] == 'func':
                    param[name][0][2] = 'number'
                else:
                    param[name][0][0]= 'number'
                typ[0] = 'number'
            if typ[0] != 'number':
                raise TypeMismatchInExpression(ast)
            return ['number'],self.scope,''
        if ast.op == 'not':
            if typ[0] == 'none':
                if param[name][0][0] == 'func':
                    param[name][0][2] = 'bool'
                else:
                    param[name][0][0]= 'bool'
                typ[0] = 'bool'
            if typ[0] != 'bool':
                raise TypeMismatchInExpression(ast)
            return ['bool'],self.scope,''
        if ast.op == '[,]':
            if typ[0] == 'none':
                if param[name][0][0] == 'func':
                    param[name][0][2] = 'array'
                else:
                    param[name][0][0]= 'array'
                typ[0] = 'bool'
            if typ[0] != 'array':
                raise TypeMismatchInExpression(ast)
            return [typ[2]],self.scope,''

    def visitCallExpr(self, ast, param):
        func,scope,name = self.visit(ast.name,param)
        if func[0] == 'undecl' or func[0] != 'func':
            raise Undeclared(Function(),name)
        arglist = func[1]
        typ=func[2]
        argcall = ast.args
        if len(ast.args) != len(arglist):
            raise TypeMismatchInStatement(ast)
        if typ == 'void' or typ == 'v':
            raise TypeMismatchInExpression(ast)
        for i in range(len(argcall)):
            argtyp,scope,argname = self.visit(argcall[i],param)
            if argtyp[0] == 'undecl':
                raise Undeclared(Identifier(),argname)
            if argtyp[0] == 'none':
                raise TypeCannotBeInferred(ast)
            if argtyp[0] != arglist[i]:
                raise TypeMismatchInExpression(ast)
        return func,scope,name
        

    def visitId(self, ast, param):
        if ast.name not in param:
            return (['undecl'],self.scope,ast.name)
        a=param[ast.name][0].copy()
        b=param[ast.name][1]
        return (a,b,ast.name)

    def visitArrayCell(self, ast, param):
        ar, scope, name=self.visit(ast.arr,param)
        if ar[0] == 'undecl':
            raise Undeclared(Identifier(),name)
        if ar[0] == 'func':
            if len(ar[2])==3:
                ar[0]==ar[2][0]
                ar=ar[2]
            else:
                ar[0] = ar[2]
        if ar[0] != 'array':
            raise TypeMismatchInExpression(ast)
        for x in ast.idx:
            typ,idxscope,idxname=self.visit(x,param)
            if typ[0] == 'none':
                param[idxname][0][0] = 'number'
            elif typ[0] != 'number':
                raise TypeMismatchInExpression(ast)
        return ar[2],self.scope,name
        

    def visitBlock(self, ast, param):
        paramblock = param
        self.scope+=1
        for x in ast.stmt:
            self.visit(x,paramblock)
        self.scope-=1
        rmkey=[]
        for x in param:
            if param[x][1] > self.scope:
                rmkey.append(x)
        for x in rmkey:
            param.pop(x,None)


    def visitIf(self, ast, param):
        cond, cscope, cname = self.visit(ast.expr,param)
        if cond[0] == 'func':
            cond[0]=cond[2]
        if cond[0] == 'none':
            raise TypeCannotBeInferred(ast)
        if cond[0] == 'undecl':
            raise Undeclared(Identifier(),cname)
        if cond[0] != 'bool':
            raise TypeMismatchInStatement(ast)
        ifparam = param
        self.visit(ast.thenStmt,ifparam)
        if ast.elifStmt != []:
            for x in ast.elifStmt:
                cond, cscope, cname = self.visit(x[0],param)
                if cond[0] == 'func':
                    cond[0]=cond[2]
                if cond[0] == 'none':
                    raise TypeCannotBeInferred(ast)
                if cond[0] != 'bool':
                    raise TypeMismatchInStatement(ast)
                ifparam = param
                self.visit(x[1],ifparam)
        if ast.elseStmt is not None:
            ifparam = param
            self.visit(ast.elseStmt,ifparam)


    def visitFor(self, ast, param):
        expr,scope,name = self.visit(ast.name,param)
        if expr[0] == 'func':
            expr[0]=expr[2]
        if expr[0] == 'undecl':
            raise Undeclared(Identifier(),name)
        if expr[0] == 'none':
            raise TypeCannotBeInferred(ast)
        if expr[0] != 'number':
            raise TypeMismatchInStatement(ast)
        expr,scope,name = self.visit(ast.condExpr,param)
        if expr[0] == 'func':
            expr[0]=expr[2]
        if expr[0] == 'undecl':
            raise Undeclared(Identifier(),name)
        if expr[0] == 'none':
            raise TypeCannotBeInferred(ast)
        if expr[0] != 'bool':
            raise TypeMismatchInStatement(ast)
        expr,scope,name = self.visit(ast.updExpr,param)
        if expr[0] == 'func':
            expr[0]=expr[2]
        if expr[0] == 'undecl':
            raise Undeclared(Identifier(),name)
        if expr[0] == 'none':
            raise TypeCannotBeInferred(ast)
        if expr[0] != 'number':
            raise TypeMismatchInStatement(ast)
        forparam = param
        forparam['0']='inloop'
        self.visit(ast.body,forparam)
        param.pop('0',None)


    def visitContinue(self, ast, param):
        if '0' in param:
            if param['0'] != 'inloop':
                raise MustInLoop(ast)
        else:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if '0' in param:
            if param['0'] != 'inloop':
                raise MustInLoop(ast)
        else:
            raise MustInLoop(ast)

    def visitReturn(self, ast, param):
        if ast.expr is not None:
            id,scope,name = self.visit(ast.expr,param)
            if id[0] == 'undecl':
                raise Undeclared(Identifier(),name)
            if id[0] == 'func':
                id[0]=id[2]
            if id[0] == 'none':
                raise TypeCannotBeInferred(ast)
            return id,scope,name
        return 'void'

    def visitAssign(self, ast, param):
        lhs,lscope,lname=self.visit(ast.lhs,param)
        rhs,rscope,rname=self.visit(ast.rhs,param)
        if lhs[0] == 'func':
            if len(lhs[2])==3:
                lhs[0]=lhs[2][0]
                lhs=lhs[2]
            else:
                lhs[0]=lhs[2]
        if rhs[0] == 'func':
            if len(rhs[2])==3:
                rhs[0]=rhs[2][0]
                rhs=rhs[2]
            else:
                rhs[0]=rhs[2]
        if lhs[0] == 'undecl':
            raise Undeclared(Identifier(),lname)
        if rhs[0] == 'undecl':
            raise Undeclared(Identifier(),rname)
        if lhs[0] == 'void' or lhs[0] == 'v':
            raise TypeMismatchInStatement(ast)
        if lhs[0] == 'none':
            if rhs[0] =='none':
                raise TypeCannotBeInferred(ast)
            if param[lname][0][0] == 'func':
                if rhs[0]=='array':
                    param[lname][0][2]=rhs
                else:
                    param[lname][0][2]=rhs[0]
            else:
                if rhs[0]=='array':
                    param[lname]=(rhs,lscope)
                else:
                    param[lname][0][0]=rhs[0]
        elif rhs[0] == 'none':
            if param[rname][0][0] == 'func':
                if lhs[0] == 'array':
                    param[rname][0][2]=lhs
                else:
                    param[rname][0][2]=lhs[0]
            else:
                if lhs[0] == 'array':
                    param[rname]=(lhs,rscope)
                else:
                    param[rname][0][0]=lhs[0]
        else:
            if lhs[0] != rhs[0]:
                raise TypeMismatchInStatement(ast)
            if lhs[0]=='array':
                ll=len(lhs[1])
                lr=len(rhs[1])
                if ll != lr:
                    raise TypeMismatchInStatement(ast)
                for i in range(ll):
                    if lhs[1][i]!=rhs[1][i]:
                        raise TypeMismatchInStatement(ast)
                if lhs[2]!=rhs[2]:
                    raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast, param):
        id,scope,name=self.visit(ast.name,param)
        if id[0]=='undecl':
            raise Undeclared(Function(),name)
        if id[2]=='none':
            param[name][0][2] = 'void'
            id[2]='void'
        if id[0]!='func' or (id[2]!='void' and id[2]!='v'):
            raise TypeMismatchInStatement(ast)
        arglist = ast.args
        argfunc = id[1]
        if len(arglist) != len(argfunc):
            raise TypeMismatchInStatement(ast)
        for i in range(len(arglist)):
            typ,scope,argname = self.visit(arglist[i],param)
            if typ[0]=='func':
                if len(typ[2])==3:
                    typ[0]=typ[2][0]
                else:
                    typ[0]=typ[2]
            if typ[0]=='none':
                raise TypeCannotBeInferred(ast)
            elif typ[0]!=argfunc[i]:
                raise TypeMismatchInStatement(ast)
            

    def visitNumberLiteral(self, ast, param):
        return ['number'],ast.value,''

    def visitBooleanLiteral(self, ast, param):
        return ['bool'],ast.value,''

    def visitStringLiteral(self, ast, param):
        return ['string'],ast.value,''

    def visitArrayLiteral(self, ast, param):
        idx=[]
        for x in ast.value:
            typ,val,name=self.visit(x,param)
            if typ[0]=='undecl':
                raise Undeclared(Identifier(),name)
            if typ[0]=='func':
                if len(typ[2])==3:
                    typ[0]==typ[2][0]
                    typ=typ[2]
                else:
                    typ[0]=typ[2]
            idx.append(([typ[0]],val,name))
        returntyp=idx[0][0][0]
        for x in idx:
            if x[0][0]!=returntyp:
                raise TypeMismatchInExpression(ast)
        return ['array',[('',len(idx),'')],[returntyp]],0,''
