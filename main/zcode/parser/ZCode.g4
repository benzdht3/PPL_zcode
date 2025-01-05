grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: NL* declaration+ NL* EOF;

declaration: (var_declare | func_declare) NL+;

//VARIABLE DECLARATION

var_declare:
	normaldeclare
|	arraydeclare
|	vartypedeclare;

normaldeclare: (var_type | DYNTYPE) IDENTIFIER initialnormal ;

var_type: NUMBER_TYPE | BOOL_TYPE | STR_TYPE ;

initialnormal: ASSIGN expr | ;

arraydeclare: var_type IDENTIFIER array initialarray ;

array: LP dimension RP;

dimension: NUMLIT dimtail;

dimtail: (CM NUMLIT dimtail) | ;

initialarray: ASSIGN expr | ;

arraylit:
	LP literals arraylittail RP
|	LP RP;

arraylittail: CM literals arraylittail
| ;

literals:
	arraylit
|	IDENTIFIER
|	SUBTR? NUMLIT
|	STRINGLIT
|	BOOLIT;

vartypedeclare: VARTYPE IDENTIFIER ASSIGN expr ;

//FUNCTION DECLARATION

func_declare: FUNCTYPE IDENTIFIER LB param_here RB NL* bodyhere;

param_here: param_list | ;

param_list: para paratail;

paratail: (CM para paratail) | ;

para: var_type (IDENTIFIER | IDENTIFIER array);

bodyhere: body | ;

body: return_stm | block ;

//STATEMENT

statement:
	ifstm
|	forstm
|	((var_declare
|	assignment
|	break_stm
|	continue_stm
|	return_stm
|	func_call_stm
|	block) NL+) ;

//Assignement Statement
assignment: lhs ASSIGN expr;

lhs:
  IDENTIFIER
| arrayindex ;

arrayindex: arr_expr LP cell RP ;

arr_expr: IDENTIFIER | func_call_expr ;

cell: expr exprtail;

exprtail:
	CM expr exprtail
| ;

//If Statement
ifstm: IFOP LB expr RB NL* statement elif_here else_here ;

elif_here: elifbranch | ;

else_here: elsebranch | ;

elifbranch: ELIFOP LB expr RB NL* statement eliftail ;

eliftail: elifbranch | ;

elsebranch: ELSEOP NL* statement;

//For Statement
forstm: FOROP IDENTIFIER UNTILOP cond_expr BYOP update_expr NL* statement;

cond_expr: expr;

update_expr: expr;

//Break Statement
break_stm: BREAKOP ;

//Continue Statement
continue_stm: CONTOP ;

//Return Statement
return_stm: RETURNOP expr? ;

//Function call statement
func_call_stm: IDENTIFIER LB argumentlist RB;

argumentlist: arguments | ;

arguments: expr argtail ;

argtail:
  CM expr argtail
| ;

//Block Statement
block: BEGINOP NL+ (statement)* ENDOP;

//EXPRESSIONS
expr:
	expr CONCAT expr1
|	expr1;

expr1:
	expr1 ANDOR expr2
|	expr2;

expr2:
	expr2 RELATION expr3
|	expr3;

expr3:
	expr3 (ADDOP | SUBTR) expr4
| expr4;

expr4:
	expr4 (MULOP | DIVOP | MODOP) expr5
| expr5;

expr5:
	<assoc=right> NOTOP expr6
| 	expr6;

expr6:
	<assoc=right> SUBTR expr7
| expr7;

expr7: arrayindex |	func_call_expr | operand;

func_call_expr: IDENTIFIER LB argumentlist RB ;

operand:
	literals
| LB expr RB;

//LEXICAL STRUCTRUE

IFOP: 'if';
ELIFOP: 'elif';
ELSEOP: 'else';
FOROP: 'for';
UNTILOP: 'until';
BYOP: 'by';
BREAKOP: 'break';
CONTOP: 'continue';
RETURNOP: 'return';
BEGINOP: 'begin';
ENDOP: 'end';

//TYPE and VALUE

BOOL_TYPE: 'bool';
NUMBER_TYPE: 'number';
STR_TYPE: 'string';
DYNTYPE: 'dynamic';
VARTYPE: 'var';
FUNCTYPE: 'func';

//Logical
NOTOP: 'not';
ANDOR: 'and' | 'or';

//Arithmetic
ADDOP: '+';
SUBTR: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';

//String
CONCAT: '...';

//RELATIONAL
ASSIGN: '<-';
RELATION: '==' | '>=' | '<=' | '>' | '<' | '!=' | '=' ;



//3.6. Seperators:

CM: ',';
LP: '[';
RP: ']';
LB: '(';
RB: ')';

//3.7. Literals:

NUMLIT: NUM1 | NUM2 | NUM3 | NUM4;

NUM1: [0-9]+;

NUM2: [0-9]+ '.'? [0-9]*;

NUM3: [0-9]+ [eE] [-+]? [0-9]+;

NUM4: [0-9]+ '.' [0-9]+ [eE] [-+]? [0-9]+;


BOOLIT: 'true' | 'false';

STRINGLIT: '"' (~[\r\n"] | [\b\f\t'\\] | ('\'' '"'))* '"' {
			txt = self.text[1:-1]
			pos = 0
			l = len(txt)
			while pos < l:
				while pos < l and txt[pos] != '\\':
					pos += 1
				pos += 1
				if pos < l:
					escap = txt[pos]
					if escap != 'b' and escap != 't' and escap != 'f' and escap != '\'' and escap != 'n' and escap != 'r' and escap != '\\' and escap != ' ':
						raise IllegalEscape(txt[:pos+1])
					else:
						pos += 1
				else:
					self.text=txt
			self.text=txt
		};


IDENTIFIER: [a-zA-Z_] [a-zA-Z_0-9]*;

COMMENT: ('##' (~[\n])*) -> skip;

WS : [ \t\b\f]+ -> skip ;

NL: '\n' | '\r\n' | '\r';


ERROR_CHAR: .{raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' ([#-~ !]| [\b\f\t] | ('\'' '"'))* {raise UncloseString(self.text[1:])};

ILLEGAL_ESCAPE: . {raise IllegalEscape(self.text)};
