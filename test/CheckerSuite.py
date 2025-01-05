from ast import Call, IfExp
import unittest
from xmlrpc.client import Boolean
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_no_entry_point_400(self):
        input = Program([VarDecl(Id("b"), NumberType())])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))

    #Redeclared
    def test_case_401(self):
        input = Program([FuncDecl(Id("main"), [],None), VarDecl(Id("a"), NumberType()), VarDecl(Id("a"), StringType())])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_case_402(self):
        input = Program([FuncDecl(Id("main"), [],None), FuncDecl(Id("main"), [],[Return(Id("a"))])])
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_case_403(self):
        input = Program([FuncDecl(Id("main"), [],None), FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("a"), BoolType())],Return(Id("a")))])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_case_404(self):
        input = Program([FuncDecl(Id("main"), [],None), FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("a"), BoolType())],Return(Id("a")))])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_case_405(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())],Return(Id("a"))),
        FuncDecl(Id("foo"), [],[Return(Id("a"))])
        ])
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_case_406(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())],Return(Id("a"))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("a"), BoolType())],Return(Id("a")))
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_case_407(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("x"), NumberType()),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())],Block([
            VarDecl(Id("x"), NumberType()),
            VarDecl(Id("y"), NumberType()),
            VarDecl(Id("y"), NumberType())
            ])
        )
        ])
        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_case_408(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("x"), NumberType()),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())],Block([
            VarDecl(Id("a"), NumberType())
            ])
        )
        ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_case_409(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())], None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())], Return(Id("a"))),
        FuncDecl(Id("foo1"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())], Return(Id("a"))),
        FuncDecl(Id("foo1"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())], None)
        ])
        expect = "Redeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_case_410(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("x"), NumberType()),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())], Block([
            VarDecl(Id("x"), NumberType()),
            VarDecl(Id("y"), NumberType())
            ])
        ),
        VarDecl(Id("y"), NumberType()),
        VarDecl(Id("z"), NumberType()),
        VarDecl(Id("z"), StringType()),
        ])
        expect = "Redeclared Variable: z"
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    #Undeclared
    def test_case_411(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())], Return(Id("x"))),
        ])
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_case_412(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())], Return(BinaryOp("+",Id("a"),Id("y")))),
        ])
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_case_413(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())], Block([
            Assign(Id("a"),Id("x"))
            ])
        ),
        ])
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_case_414(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())], Block([
            If(BinaryOp("=",Id("a"),Id("x")),Assign(Id("a"),Id("b")))
            ])
        ),
        ])
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_case_415(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), NumberType())], Block([
            If(BinaryOp("=",Id("a"),Id("b")),Assign(Id("a"),Id("x")))
            ])
        ),
        ])
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_case_416(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), NumberType())], Block([
            For(Id("x"),BinaryOp("=",NumberLiteral(0),NumberLiteral(1)),NumberLiteral(1),Assign(Id("a"),Id("b")))
            ])
        ),
        ])
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_case_417(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("a"),None,"var",Id("b"))
        ])
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_case_418(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("a"),NumberType(),None,Id("b"))
        ])
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_case_419(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("a"),NumberType(),None,CallExpr(Id("foo"),[]))
        ])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_case_420(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("a"),None,"dynamic",CallExpr(Id("foo"),[]))
        ])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_case_421(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("a"),None,"dynamic",ArrayCell(Id("b"),[NumberLiteral(1)]))
        ])
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_case_422(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), BoolType())], Return(NumberLiteral(1))),
        VarDecl(Id("x"),NumberType(),None,CallExpr(Id("foo"),[Id("a"),Id("b")]))
        ])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_case_423(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), NumberType())], Block([
            CallStmt(Id("foo1"),[])
            ])
        )
        ])
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_case_424(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), NumberType())], Block([
            CallStmt(Id("foo"),[])
            ])
        )
        ])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 424))

    #Type Mismatch in Expression
    def test_case_425(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("a"), NumberType()),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), NumberType())], Block([
            Assign(UnaryOp('[,]',ArrayCell(Id("a"),[NumberLiteral(1)])),NumberLiteral(1))
            ])
        )
        ])
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_case_426(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("a"), ArrayType([NumberLiteral(1)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), NumberType())], Block([
            Assign(UnaryOp('[,]',ArrayCell(Id("a"),[StringLiteral("1")])),NumberLiteral(1))
            ])
        )
        ])
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_case_427(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("a"), ArrayType([NumberLiteral(1)],NumberType())),
        VarDecl(Id("b"),StringType()),
        FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()),VarDecl(Id("b"), NumberType())], Block([
            Assign(UnaryOp('[,]',ArrayCell(Id("a"),[Id("b")])),NumberLiteral(1))
            ])
        )
        ])
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [Id(b)])"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_case_428(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"), ArrayType([NumberLiteral(1)],NumberType())),
        VarDecl(Id("a"),StringType()),
        FuncDecl(Id("foo"), [VarDecl(Id("x"), NumberType()),VarDecl(Id("y"), StringType())], 
            Return(BinaryOp("+",Id("a"),Id("b")))
        )
        ])
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_case_429(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"), ArrayType([NumberLiteral(1)],NumberType())),
        VarDecl(Id("a"),StringType()),
        FuncDecl(Id("foo"), [VarDecl(Id("x"), NumberType()),VarDecl(Id("y"), NumberType())], 
            Return(BinaryOp("=",Id("x"),BinaryOp("=",Id("x"),Id("y"))))
        )
        ])
        expect = "Type Mismatch In Expression: BinaryOp(=, Id(x), BinaryOp(=, Id(x), Id(y)))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_case_430(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"), ArrayType([NumberLiteral(1)],NumberType())),
        VarDecl(Id("a"),StringType()),
        FuncDecl(Id("foo"), [VarDecl(Id("x"), BoolType()),VarDecl(Id("y"), NumberType())], 
            Return(BinaryOp("and",Id("x"),Id("y")))
        )
        ])
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(x), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_case_431(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"), ArrayType([NumberLiteral(1)],NumberType())),
        VarDecl(Id("a"),StringType()),
        FuncDecl(Id("foo"), [VarDecl(Id("x"), BoolType()),VarDecl(Id("y"), BoolType())], 
            Return(BinaryOp("or",Id("a"),BinaryOp("and",Id("x"),Id("y"))))
        )
        ])
        expect = "Type Mismatch In Expression: BinaryOp(or, Id(a), BinaryOp(and, Id(x), Id(y)))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_case_432(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"), ArrayType([NumberLiteral(1)],NumberType())),
        VarDecl(Id("a"),StringType()),
        FuncDecl(Id("foo"), [], 
            Return(NumberLiteral(1))
        ),
        FuncDecl(Id("foo1"), [], 
            Return(BinaryOp("...",Id("a"),CallExpr(Id("foo"),[])))
        )
        ])
        expect = "Type Mismatch In Expression: BinaryOp(..., Id(a), CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_case_433(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"), ArrayType([NumberLiteral(1)],NumberType())),
        VarDecl(Id("a"),StringType()),
        FuncDecl(Id("foo"), [], 
            Return(NumberLiteral(1))
        ),
        FuncDecl(Id("foo1"), [], 
            Return(UnaryOp("not",CallExpr(Id("foo"),[])))
        )
        ])
        expect = "Type Mismatch In Expression: UnaryOp(not, CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_case_434(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"), ArrayType([NumberLiteral(1)],NumberType())),
        VarDecl(Id("a"),StringType()),
        FuncDecl(Id("foo"), [], 
            Return(NumberLiteral(1))
        ),
        FuncDecl(Id("foo1"), [], 
            Return(UnaryOp("-",CallExpr(Id("foo"),[])))
        ),
        VarDecl(Id("c"),StringType(),None,CallExpr(Id("foo1"),[]))
        ])
        expect = "Type Mismatch In Statement: VarDecl(Id(c), StringType, None, CallExpr(Id(foo1), []))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_case_435(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"), ArrayType([NumberLiteral(1)],NumberType())),
        VarDecl(Id("a"),StringType()),
        FuncDecl(Id("foo"), [], Block([])),
        FuncDecl(Id("foo1"), [], 
            Return(CallExpr(Id("foo"),[]))
        ),
        ])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_case_436(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"), ArrayType([NumberLiteral(1)],NumberType())),
        VarDecl(Id("a"),StringType()),
        FuncDecl(Id("foo"), [], Return()),
        FuncDecl(Id("foo1"), [], 
            Return(CallExpr(Id("foo"),[]))
        ),
        ])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_case_437(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"), ArrayType([NumberLiteral(1)],NumberType())),
        VarDecl(Id("a"),StringType()),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType()),VarDecl(Id("b"),StringType()),VarDecl(Id("c"),BoolType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo1"), [], 
            Return(CallExpr(Id("foo"),[Id("a"),Id("a"),Id("a")]))
        ),
        ])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(a), Id(a), Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_case_438(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"), ArrayType([NumberLiteral(1)],NumberType())),
        VarDecl(Id("a"),StringType()),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo1"), [VarDecl(Id("a"),StringType())], 
            Return(NumberLiteral(1))
        ),
        VarDecl(Id("c"),NumberType(),None,CallExpr(Id("foo1"),[CallExpr(Id("foo"),[NumberLiteral(1)])])),
        ])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo1), [CallExpr(Id(foo), [NumLit(1)])])"
        self.assertTrue(TestChecker.test(input, expect, 438))

    #Type cannot be infered
    def test_case_439(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("a"),None,"var",Id("b"))
        ])
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_case_440(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("a"),None,"dynamic",Id("b"))
        ])
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_case_441(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),None,"dynamic",None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())]),
        VarDecl(Id("a"),None,"var",BinaryOp("+",Id("b"),CallExpr(Id("foo"),[Id("c")])))
        ])
        expect = "Type Cannot Be Inferred: CallExpr(Id(foo), [Id(c)])"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_case_442(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),None,"dynamic",None),
        FuncDecl(Id("foo"), [], Block([
            Assign(Id("b"),Id("c"))
        ])),
        ])
        expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test_case_443(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),None,"dynamic",None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            Assign(Id("b"),CallExpr(Id("foo"),[NumberLiteral(1)]))
        ]))
        ])
        expect = "Type Cannot Be Inferred: AssignStmt(Id(b), CallExpr(Id(foo), [NumLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_case_444(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),None,"dynamic",None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            If(Id("b"),Return())
        ]))
        ])
        expect = "Type Cannot Be Inferred: If((Id(b), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 444))
    
    def test_case_445(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            If(Id("b"),Return(),[(CallExpr(Id("foo"),[NumberLiteral(1)]),Return())])
        ]))
        ])
        expect = "Type Cannot Be Inferred: If((Id(b), Return()), [(CallExpr(Id(foo), [NumLit(1)]), Return())], None)"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_case_446(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            For(Id("c"),BooleanLiteral(True),NumberLiteral(1),Return())
        ]))
        ])
        expect = "Type Cannot Be Inferred: For(Id(c), BooleanLit(True), NumLit(1), Return())"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_case_447(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",NumberLiteral(1)),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            For(Id("c"),Id("b"),CallExpr(Id("foo"),[NumberLiteral(1)]),Return())
        ]))
        ])
        expect = "Type Cannot Be Inferred: For(Id(c), Id(b), CallExpr(Id(foo), [NumLit(1)]), Return())"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_case_448(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",NumberLiteral(1)),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            Assign(Id("c"),BinaryOp("+",Id("c"),CallExpr(Id("foo"),[NumberLiteral(1)]))),
            VarDecl(Id("x"),None,"dynamic",None),
            Assign(Id("c"),CallExpr(Id("foo"),[NumberLiteral(1)])),
            Return(Id("x"))
        ]))
        ])
        expect = "Type Cannot Be Inferred: Return(Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_case_449(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",NumberLiteral(1)),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            Return(CallExpr(Id("foo"),[NumberLiteral(1)]))
        ]))
        ])
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(foo), [NumLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 449))
    
    def test_case_450(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",NumberLiteral(1)),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return()),
        FuncDecl(Id("foo1"), [], Block([
            VarDecl(Id("x"),None, "dynamic" ,None),
            CallStmt(Id("foo"),[Id("x")])
        ]))
        ])
        expect = "Type Cannot Be Inferred: CallStmt(Id(foo), [Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_case_451(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",NumberLiteral(1)),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType()),VarDecl(Id("b"),BoolType()),VarDecl(Id("c"),StringType())], Return()),
        FuncDecl(Id("foo1"), [], Block([
            VarDecl(Id("x"),None, "dynamic" ,None),
            CallStmt(Id("foo"),[Id("c"),Id("b"),Id("x")])
        ]))
        ])
        expect = "Type Cannot Be Inferred: CallStmt(Id(foo), [Id(c), Id(b), Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 451))

    #Type Mismatch in Statement
    def test_case_452(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",NumberLiteral(1)),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType()),VarDecl(Id("b"),BoolType()),VarDecl(Id("c"),StringType())], Return()),
        FuncDecl(Id("foo1"), [], Block([
            If(Id("c"),Return())
        ]))
        ])
        expect = "Type Mismatch In Statement: If((Id(c), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_case_453(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",NumberLiteral(1)),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType()),VarDecl(Id("b"),BoolType()),VarDecl(Id("c"),StringType())], Return()),
        FuncDecl(Id("foo1"), [], Block([
            If(Id("b"),Return()),
            If(Id("b"),Return(),[(Id("c"),Return())])
        ]))
        ])
        expect = "Type Mismatch In Statement: If((Id(b), Return()), [(Id(c), Return())], None)"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_case_454(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",NumberLiteral(1)),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType()),VarDecl(Id("b"),BoolType()),VarDecl(Id("c"),StringType())], Return()),
        FuncDecl(Id("foo1"), [], Block([
            For(Id("c"),Id("c"),Id("c"),Return())
        ]))
        ])
        expect = "Type Mismatch In Statement: For(Id(c), Id(c), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_case_455(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",NumberLiteral(1)),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType()),VarDecl(Id("b"),BoolType()),VarDecl(Id("c"),StringType())], Return()),
        FuncDecl(Id("foo1"), [], Block([
            If(BinaryOp("+",Id("c"),Id("c")),Return())
        ]))
        ])
        expect = "Type Mismatch In Statement: If((BinaryOp(+, Id(c), Id(c)), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_case_456(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",NumberLiteral(1)),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType()),VarDecl(Id("b"),BoolType()),VarDecl(Id("c"),StringType())], Return()),
        FuncDecl(Id("foo1"), [], Block([
            VarDecl(Id("x"),None,"dynamic",None),
            If(BinaryOp("=",Id("c"),Id("c")),For(Id("c"),BinaryOp('+',Id("x"),Id("c")),Id("c"),Return()))
        ]))
        ])
        expect = "Type Mismatch In Statement: For(Id(c), BinaryOp(+, Id(x), Id(c)), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_case_457(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",NumberLiteral(1)),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(StringLiteral("ok"))),
        FuncDecl(Id("foo1"), [], Block([
            Assign(CallExpr(Id("foo"),[NumberLiteral(1)]),Id("c"))
        ]))
        ])
        expect = "Type Mismatch In Statement: AssignStmt(CallExpr(Id(foo), [NumLit(1)]), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_case_458(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())], Return()),
        FuncDecl(Id("foo1"), [], Block([
            Assign(Id("b"),Id("c")),
            Assign(CallExpr(Id("foo"),[NumberLiteral(1)]),Id("c"))
        ]))
        ])
        expect = "Type Mismatch In Statement: AssignStmt(CallExpr(Id(foo), [NumLit(1)]), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_case_459(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            Assign(Id("c"),Id("b")),
            Assign(CallExpr(Id("foo2"),[NumberLiteral(1)]),Id("c")),
            Assign(CallExpr(Id("foo2"),[NumberLiteral(1)]),CallExpr(Id("foo"),[NumberLiteral(1)]))
        ]))
        ])
        expect = "Type Mismatch In Statement: AssignStmt(CallExpr(Id(foo2), [NumLit(1)]), CallExpr(Id(foo), [NumLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_case_460(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",BooleanLiteral(True)),
        VarDecl(Id("c"),None,"dynamic",None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            VarDecl(Id("x"),ArrayType([NumberLiteral(2)],NumberType())),
            Assign(Id("x"),Id("b"))
        ]))
        ])
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_case_461(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),ArrayType([NumberLiteral(1)],NumberType())),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo1"), [], Block([
            VarDecl(Id("x"),ArrayType([NumberLiteral(2)],NumberType())),
            Assign(Id("x"),Id("c")),
            Assign(Id("x"),Id("b"))
        ]))
        ])
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_case_462(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),ArrayType([NumberLiteral(2)],BoolType())),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            VarDecl(Id("x"),ArrayType([NumberLiteral(2)],NumberType())),
            Assign(Id("x"),Id("c")),
            Assign(Id("x"),Id("b"))
        ]))
        ])
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_case_463(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            VarDecl(Id("x"),ArrayType([NumberLiteral(1)],NumberType())),
            Assign(Id("b"),Id("c")),
            Assign(Id("c"),Id("b")),
            Assign(Id("x"),Id("b"))
        ]))
        ])
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_case_464(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            VarDecl(Id("x"),ArrayType([NumberLiteral(1)],NumberType())),
            Assign(CallExpr(Id("foo2"),[NumberLiteral(1)]),Id("c")),
            Assign(Id("c"),CallExpr(Id("foo2"),[NumberLiteral(1)])),
            Assign(Id("x"),CallExpr(Id("foo2"),[NumberLiteral(1)]))
        ]))
        ])
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), CallExpr(Id(foo2), [NumLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 464))
    
    def test_case_465(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),ArrayType([NumberLiteral(2)],NumberType())),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            Assign(ArrayCell(Id("c"),[NumberLiteral(1)]),Id("b"))
        ]))
        ])
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(c), [NumLit(1)]), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_case_466(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            Assign(ArrayCell(Id("c"),[NumberLiteral(1)]),Id("b")),
            Assign(Id("c"),CallExpr(Id("foo2"),[NumberLiteral(1)])),
            Assign(Id("b"),CallExpr(Id("foo2"),[NumberLiteral(1)]))
        ]))
        ])
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), CallExpr(Id(foo2), [NumLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_case_467(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            CallStmt(Id("foo"),[NumberLiteral(1)])
        ]))
        ])
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_case_468(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            CallStmt(Id("foo2"),[NumberLiteral(1)]),
            CallStmt(Id("foo"),[NumberLiteral(1)])
        ]))
        ])
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test_case_469(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            CallStmt(Id("foo2"),[NumberLiteral(1),NumberLiteral(1)]),
        ]))
        ])
        expect = "Type Mismatch In Statement: CallStmt(Id(foo2), [NumLit(1), NumLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_case_470(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), []),
        FuncDecl(Id("foo1"), [], Block([
            CallStmt(Id("foo2"),[NumberLiteral(1)]),
        ]))
        ])
        expect = "Type Mismatch In Statement: CallStmt(Id(foo2), [NumLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_case_471(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            CallStmt(Id("foo2"),[StringLiteral(1)]),
        ]))
        ])
        expect = "Type Mismatch In Statement: CallStmt(Id(foo2), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_case_472(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())], Return(NumberLiteral(1))),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            CallStmt(Id("foo2"),[CallExpr(Id("foo"),[NumberLiteral(1)])]),
            CallStmt(Id("foo"),[Id("c")])
        ]))
        ])
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [Id(c)])"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_case_473(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo2"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            Assign(Id("c"),CallExpr(Id("foo"),[NumberLiteral(1)])),
            CallStmt(Id("foo2"),[ArrayCell(CallExpr(Id("foo"),[NumberLiteral(1)]),[NumberLiteral(1)])]),
            CallStmt(Id("foo"),[Id("c")])
        ]))
        ])
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [Id(c)])"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_case_474(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())],Block([
            Assign(Id("a"),BooleanLiteral(True))
        ])),
        ])
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_case_475(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType()),None,NumberLiteral(1)),
        ])
        expect = "Type Mismatch In Statement: VarDecl(Id(c), ArrayType([NumLit(2)], NumberType), None, NumLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_case_476(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType()),None,ArrayLiteral([NumberLiteral(1)])),
        ])
        expect = "Type Mismatch In Statement: VarDecl(Id(c), ArrayType([NumLit(2)], NumberType), None, ArrayLit(NumLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_case_477(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),

        VarDecl(Id("c"),ArrayType([NumberLiteral(1)],NumberType()),None,ArrayLiteral([NumberLiteral(1)])),
        VarDecl(Id("x"),ArrayType([NumberLiteral(1)],NumberType()),None,ArrayLiteral([StringLiteral("fail")]))
        ])
        expect = "Type Mismatch In Statement: VarDecl(Id(x), ArrayType([NumLit(1)], NumberType), None, ArrayLit(StringLit(fail)))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_case_478(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"var",None),
        ])
        expect = "Type Mismatch In Statement: VarDecl(Id(b), None, var, None)"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_case_479(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),NumberType(),"var",StringLiteral("fail")),
        ])
        expect = "Type Mismatch In Statement: VarDecl(Id(b), NumberType, var, StringLit(fail))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_case_480(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        VarDecl(Id("c"),ArrayType([NumberLiteral(2)],NumberType())),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())]),
        FuncDecl(Id("foo1"), [], Block([
            Assign(Id("c"),CallExpr(Id("foo"),[NumberLiteral(1)])),
            VarDecl(Id("x"),ArrayType([NumberLiteral(2)],NumberType()),None,CallExpr(Id("foo"),[NumberLiteral(1)])),
            VarDecl(Id("y"),ArrayType([NumberLiteral(1)],NumberType()),None,Id("x"))
        ]))
        ])
        expect = "Type Mismatch In Statement: VarDecl(Id(y), ArrayType([NumLit(1)], NumberType), None, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_case_481(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        VarDecl(Id("b"),None,"dynamic",None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())],Return(NumberLiteral(1))),
        VarDecl(Id("c"),ArrayType([NumberLiteral(1)],NumberType()),None,ArrayLiteral([CallExpr(Id("foo"),[NumberLiteral(1)])])),
        VarDecl(Id("x"),ArrayType([NumberLiteral(1)],NumberType()),None,ArrayLiteral([StringLiteral("fail")]))
        ])
        expect = "Type Mismatch In Statement: VarDecl(Id(x), ArrayType([NumLit(1)], NumberType), None, ArrayLit(StringLit(fail)))"
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    #No definition for a function
    def test_case_482(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())]),
        ])
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_case_483(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), []),
        ])
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_case_484(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), []),
        FuncDecl(Id("foo"), [VarDecl(Id("a"),NumberType())])
        ])
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_case_485(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), []),
        FuncDecl(Id("foo1"), [], Return(BinaryOp("+",NumberLiteral(1),CallExpr(Id("foo"),[])))),
        FuncDecl(Id("foo2"), [])
        ])
        expect = "No Function Definition: foo2"
        self.assertTrue(TestChecker.test(input, expect, 485))

    #Break/Loop not in loop
    def test_case_486(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [], Block([
            Break()
        ])),
        ])
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_case_487(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [], Block([
            Continue()
        ])),
        ])
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_case_488(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [], Block([
            VarDecl(Id("b"),NumberType()),
            VarDecl(Id("c"),NumberType()),
            For(Id("b"),BooleanLiteral(True),NumberLiteral(1),For(Id("c"),BooleanLiteral(True),NumberLiteral(1),Break())),
            Break()
        ])),
        ])
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 488))
    def test_case_489(self):
        input = Program([
        FuncDecl(Id("main"), [],None),
        FuncDecl(Id("foo"), [], Block([
            VarDecl(Id("b"),NumberType()),
            VarDecl(Id("c"),NumberType()),
            For(Id("b"),BooleanLiteral(True),NumberLiteral(1),For(Id("c"),BooleanLiteral(True),NumberLiteral(1),Break())),
            Continue()
        ])),
        ])
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 489))

    #No Entry Point
    def test_case_490(self):
        input = Program([
        FuncDecl(Id("foo"), [], Block([
            VarDecl(Id("b"),NumberType()),
        ])),
        ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_case_491(self):
        input = Program([
        FuncDecl(Id("main1"), [],None),
        FuncDecl(Id("foo"), [], Block([
            VarDecl(Id("b"),NumberType()),
        ])),
        ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_case_492(self):
        input = Program([
        FuncDecl(Id("main"), [VarDecl(Id("b"),NumberType())],Return()),
        FuncDecl(Id("foo"), [], Block([
            VarDecl(Id("b"),NumberType()),
        ])),
        ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 492))


    def test_case_493(self):
        input = Program([
        FuncDecl(Id("main"), [],Return(NumberLiteral(1))),
        FuncDecl(Id("foo"), [], Block([
            VarDecl(Id("b"),NumberType()),
        ])),
        ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_case_494(self):
        input = Program([
        FuncDecl(Id("Main"), [],Return()),
        FuncDecl(Id("foo"), [], Block([
            VarDecl(Id("b"),NumberType()),
        ])),
        ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_case_495(self):
        input = Program([
        FuncDecl(Id("main"), []),
        FuncDecl(Id("foo"), [], Block([
            VarDecl(Id("b"),NumberType()),
            Assign(Id("b"),CallExpr(Id("main"),[]))
        ])),
        ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_case_496(self):
        input = Program([
        FuncDecl(Id("m a i n"), []),
        FuncDecl(Id("foo"), [], Block([
            VarDecl(Id("b"),NumberType())
        ])),
        ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_case_497(self):
        input = Program([
        FuncDecl(Id("foo"), [], Block([
            VarDecl(Id("b"),NumberType())
        ])),
        FuncDecl(Id("main"),[]),
        VarDecl(Id("b"),NumberType(),None,CallExpr(Id("main"),[]))
        ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_case_498(self):
        input = Program([
        FuncDecl(Id("main"),[],Block([
            VarDecl(Id("b"),NumberType())
        ])),
        VarDecl(Id("a"),NumberType(),None,CallExpr(Id("main"),[]))
        ])
        expect = "Type Mismatch In Expression: CallExpr(Id(main), [])"
        self.assertTrue(TestChecker.test(input, expect, 498))
    
    def test_case_Thank_you_for_checking(self):
        input = Program([
        FuncDecl(Id("Please take it easy for me T.T"),[],Block([])),
        ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 499))