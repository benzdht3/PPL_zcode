import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_301(self):
        input = """var str <- "Hello world!"
        """
        expect = str(Program([VarDecl(Id("str"), None, "var", StringLiteral("Hello world!"))]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        input = """func main() return 1
        """
        expect = str(Program([FuncDecl(Id("main"), [], Return(NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input, expect, 302))
    
    def test_303(self):
        input ="""func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = str(Program([FuncDecl(Id("inc"), [VarDecl(Id("a"), NumberType(), None, None)], Return(BinaryOp("+", Id("a"), NumberLiteral(1.0)))), FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), None, "var", NumberLiteral(1.0)), CallStmt(Id("inc"), [Id("a")]), CallStmt(Id("writeNumber"), [Id("a")])]))]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        input = """func main() begin
        number a
        if (5 < 2) a <- 1
        elif (not true) a <- 2
        elif ("h" == "6") a <- 3
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, None), If(BinaryOp("<", NumberLiteral(5.0), NumberLiteral(2.0)), Assign(Id("a"), NumberLiteral(1.0)), [(UnaryOp("not", BooleanLiteral(True)), Assign(Id("a"), NumberLiteral(2.0))), (BinaryOp("==", StringLiteral("h"), StringLiteral("6")), Assign(Id("a"), NumberLiteral(3.0)))], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = """func main() begin
        if (1) writeString("1")
        elif (2) if(3) writeString("1")
        elif (4) writeString("1")
        else writeString("1")
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(NumberLiteral(1.0), CallStmt(Id("writeString"), [StringLiteral("1")]), [(NumberLiteral(2.0), If(NumberLiteral(3.0), CallStmt(Id("writeString"), [StringLiteral("1")]), [(NumberLiteral(4.0), CallStmt(Id("writeString"), [StringLiteral("1")]))], CallStmt(Id("writeString"), [StringLiteral("1")])))], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = """
        func main()
        begin
            var i <- 0
            number j <- 0
            for i until i <= 10 by 2
            begin
                for j until j <= 20 by 4
                    writeNumber(i*j)
            end
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), VarDecl(Id("j"), NumberType(), None, NumberLiteral(0.0)), For(Id("i"), BinaryOp("<=", Id("i"), NumberLiteral(10.0)), NumberLiteral(2.0), Block([For(Id("j"), BinaryOp("<=", Id("j"), NumberLiteral(20.0)), NumberLiteral(4.0), CallStmt(Id("writeNumber"), [BinaryOp("*", Id("i"), Id("j"))]))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = """
        number a <- 100

        func sum(number n)
        begin
            if (n = 0) return 0
            return n + sum(n - 1)
        end

        func main()
        begin
            writeNumber(sum(a))
        end
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, NumberLiteral(100.0)), FuncDecl(Id("sum"), [VarDecl(Id("n"), NumberType(), None, None)], Block([If(BinaryOp("=", Id("n"), NumberLiteral(0.0)), Return(NumberLiteral(0.0)), [], None), Return(BinaryOp("+", Id("n"), CallExpr(Id("sum"), [BinaryOp("-", Id("n"), NumberLiteral(1.0))])))])), FuncDecl(Id("main"), [], Block([CallStmt(Id("writeNumber"), [CallExpr(Id("sum"), [Id("a")])])]))]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input = """number a[1]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([1], NumberType()), None, None)]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input = """number a <- 1 + 2 + 3 + 4
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, BinaryOp("+", BinaryOp("+", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0)))]))
        self.assertTrue(TestAST.test(input, expect, 309))

    
    def test_310(self):
        input = """func main() begin
        var result <- 5 + 3 * 2
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("result"), None, "var", BinaryOp("+", NumberLiteral(5.0), BinaryOp("*", NumberLiteral(3.0), NumberLiteral(2.0))))]))]))
        self.assertTrue(TestAST.test(input, expect, 310))

    
    def test_311(self):
        input = """func add(number a, number b) return a + b
        func main() begin
        var result <- add(5, 3)
        end
        """
        expect = str(Program([FuncDecl(Id("add"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Return(BinaryOp("+", Id("a"), Id("b")))), FuncDecl(Id("main"), [], Block([VarDecl(Id("result"), None, "var", CallExpr(Id("add"), [NumberLiteral(5.0), NumberLiteral(3.0)]))]))]))
        self.assertTrue(TestAST.test(input, expect, 311))

    
    def test_312(self):
        input = """func main() begin
        number arr[5] <- [1, 2, 3, 4, 5]
        var value <- arr[2]
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("arr"), ArrayType([5], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0), NumberLiteral(5.0)])), VarDecl(Id("value"), None, "var", ArrayCell(Id("arr"), [NumberLiteral(2.0)]))]))]))
        self.assertTrue(TestAST.test(input, expect, 312))

    
    def test_313(self):
        input = """func main()
        begin
        string str <- "Hello" ... "World"
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("str"), StringType(), None, BinaryOp("...", StringLiteral("Hello"), StringLiteral("World")))]))]))
        self.assertTrue(TestAST.test(input, expect, 313))

    
    def test_314(self):
        input = """func main() 
        begin
        var x <- 10
        if (x > 5) begin
        if (x < 15) begin
        var y <- 20
        end
        end
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), None, "var", NumberLiteral(10.0)), If(BinaryOp(">", Id("x"), NumberLiteral(5.0)), Block([If(BinaryOp("<", Id("x"), NumberLiteral(15.0)), Block([VarDecl(Id("y"), None, "var", NumberLiteral(20.0))]), [], None)]), [], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 314))

    
    def test_315(self):
        input = """func main() 
        begin
        var flag <- true and false
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("flag"), None, "var", BinaryOp("and", BooleanLiteral(True), BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.test(input, expect, 315))

    
    def test_316(self):
        input = """
        var result <- (5 + 3) * 2 - 4 / 2
        """
        expect = str(Program([VarDecl(Id("result"), None, "var", BinaryOp("-", BinaryOp("*", BinaryOp("+", NumberLiteral(5.0), NumberLiteral(3.0)), NumberLiteral(2.0)), BinaryOp("/", NumberLiteral(4.0), NumberLiteral(2.0))))]))
        self.assertTrue(TestAST.test(input, expect, 316))

    
    def test_317(self):
        input = """func main() 
        begin
        var x <- 10
        if (x > 5) begin
        var y <- 20
        end 
        else begin
        var z <- 30
        end
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), None, "var", NumberLiteral(10.0)), If(BinaryOp(">", Id("x"), NumberLiteral(5.0)), Block([VarDecl(Id("y"), None, "var", NumberLiteral(20.0))]), [], Block([VarDecl(Id("z"), None, "var", NumberLiteral(30.0))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 317))

    
    def test_318(self):
        input = """func main() 
        begin
        var i <- 0
        for i until i < 5 by 1 begin
        if (i == 3) begin
            break
        end
        end
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([If(BinaryOp("==", Id("i"), NumberLiteral(3.0)), Block([Break()]), [], None)]))]))]))
        self.assertTrue(TestAST.test(input, expect, 318))

    
    def test_319(self):
        input = """func sumArray(number arr[3]) begin
        var sum <- arr[0] + arr[1] + arr[2]
        end
        """
        expect = str(Program([FuncDecl(Id("sumArray"), [VarDecl(Id("arr"), ArrayType([NumberLiteral(3.0)], NumberType()), None, None)], Block([VarDecl(Id("sum"), None, "var", BinaryOp("+", BinaryOp("+", ArrayCell(Id("arr"), [NumberLiteral(0.0)]), ArrayCell(Id("arr"), [NumberLiteral(1.0)])), ArrayCell(Id("arr"), [NumberLiteral(2.0)])))]))]))
        self.assertTrue(TestAST.test(input, expect, 319))

    
    def test_320(self):
        input = """func main() begin
        a[3 + foo(2)] <- a[b[2, 3]] + 4
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Assign(ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(3.0), CallExpr(Id("foo"), [NumberLiteral(2.0)]))]), BinaryOp("+", ArrayCell(Id("a"), [ArrayCell(Id("b"), [NumberLiteral(2.0), NumberLiteral(3.0)])]), NumberLiteral(4.0)))]))]))
        self.assertTrue(TestAST.test(input, expect, 320))

    
    def test_321(self):
        input = """func foo(number a[5], string b) 
        begin 
        var i <- 0 
        for i until i >= 5 by 1 
        begin 
        a[i] <- i * i + 5 
        end 
        return -1 
        end

        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), ArrayType([NumberLiteral(5.0)], NumberType()), None, None), VarDecl(Id("b"), StringType(), None, None)], Block([VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp(">=", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([Assign(ArrayCell(Id("a"), [Id("i")]), BinaryOp("+", BinaryOp("*", Id("i"), Id("i")), NumberLiteral(5.0)))])), Return(UnaryOp("-", NumberLiteral(1.0)))]))]))
        self.assertTrue(TestAST.test(input, expect, 321))

    
    def test_322(self):
        input = """func areDivisors(number num1, number num2) return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main() 
        begin 
        var num1 <- readNumber() 
        var num2 <- readNumber()
        if (areDivisors(num1, num2)) printString("Yes") 
        else printString("No")
        end
        """
        expect = str(Program([FuncDecl(Id("areDivisors"), [VarDecl(Id("num1"), NumberType(), None, None), VarDecl(Id("num2"), NumberType(), None, None)], Return(BinaryOp("or", BinaryOp("=", BinaryOp("%", Id("num1"), Id("num2")), NumberLiteral(0.0)), BinaryOp("=", BinaryOp("%", Id("num2"), Id("num1")), NumberLiteral(0.0))))), FuncDecl(Id("main"), [], Block([VarDecl(Id("num1"), None, "var", CallExpr(Id("readNumber"), [])), VarDecl(Id("num2"), None, "var", CallExpr(Id("readNumber"), [])), If(CallExpr(Id("areDivisors"), [Id("num1"), Id("num2")]), CallStmt(Id("printString"), [StringLiteral("Yes")]), [], CallStmt(Id("printString"), [StringLiteral("No")]))]))]))
        self.assertTrue(TestAST.test(input, expect, 322))

    
    def test_323(self):
        input = """func isPrime(number x)
        func main() 
        begin 
        number x <- readNumber() 
        if (isPrime(x)) printString("Yes") 
        else printString("No") 
        end
        func isPrime(number x) 
        begin 
        if (x <= 1) return false 
        var i <- 2 
        for i until i > x / 2 by 1 
        begin 
        if (x % i = 0) return false 
        end 
        return true 
        end
        """
        expect = str(Program([FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType(), None, None)], None), FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), NumberType(), None, CallExpr(Id("readNumber"), [])), If(CallExpr(Id("isPrime"), [Id("x")]), CallStmt(Id("printString"), [StringLiteral("Yes")]), [], CallStmt(Id("printString"), [StringLiteral("No")]))])), FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType(), None, None)], Block([If(BinaryOp("<=", Id("x"), NumberLiteral(1.0)), Return(BooleanLiteral(True)), [], None), VarDecl(Id("i"), None, "var", NumberLiteral(2.0)), For(Id("i"), BinaryOp(">", Id("i"), BinaryOp("/", Id("x"), NumberLiteral(2.0))), NumberLiteral(1.0), Block([If(BinaryOp("=", BinaryOp("%", Id("x"), Id("i")), NumberLiteral(0.0)), Return(BooleanLiteral(True)), [], None)])), Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input, expect, 323))

    
    def test_324(self):
        input = """func main()
        begin
        number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("b"), ArrayType([2, 3], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 324))

    
    def test_325(self):
        input = """func concatenate(string str1, string str2) return str1 ... str2
        func main() 
        begin
        string result <- concatenate("Hello", "World")
        end
        """
        expect = str(Program([FuncDecl(Id("concatenate"), [VarDecl(Id("str1"), StringType(), None, None), VarDecl(Id("str2"), StringType(), None, None)], Return(BinaryOp("...", Id("str1"), Id("str2")))), FuncDecl(Id("main"), [], Block([VarDecl(Id("result"), StringType(), None, CallExpr(Id("concatenate"), [StringLiteral("Hello"), StringLiteral("World")]))]))]))
        self.assertTrue(TestAST.test(input, expect, 325))

    
    def test_326(self):
        input = """func printMessage(bool flag) 
        begin
        if (flag) 
        begin
        printString("True")
        end 
        else 
        begin
        printString("False")
        end
        end
        """
        expect = str(Program([FuncDecl(Id("printMessage"), [VarDecl(Id("flag"), BoolType(), None, None)], Block([If(Id("flag"), Block([CallStmt(Id("printString"), [StringLiteral("True")])]), [], Block([CallStmt(Id("printString"), [StringLiteral("False")])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 326))

    
    def test_327(self):
        input = """func createArray() return [1, 2, 3, 4, 5]
        """
        expect = str(Program([FuncDecl(Id("createArray"), [], Return(ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0), NumberLiteral(5.0)])))]))
        self.assertTrue(TestAST.test(input, expect, 327))

    
    def test_328(self):
        input = """func checkRange(number x) 
        begin
        if (x > 0) 
        begin
        if (x < 10) 
        begin
        printString("In range")
        end
        end
        end
        """
        expect = str(Program([FuncDecl(Id("checkRange"), [VarDecl(Id("x"), NumberType(), None, None)], Block([If(BinaryOp(">", Id("x"), NumberLiteral(0.0)), Block([If(BinaryOp("<", Id("x"), NumberLiteral(10.0)), Block([CallStmt(Id("printString"), [StringLiteral("In range")])]), [], None)]), [], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 328))

    
    def test_329(self):
        input = """func factorial(number n) 
        begin
        if (n <= 1) 
        begin
        return 1
        end
        return n * factorial(n - 1)
        end
        """
        expect = str(Program([FuncDecl(Id("factorial"), [VarDecl(Id("n"), NumberType(), None, None)], Block([If(BinaryOp("<=", Id("n"), NumberLiteral(1.0)), Block([Return(NumberLiteral(1.0))]), [], None), Return(BinaryOp("*", Id("n"), CallExpr(Id("factorial"), [BinaryOp("-", Id("n"), NumberLiteral(1.0))])))]))]))
        self.assertTrue(TestAST.test(input, expect, 329))

    
    def test_330(self):
        input = """func calculateExpression(number a, number b) 
        begin
        var result <- (a + b) * (a - b)
        end
        """
        expect = str(Program([FuncDecl(Id("calculateExpression"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Block([VarDecl(Id("result"), None, "var", BinaryOp("*", BinaryOp("+", Id("a"), Id("b")), BinaryOp("-", Id("a"), Id("b"))))]))]))
        self.assertTrue(TestAST.test(input, expect, 330))

    
    def test_331(self):
        input = """func processArray(number arr[5]) 
        begin
        for i until i < 5 by 1 
        begin
        arr[i] <- arr[i] * arr[i]
        end
        end
        """
        expect = str(Program([FuncDecl(Id("processArray"), [VarDecl(Id("arr"), ArrayType([NumberLiteral(5.0)], NumberType()), None, None)], Block([For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([Assign(ArrayCell(Id("arr"), [Id("i")]), BinaryOp("*", ArrayCell(Id("arr"), [Id("i")]), ArrayCell(Id("arr"), [Id("i")])))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 331))

    
    def test_332(self):
        input = """func checkString(string str) 
        begin
        if (str = "Hello") 
        begin
        printString("Greeting detected")
        end
        end
        """
        expect = str(Program([FuncDecl(Id("checkString"), [VarDecl(Id("str"), StringType(), None, None)], Block([If(BinaryOp("=", Id("str"), StringLiteral("Hello")), Block([CallStmt(Id("printString"), [StringLiteral("Greeting detected")])]), [], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 332))

    
    def test_333(self):
        input = """func generateArray(bool flag)
        begin
        if (flag) return [4, 5, 6]
        else return [7, 8, 9]
        end
        """
        expect = str(Program([FuncDecl(Id("generateArray"), [VarDecl(Id("flag"), BoolType(), None, None)], Block([If(Id("flag"), Return(ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])), [], Return(ArrayLiteral([NumberLiteral(7.0), NumberLiteral(8.0), NumberLiteral(9.0)])))]))]))
        self.assertTrue(TestAST.test(input, expect, 333))

    
    def test_334(self):
        input = """func fibonacci(number n) 
        begin
        if (n <= 1) begin
        return n
        end
        return fibonacci(n - 1) + fibonacci(n - 2)
        end
        """
        expect = str(Program([FuncDecl(Id("fibonacci"), [VarDecl(Id("n"), NumberType(), None, None)], Block([If(BinaryOp("<=", Id("n"), NumberLiteral(1.0)), Block([Return(Id("n"))]), [], None), Return(BinaryOp("+", CallExpr(Id("fibonacci"), [BinaryOp("-", Id("n"), NumberLiteral(1.0))]), CallExpr(Id("fibonacci"), [BinaryOp("-", Id("n"), NumberLiteral(2.0))])))]))]))
        self.assertTrue(TestAST.test(input, expect, 334))

    
    def test_335(self):
        input = """func printOddNumbers()
        begin
        var i <- 0
        for i until i < 10 by 1 
        begin
        if (i % 2 = 0) begin
        continue
        end
        writeNumber(i)
        end
        end
        """
        expect = str(Program([FuncDecl(Id("printOddNumbers"), [], Block([VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), Block([If(BinaryOp("=", BinaryOp("%", Id("i"), NumberLiteral(2.0)), NumberLiteral(0.0)), Block([Continue()]), [], None), CallStmt(Id("writeNumber"), [Id("i")])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 335))

    
    def test_336(self):
        input = """func checkConditions(number a, number b, bool flag) 
        begin
        if (flag and (a > b)) 
        begin
        printString("Condition met")
        end 
        else 
        begin
        printString("Condition not met")
        end
        end
        """
        expect = str(Program([FuncDecl(Id("checkConditions"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None), VarDecl(Id("flag"), BoolType(), None, None)], Block([If(BinaryOp("and", Id("flag"), BinaryOp(">", Id("a"), Id("b"))), Block([CallStmt(Id("printString"), [StringLiteral("Condition met")])]), [], Block([CallStmt(Id("printString"), [StringLiteral("Condition not met")])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 336))

    
    def test_337(self):
        input = """func gcd(number a, number b)
        begin
        if (b = 0) begin
        return a
        end
        return gcd(b, a % b)
        end
        """
        expect = str(Program([FuncDecl(Id("gcd"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Block([If(BinaryOp("=", Id("b"), NumberLiteral(0.0)), Block([Return(Id("a"))]), [], None), Return(CallExpr(Id("gcd"), [Id("b"), BinaryOp("%", Id("a"), Id("b"))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 337))

    
    def test_338(self):
        input = """func checkValue(number x) 
        begin
        if (x < 0) 
        begin
        return "Negative"
        end 
        else 
        if (x = 0) 
        begin
        return "Zero"
        end 
        else 
        begin
        return "Positive"
        end
        end
        """
        expect = str(Program([FuncDecl(Id("checkValue"), [VarDecl(Id("x"), NumberType(), None, None)], Block([If(BinaryOp("<", Id("x"), NumberLiteral(0.0)), Block([Return(StringLiteral("Negative"))]), [], If(BinaryOp("=", Id("x"), NumberLiteral(0.0)), Block([Return(StringLiteral("Zero"))]), [], Block([Return(StringLiteral("Positive"))])))]))]))
        self.assertTrue(TestAST.test(input, expect, 338))

    
    def test_339(self):
        input = """func processArray(number arr[5]) 
        begin
        var sum <- 0
        var i <- 0
        for i until i < 5 by 1 
        begin
        if (arr[i] > 0) 
        begin
        sum <- sum + arr[i]
        end 
        else
        begin
        sum <- sum - arr[i]
        end
        end
        end
        """
        expect = str(Program([FuncDecl(Id("processArray"), [VarDecl(Id("arr"), ArrayType([NumberLiteral(5.0)], NumberType()), None, None)], Block([VarDecl(Id("sum"), None, "var", NumberLiteral(0.0)), VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([If(BinaryOp(">", ArrayCell(Id("arr"), [Id("i")]), NumberLiteral(0.0)), Block([Assign(Id("sum"), BinaryOp("+", Id("sum"), ArrayCell(Id("arr"), [Id("i")])))]), [], Block([Assign(Id("sum"), BinaryOp("-", Id("sum"), ArrayCell(Id("arr"), [Id("i")])))]))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 339))

    
    def test_340(self):
        input = """func generateMatrix() 
        begin
        number matrix[3, 3]
        var i <- 0
        for i until i < 3 by 1 
        begin
        var j <- 0
        for j until j < 3 by 1 
        begin
        matrix[i, j] <- i + j
        end
        end
        return matrix
        end
        """
        expect = str(Program([FuncDecl(Id("generateMatrix"), [], Block([VarDecl(Id("matrix"), ArrayType([3, 3], NumberType()), None, None), VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(3.0)), NumberLiteral(1.0), Block([VarDecl(Id("j"), None, "var", NumberLiteral(0.0)), For(Id("j"), BinaryOp("<", Id("j"), NumberLiteral(3.0)), NumberLiteral(1.0), Block([Assign(ArrayCell(Id("matrix"), [Id("i"), Id("j")]), BinaryOp("+", Id("i"), Id("j")))]))])), Return(Id("matrix"))]))]))
        self.assertTrue(TestAST.test(input, expect, 340))

    
    def test_341(self):
        input = """func capitalizeString(string str) 
        begin
        var firstChar <- str[0]
        var remaining <- substring(str, 1)
        return upper(firstChar) + remaining
        end
        """
        expect = str(Program([FuncDecl(Id("capitalizeString"), [VarDecl(Id("str"), StringType(), None, None)], Block([VarDecl(Id("firstChar"), None, "var", ArrayCell(Id("str"), [NumberLiteral(0.0)])), VarDecl(Id("remaining"), None, "var", CallExpr(Id("substring"), [Id("str"), NumberLiteral(1.0)])), Return(BinaryOp("+", CallExpr(Id("upper"), [Id("firstChar")]), Id("remaining")))]))]))
        self.assertTrue(TestAST.test(input, expect, 341))

    
    def test_342(self):
        input = """func sumOfDigits(number n) 
        return n % 10 + sumOfDigits(n / 10)
        """
        expect = str(Program([FuncDecl(Id("sumOfDigits"), [VarDecl(Id("n"), NumberType(), None, None)], Return(BinaryOp("+", BinaryOp("%", Id("n"), NumberLiteral(10.0)), CallExpr(Id("sumOfDigits"), [BinaryOp("/", Id("n"), NumberLiteral(10.0))]))))]))
        self.assertTrue(TestAST.test(input, expect, 342))

    
    def test_343(self):
        input = """func reverseString(string str) 
        begin
        var reversed <- ""
        var i <- length(str) - 1
        for i until i >= 0 by -1 
        begin
        reversed <- reversed + str[i]
        end
        return reversed
        end
        """
        expect = str(Program([FuncDecl(Id("reverseString"), [VarDecl(Id("str"), StringType(), None, None)], Block([VarDecl(Id("reversed"), None, "var", StringLiteral("")), VarDecl(Id("i"), None, "var", BinaryOp("-", CallExpr(Id("length"), [Id("str")]), NumberLiteral(1.0))), For(Id("i"), BinaryOp(">=", Id("i"), NumberLiteral(0.0)), UnaryOp("-", NumberLiteral(1.0)), Block([Assign(Id("reversed"), BinaryOp("+", Id("reversed"), ArrayCell(Id("str"), [Id("i")])))])), Return(Id("reversed"))]))]))
        self.assertTrue(TestAST.test(input, expect, 343))

    
    def test_344(self):
        input = """func countVowels(string str) 
        begin
        var vowels <- 0
        var i <- 0
        for i until i < length(str) by 1 begin
        if (str[i] = "a" or str[i] = "e" or str[i] = "i" or str[i] = "o" or str[i] = "u") begin
        vowels <- vowels + 1
        end
        end
        return vowels
        end
        """
        expect = str(Program([FuncDecl(Id("countVowels"), [VarDecl(Id("str"), StringType(), None, None)], Block([VarDecl(Id("vowels"), None, "var", NumberLiteral(0.0)), VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp("<", Id("i"), CallExpr(Id("length"), [Id("str")])), NumberLiteral(1.0), Block([If(BinaryOp("or", BinaryOp("or", BinaryOp("or", BinaryOp("or", BinaryOp("=", ArrayCell(Id("str"), [Id("i")]), StringLiteral("a")), BinaryOp("=", ArrayCell(Id("str"), [Id("i")]), StringLiteral("e"))), BinaryOp("=", ArrayCell(Id("str"), [Id("i")]), StringLiteral("i"))), BinaryOp("=", ArrayCell(Id("str"), [Id("i")]), StringLiteral("o"))), BinaryOp("=", ArrayCell(Id("str"), [Id("i")]), StringLiteral("u"))), Block([Assign(Id("vowels"), BinaryOp("+", Id("vowels"), NumberLiteral(1.0)))]), [], None)])), Return(Id("vowels"))]))]))
        self.assertTrue(TestAST.test(input, expect, 344))

    
    def test_345(self):
        input = """func innerFunc() 
        func outerFunc() 
        begin
        writeString("Inside inner function")
        innerFunc()
        end
        """
        expect = str(Program([FuncDecl(Id("innerFunc"), [], None), FuncDecl(Id("outerFunc"), [], Block([CallStmt(Id("writeString"), [StringLiteral("Inside inner function")]), CallStmt(Id("innerFunc"), [])]))]))
        self.assertTrue(TestAST.test(input, expect, 345))

    
    def test_346(self):
        input = """func sumArray(number arr[], number size)
        begin
        if (size = 0) return 0
        else return arr[size - 1] + sumArray(arr, size - 1)
        end
        func main()
        begin
        number myArray[5] <- [1, 2, 3, 4, 5]
        var total <- sumArray(myArray, 5)
        end
        """
        expect = str(Program([FuncDecl(Id("sumArray"), [VarDecl(Id("arr"), ArrayType([], NumberType()), None, None), VarDecl(Id("size"), NumberType(), None, None)], Block([If(BinaryOp("=", Id("size"), NumberLiteral(0.0)), Return(NumberLiteral(0.0)), [], Return(BinaryOp("+", ArrayCell(Id("arr"), [BinaryOp("-", Id("size"), NumberLiteral(1.0))]), CallExpr(Id("sumArray"), [Id("arr"), BinaryOp("-", Id("size"), NumberLiteral(1.0))]))))])), FuncDecl(Id("main"), [], Block([VarDecl(Id("myArray"), ArrayType([5], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0), NumberLiteral(5.0)])), VarDecl(Id("total"), None, "var", CallExpr(Id("sumArray"), [Id("myArray"), NumberLiteral(5.0)]))]))]))
        self.assertTrue(TestAST.test(input, expect, 346))

    
    def test_347(self):
        input = """func main()
        begin
        var sentence <- ""
        for i until i < 5 by 1 begin
        sentence <- sentence ... "Number " ... i ... ", "
        end
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("sentence"), None, "var", StringLiteral("")), For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([Assign(Id("sentence"), BinaryOp("...", BinaryOp("...", BinaryOp("...", Id("sentence"), StringLiteral("Number ")), Id("i")), StringLiteral(", ")))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 347))

    
    def test_348(self):
        input = """func main()
        begin
        number matrix[2, 2] <- [[1, 2], [3, 4]]
        var element <- matrix[1,0]
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("matrix"), ArrayType([2, 2], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]), ArrayLiteral([NumberLiteral(3.0), NumberLiteral(4.0)])])), VarDecl(Id("element"), None, "var", ArrayCell(Id("matrix"), [NumberLiteral(1.0), NumberLiteral(0.0)]))]))]))
        self.assertTrue(TestAST.test(input, expect, 348))

    
    def test_349(self):
        input = """var y <- multiply(x, add(4, 5))
        """
        expect = str(Program([VarDecl(Id("y"), None, "var", CallExpr(Id("multiply"), [Id("x"), CallExpr(Id("add"), [NumberLiteral(4.0), NumberLiteral(5.0)])]))]))
        self.assertTrue(TestAST.test(input, expect, 349))

    
    def test_350(self):
        input = """func calculateExpression(number a, number b, number c) 
        begin
        return a * b + c / 2
        end
        """
        expect = str(Program([FuncDecl(Id("calculateExpression"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None), VarDecl(Id("c"), NumberType(), None, None)], Block([Return(BinaryOp("+", BinaryOp("*", Id("a"), Id("b")), BinaryOp("/", Id("c"), NumberLiteral(2.0))))]))]))
        self.assertTrue(TestAST.test(input, expect, 350))

    
    def test_351(self):
        input = """number matrix[3, 3] <- [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        var diagonalSum <- matrix[0,0] + matrix[1,1] + matrix[2,2]
        """
        expect = str(Program([VarDecl(Id("matrix"), ArrayType([3, 3], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)]), ArrayLiteral([NumberLiteral(7.0), NumberLiteral(8.0), NumberLiteral(9.0)])])), VarDecl(Id("diagonalSum"), None, "var", BinaryOp("+", BinaryOp("+", ArrayCell(Id("matrix"), [NumberLiteral(0.0), NumberLiteral(0.0)]), ArrayCell(Id("matrix"), [NumberLiteral(1.0), NumberLiteral(1.0)])), ArrayCell(Id("matrix"), [NumberLiteral(2.0), NumberLiteral(2.0)])))]))
        self.assertTrue(TestAST.test(input, expect, 351))

    
    def test_352(self):
        input = """var message <- "The value of x is: " ... 10
        """
        expect = str(Program([VarDecl(Id("message"), None, "var", BinaryOp("...", StringLiteral("The value of x is: "), NumberLiteral(10.0)))]))
        self.assertTrue(TestAST.test(input, expect, 352))

    
    def test_353(self):
        input = """func isPalindrome(string str) 
        begin
        var length <- strlength
        for i until i < length / 2 by 1 
        begin
        if (str[i] != str[length - i - 1]) return false
        end
        return true
        end
        """
        expect = str(Program([FuncDecl(Id("isPalindrome"), [VarDecl(Id("str"), StringType(), None, None)], Block([VarDecl(Id("length"), None, "var", Id("strlength")), For(Id("i"), BinaryOp("<", Id("i"), BinaryOp("/", Id("length"), NumberLiteral("2.0"))), NumberLiteral(1.0), Block([If(BinaryOp("!=", ArrayCell(Id("str"), [Id("i")]), ArrayCell(Id("str"), [BinaryOp("-", BinaryOp("-", Id("length"), Id("i")), NumberLiteral(1.0))])), Return(BooleanLiteral(True)), [], None)])), Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input, expect, 353))

    
    def test_354(self):
        input = """func greet(string name, string greeting) 
        begin
        printString(greeting ... " " ... name)
        end
        """
        expect = str(Program([FuncDecl(Id("greet"), [VarDecl(Id("name"), StringType(), None, None), VarDecl(Id("greeting"), StringType(), None, None)], Block([CallStmt(Id("printString"), [BinaryOp("...", BinaryOp("...", Id("greeting"), StringLiteral(" ")), Id("name"))])]))]))
        self.assertTrue(TestAST.test(input, expect, 354))

    
    def test_355(self):
        input = """var a <- funcwitharr([1,-2,3])
        """
        expect = str(Program([VarDecl(Id("a"), None, "var", CallExpr(Id("funcwitharr"), [ArrayLiteral([NumberLiteral(1.0), UnaryOp("-", NumberLiteral(2.0)), NumberLiteral(3.0)])]))]))
        self.assertTrue(TestAST.test(input, expect, 355))

    
    def test_356(self):
        input = """number data[] <- [10, 20, 30, 40, 50]
        """
        expect = str(Program([VarDecl(Id("data"), ArrayType(["<missing NUMLIT>"], NumberType()), None, ArrayLiteral([NumberLiteral(10.0), NumberLiteral(20.0), NumberLiteral(30.0), NumberLiteral(40.0), NumberLiteral(50.0)]))]))
        self.assertTrue(TestAST.test(input, expect, 356))

    
    def test_357(self):
        input = """func getFirstThreeChars(string str) return str[0] ... str[1] ... str[2]
        """
        expect = str(Program([FuncDecl(Id("getFirstThreeChars"), [VarDecl(Id("str"), StringType(), None, None)], Return(BinaryOp("...", BinaryOp("...", ArrayCell(Id("str"), [NumberLiteral(0.0)]), ArrayCell(Id("str"), [NumberLiteral(1.0)])), ArrayCell(Id("str"), [NumberLiteral(2.0)]))))]))
        self.assertTrue(TestAST.test(input, expect, 357))

    
    def test_358(self):
        input = """func bubbleSort(number arr[], number size) begin
        for i until i < size - 1 by 1 begin
        for j until j < size - i - 1 by 1 begin
        if (arr[j] > arr[j + 1]) begin
        var temp <- arr[j]
        arr[j] <- arr[j + 1]
        arr[j + 1] <- temp
        end
        end
        end
        end
        """
        expect = str(Program([FuncDecl(Id("bubbleSort"), [VarDecl(Id("arr"), ArrayType([], NumberType()), None, None), VarDecl(Id("size"), NumberType(), None, None)], Block([For(Id("i"), BinaryOp("<", Id("i"), BinaryOp("-", Id("size"), NumberLiteral(1.0))), NumberLiteral(1.0), Block([For(Id("j"), BinaryOp("<", Id("j"), BinaryOp("-", BinaryOp("-", Id("size"), Id("i")), NumberLiteral(1.0))), NumberLiteral(1.0), Block([If(BinaryOp(">", ArrayCell(Id("arr"), [Id("j")]), ArrayCell(Id("arr"), [BinaryOp("+", Id("j"), NumberLiteral(1.0))])), Block([VarDecl(Id("temp"), None, "var", ArrayCell(Id("arr"), [Id("j")])), Assign(ArrayCell(Id("arr"), [Id("j")]), ArrayCell(Id("arr"), [BinaryOp("+", Id("j"), NumberLiteral(1.0))])), Assign(ArrayCell(Id("arr"), [BinaryOp("+", Id("j"), NumberLiteral(1.0))]), Id("temp"))]), [], None)]))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 358))

    
    def test_359(self):
        input = """func calculateExpression(number x, number y) return (x + y) * (x - y) / (x * y)
        """
        expect = str(Program([FuncDecl(Id("calculateExpression"), [VarDecl(Id("x"), NumberType(), None, None), VarDecl(Id("y"), NumberType(), None, None)], Return(BinaryOp("/", BinaryOp("*", BinaryOp("+", Id("x"), Id("y")), BinaryOp("-", Id("x"), Id("y"))), BinaryOp("*", Id("x"), Id("y")))))]))
        self.assertTrue(TestAST.test(input, expect, 359))

    
    def test_360(self):
        input = """func calculate(number a, number b) 
        begin
        var result <- a + b
        if (result > 10) return "Greater"
        else return "Smaller or Equal"
        end
        """
        expect = str(Program([FuncDecl(Id("calculate"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Block([VarDecl(Id("result"), None, "var", BinaryOp("+", Id("a"), Id("b"))), If(BinaryOp(">", Id("result"), NumberLiteral(10.0)), Return(StringLiteral("Greater")), [], Return(StringLiteral("Smaller or Equal")))]))]))
        self.assertTrue(TestAST.test(input, expect, 360))

    
    def test_361(self):
        input = """var result <- isEven(8) and isEven(9)
        """
        expect = str(Program([VarDecl(Id("result"), None, "var", BinaryOp("and", CallExpr(Id("isEven"), [NumberLiteral(8.0)]), CallExpr(Id("isEven"), [NumberLiteral(9.0)])))]))
        self.assertTrue(TestAST.test(input, expect, 361))

    
    def test_362(self):
        input = """func emptyFunction() begin
        end
        """
        expect = str(Program([FuncDecl(Id("emptyFunction"), [], Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 362))

    
    def test_363(self):
        input = """func moreemptyFunction()
        """
        expect = str(Program([FuncDecl(Id("moreemptyFunction"), [], None)]))
        self.assertTrue(TestAST.test(input, expect, 363))

    
    def test_364(self):
        input = """number emptyarray[]
        """
        expect = str(Program([VarDecl(Id("emptyarray"), ArrayType(["<missing NUMLIT>"], NumberType()), None, None)]))
        self.assertTrue(TestAST.test(input, expect, 364))

    
    def test_365(self):
        input = """number moreemptyarray[] <- [[[[]]]]

        """
        expect = str(Program([VarDecl(Id("moreemptyarray"), ArrayType(["<missing NUMLIT>"], NumberType()), None, ArrayLiteral([ArrayLiteral([ArrayLiteral([None])])]))]))
        self.assertTrue(TestAST.test(input, expect, 365))

    
    def test_366(self):
        input = """var result <- true or false
        """
        expect = str(Program([VarDecl(Id("result"), None, "var", BinaryOp("or", BooleanLiteral(True), BooleanLiteral(True)))]))
        self.assertTrue(TestAST.test(input, expect, 366))

    
    def test_367(self):
        input = """func main()
        begin
        number values[3] <- [1, 2, 3]
        values[1] <- values[1] + 10
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("values"), ArrayType([3], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])), Assign(ArrayCell(Id("values"), [NumberLiteral(1.0)]), BinaryOp("+", ArrayCell(Id("values"), [NumberLiteral(1.0)]), NumberLiteral(10.0)))]))]))
        self.assertTrue(TestAST.test(input, expect, 367))

    
    def test_368(self):
        input = """func isLeapYear(number year)
        return (year % 4 = 0 and year % 100 != 0) or (year % 400 = 0)
        """
        expect = str(Program([FuncDecl(Id("isLeapYear"), [VarDecl(Id("year"), NumberType(), None, None)], Return(BinaryOp("or", BinaryOp("and", BinaryOp("=", BinaryOp("%", Id("year"), NumberLiteral(4.0)), NumberLiteral(0.0)), BinaryOp("!=", BinaryOp("%", Id("year"), NumberLiteral(100.0)), NumberLiteral(0.0))), BinaryOp("=", BinaryOp("%", Id("year"), NumberLiteral(400.0)), NumberLiteral(0.0)))))]))
        self.assertTrue(TestAST.test(input, expect, 368))

    
    def test_369(self):
        input = """number triangle[1,1] <- triangle[i - 1,j - 1] + triangle[i - 1,j]
        """
        expect = str(Program([VarDecl(Id("triangle"), ArrayType([1, 1], NumberType()), None, BinaryOp("+", ArrayCell(Id("triangle"), [BinaryOp("-", Id("i"), NumberLiteral(1.0)), BinaryOp("-", Id("j"), NumberLiteral(1.0))]), ArrayCell(Id("triangle"), [BinaryOp("-", Id("i"), NumberLiteral(1.0)), Id("j")])))]))
        self.assertTrue(TestAST.test(input, expect, 369))

    
    def test_370(self):
        input = """func calculateCircleArea(number radius) return 3.14 * radius * radius
        """
        expect = str(Program([FuncDecl(Id("calculateCircleArea"), [VarDecl(Id("radius"), NumberType(), None, None)], Return(BinaryOp("*", BinaryOp("*", NumberLiteral(3.14), Id("radius")), Id("radius"))))]))
        self.assertTrue(TestAST.test(input, expect, 370))

    
    def test_371(self):
        input = """func isPositive(number n) return n > 0
        """
        expect = str(Program([FuncDecl(Id("isPositive"), [VarDecl(Id("n"), NumberType(), None, None)], Return(BinaryOp(">", Id("n"), NumberLiteral(0.0))))]))
        self.assertTrue(TestAST.test(input, expect, 371))

    
    def test_372(self):
        input = """func isNegative(number n) return n < 0
        """
        expect = str(Program([FuncDecl(Id("isNegative"), [VarDecl(Id("n"), NumberType(), None, None)], Return(BinaryOp("<", Id("n"), NumberLiteral(0.0))))]))
        self.assertTrue(TestAST.test(input, expect, 372))

    
    def test_373(self):
        input = """func isZero(number n) return n = 0
        """
        expect = str(Program([FuncDecl(Id("isZero"), [VarDecl(Id("n"), NumberType(), None, None)], Return(BinaryOp("=", Id("n"), NumberLiteral(0.0))))]))
        self.assertTrue(TestAST.test(input, expect, 373))

    
    def test_374(self):
        input = """var haiku <- "Autumn leaves falling, \
        Nature's symphony whispers, \
        Serenity found."
        """
        expect = str(Program([VarDecl(Id("haiku"), None, "var", StringLiteral("Autumn leaves falling,         Nature's symphony whispers,         Serenity found."))]))
        self.assertTrue(TestAST.test(input, expect, 374))

    
    def test_375(self):
        input = """func isFridayThe13th() begin
        var today <- "2024-03-12" 
        return today = "2024-03-12"
        end
        """
        expect = str(Program([FuncDecl(Id("isFridayThe13th"), [], Block([VarDecl(Id("today"), None, "var", StringLiteral("2024-03-12")), Return(BinaryOp("=", Id("today"), StringLiteral("2024-03-12")))]))]))
        self.assertTrue(TestAST.test(input, expect, 375))

    
    def test_376(self):
        input = """func flipCoin() 
        begin
        var result <- ["Heads", "Tails"]
        return result[rand(0, 1)]
        end
        """
        expect = str(Program([FuncDecl(Id("flipCoin"), [], Block([VarDecl(Id("result"), None, "var", ArrayLiteral([StringLiteral("Heads"), StringLiteral("Tails")])), Return(ArrayCell(Id("result"), [CallExpr(Id("rand"), [NumberLiteral(0.0), NumberLiteral(1.0)])]))]))]))
        self.assertTrue(TestAST.test(input, expect, 376))

    
    def test_377(self):
        input = """var coffeeShopNames <- ["Phuc Long", "Cong Caphe", "Highlands Coffee", "Trung Nguyen"]
        var randomCoffeeShop <- coffeeShopNames[rand(0, len(coffeeShopNames) - 1)]
        """
        expect = str(Program([VarDecl(Id("coffeeShopNames"), None, "var", ArrayLiteral([StringLiteral("Phuc Long"), StringLiteral("Cong Caphe"), StringLiteral("Highlands Coffee"), StringLiteral("Trung Nguyen")])), VarDecl(Id("randomCoffeeShop"), None, "var", ArrayCell(Id("coffeeShopNames"), [CallExpr(Id("rand"), [NumberLiteral(0.0), BinaryOp("-", CallExpr(Id("len"), [Id("coffeeShopNames")]), NumberLiteral(1.0))])]))]))
        self.assertTrue(TestAST.test(input, expect, 377))

    
    def test_378(self):
        input = """ var dishes <- ["Pho", "Banh Xeo", "Bun Cha", "Goi Cuon"]
        var randomDish <- dishes[rand(0, len(dishes) - 1)]
        """
        expect = str(Program([VarDecl(Id("dishes"), None, "var", ArrayLiteral([StringLiteral("Pho"), StringLiteral("Banh Xeo"), StringLiteral("Bun Cha"), StringLiteral("Goi Cuon")])), VarDecl(Id("randomDish"), None, "var", ArrayCell(Id("dishes"), [CallExpr(Id("rand"), [NumberLiteral(0.0), BinaryOp("-", CallExpr(Id("len"), [Id("dishes")]), NumberLiteral(1.0))])]))]))
        self.assertTrue(TestAST.test(input, expect, 378))

    
    def test_379(self):
        input = """var a <- funcwith2arr([1,2,3],[4,5,6])
        """
        expect = str(Program([VarDecl(Id("a"), None, "var", CallExpr(Id("funcwith2arr"), [ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])]))]))
        self.assertTrue(TestAST.test(input, expect, 379))

    
    def test_380(self):
        input = """var result <- (5 * (10 + 2)) / (3 - 1)
        """
        expect = str(Program([VarDecl(Id("result"), None, "var", BinaryOp("/", BinaryOp("*", NumberLiteral(5.0), BinaryOp("+", NumberLiteral(10.0), NumberLiteral(2.0))), BinaryOp("-", NumberLiteral(3.0), NumberLiteral(1.0))))]))
        self.assertTrue(TestAST.test(input, expect, 380))

    
    def test_381(self):
        input = """func findPrime(number n) 
        begin
        var prime <- true
        for i until i < n by 1 begin
        if (n % i == 0) 
        begin
        prime <- false
        break
        end
        end
        return prime
        end
        """
        expect = str(Program([FuncDecl(Id("findPrime"), [VarDecl(Id("n"), NumberType(), None, None)], Block([VarDecl(Id("prime"), None, "var", BooleanLiteral(True)), For(Id("i"), BinaryOp("<", Id("i"), Id("n")), NumberLiteral(1.0), Block([If(BinaryOp("==", BinaryOp("%", Id("n"), Id("i")), NumberLiteral(0.0)), Block([Assign(Id("prime"), BooleanLiteral(True)), Break()]), [], None)])), Return(Id("prime"))]))]))
        self.assertTrue(TestAST.test(input, expect, 381))

    
    def test_382(self):
        input = """var fullName <- firstName ... " " ... lastName ... " is " ... (currentYear - birthYear) ... " years old."
        """
        expect = str(Program([VarDecl(Id("fullName"), None, "var", BinaryOp("...", BinaryOp("...", BinaryOp("...", BinaryOp("...", BinaryOp("...", Id("firstName"), StringLiteral(" ")), Id("lastName")), StringLiteral(" is ")), BinaryOp("-", Id("currentYear"), Id("birthYear"))), StringLiteral(" years old.")))]))
        self.assertTrue(TestAST.test(input, expect, 382))

    
    def test_383(self):
        input = """var result <- (factorial(5) + fibonacci(8)) / sumArray([1, 2, 3, 4, 5])
        """
        expect = str(Program([VarDecl(Id("result"), None, "var", BinaryOp("/", BinaryOp("+", CallExpr(Id("factorial"), [NumberLiteral(5.0)]), CallExpr(Id("fibonacci"), [NumberLiteral(8.0)])), CallExpr(Id("sumArray"), [ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0), NumberLiteral(5.0)])])))]))
        self.assertTrue(TestAST.test(input, expect, 383))

    
    def test_384(self):
        input = """dynamic abc
        """
        expect = str(Program([VarDecl(Id("abc"), None, "dynamic", None)]))
        self.assertTrue(TestAST.test(input, expect, 384))

    
    def test_385(self):
        input = """func main()
        begin
        if ((x > 0) and (y < 10)) print("Both x is positive and y is less than 10")
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(BinaryOp("and", BinaryOp(">", Id("x"), NumberLiteral(0.0)), BinaryOp("<", Id("y"), NumberLiteral(10.0))), CallStmt(Id("print"), [StringLiteral("Both x is positive and y is less than 10")]), [], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 385))

    
    def test_386(self):
        input = """var isValid <- checkInput((x > 0) and (y < 10))
        """
        expect = str(Program([VarDecl(Id("isValid"), None, "var", CallExpr(Id("checkInput"), [BinaryOp("and", BinaryOp(">", Id("x"), NumberLiteral(0.0)), BinaryOp("<", Id("y"), NumberLiteral(10.0)))]))]))
        self.assertTrue(TestAST.test(input, expect, 386))

    
    def test_387(self):
        input = """func main()
        begin
        if (array[i] != 0) print("Array element at index i is non-zero")
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(BinaryOp("!=", ArrayCell(Id("array"), [Id("i")]), NumberLiteral(0.0)), CallStmt(Id("print"), [StringLiteral("Array element at index i is non-zero")]), [], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 387))

    
    def test_388(self):
        input = """func main()
        begin
        if ((x > 0) and ((y < 10) or ((z >= 5) and not ((a == 0) or (b != 3)))))
        print("Complex nested logical expression with multiple operators")
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(BinaryOp("and", BinaryOp(">", Id("x"), NumberLiteral(0.0)), BinaryOp("or", BinaryOp("<", Id("y"), NumberLiteral(10.0)), BinaryOp("and", BinaryOp(">=", Id("z"), NumberLiteral(5.0)), UnaryOp("not", BinaryOp("or", BinaryOp("==", Id("a"), NumberLiteral(0.0)), BinaryOp("!=", Id("b"), NumberLiteral(3.0))))))), CallStmt(Id("print"), [StringLiteral("Complex nested logical expression with multiple operators")]), [], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 388))

    
    def test_389(self):
        input = """func main()
        begin
        if (x > 0) print("x is positive") 
        if ((y > 0) and (z > 0)) print("Both y and z are positive")
        elif (y < 0) and (z < 0) print("Both y and z are negative")
        else print("One of y or z is non-positive")
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(BinaryOp(">", Id("x"), NumberLiteral(0.0)), CallStmt(Id("print"), [StringLiteral("x is positive")]), [], None), If(BinaryOp("and", BinaryOp(">", Id("y"), NumberLiteral(0.0)), BinaryOp(">", Id("z"), NumberLiteral(0.0))), CallStmt(Id("print"), [StringLiteral("Both y and z are positive")]), [(BinaryOp("and", BinaryOp("<", Id("y"), NumberLiteral(0.0)), BinaryOp("<", Id("z"), NumberLiteral(0.0))), CallStmt(Id("print"), [StringLiteral("Both y and z are negative")]))], CallStmt(Id("print"), [StringLiteral("One of y or z is non-positive")]))]))]))
        self.assertTrue(TestAST.test(input, expect, 389))

    
    def test_390(self):
        input = """dynamic dynamicVar
        """
        expect = str(Program([VarDecl(Id("dynamicVar"), None, "dynamic", None)]))
        self.assertTrue(TestAST.test(input, expect, 390))

    
    def test_391(self):
        input = """var nestedResult <- (a + (b * (c - d))) / e
        """
        expect = str(Program([VarDecl(Id("nestedResult"), None, "var", BinaryOp("/", BinaryOp("+", Id("a"), BinaryOp("*", Id("b"), BinaryOp("-", Id("c"), Id("d")))), Id("e")))]))
        self.assertTrue(TestAST.test(input, expect, 391))

    
    def test_392(self):
        input = """number complexNum <- 1.2e-3 + 5.6e2
        """
        expect = str(Program([VarDecl(Id("complexNum"), NumberType(), None, BinaryOp("+", NumberLiteral(0.0012), NumberLiteral(560.0)))]))
        self.assertTrue(TestAST.test(input, expect, 392))

    
    def test_393(self):
        input = """string complexString <- "This string includes HTML markup like <b>bold</b> and <i>italic</i>."
        """
        expect = str(Program([VarDecl(Id("complexString"), StringType(), None, StringLiteral("This string includes HTML markup like <b>bold</b> and <i>italic</i>."))]))
        self.assertTrue(TestAST.test(input, expect, 393))

    
    def test_394(self):
        input = """string complexString <- "He said, '"Hello world'""
        """
        expect = str(Program([VarDecl(Id("complexString"), StringType(), None, StringLiteral("He said, '\"Hello world'\""))]))
        self.assertTrue(TestAST.test(input, expect, 394))

    
    def test_395(self):
        input = """string name_with_
        """
        expect = str(Program([VarDecl(Id("name_with_"), StringType(), None, None)]))
        self.assertTrue(TestAST.test(input, expect, 395))

    
    def test_396(self):
        input = """func function()
        ## TO DO
        """
        expect = str(Program([FuncDecl(Id("function"), [], None)]))
        self.assertTrue(TestAST.test(input, expect, 396))

    
    def test_397(self):
        input = """func main()
        return
        """
        expect = str(Program([FuncDecl(Id("main"), [], Return())]))
        self.assertTrue(TestAST.test(input, expect, 397))

    
    def test_398(self):
        input = """##Test case:
        func one_more_test_case()
        begin
        ##Last Test Case Below
        return ##Finally
        end
        """
        expect = str(Program([FuncDecl(Id("one_more_test_case"), [], Block([Return()]))]))
        self.assertTrue(TestAST.test(input, expect, 398))

    
    def test_399(self):
        input = """func thank_you_for_checking_it_out()
        return "^______^"
        """
        expect = str(Program([FuncDecl(Id("thank_you_for_checking_it_out"), [], Return(StringLiteral("^______^")))]))
        self.assertTrue(TestAST.test(input, expect, 399))

    
        
    