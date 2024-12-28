grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: NL* declaration NL* EOF;

declaration: declare declaretail;

declaretail: declare declaretail |;

declare: var_declare | func_declare;

//VARIABLE DECLARATION

var_declare: 
	(normaldeclare
|	arraydeclare
|	vartypedeclare);
	/*((var_type single_dec)
|	('var' var_dec)
|	('dynamic' dyn_dec)) NL+;*/
normaldeclare: (var_type | DYNTYPE) IDENTIFIER initialnormal NL+;
//single_dec: IDENTIFIER array_initial;

var_type: NUMBER_TYPE | BOOL_TYPE | STR_TYPE ;

initialnormal: assignmentexpr | ;

assignmentexpr: ASSIGN expr;

arraydeclare: var_type IDENTIFIER array initialarray NL+;
//array_initial: array initial; 
array: LP dimension RP;
//array: array_ini | ;
dimension: NUMLIT dimtail;
//array_ini: LP dimension RP;
dimtail: (CM NUMLIT dimtail) | ;
//dimension: dim_length CM dimension | dim_length;
initialarray: ASSIGN expr |;
//dim_length: NUM1;
vartypedeclare: VARTYPE IDENTIFIER assignmentexpr NL+;
//initial: init | ;

//init: ASSIGN (expr | NUM1 | NUM2 | NUM3 | NUM4);

//FUNCTION DECLARATION

func_declare: FUNCTYPE IDENTIFIER parameters NL* (body|NL+);

parameters: LB param_here RB;

param_here: param_list | ;

param_list: para paratail;
//param_list: var_type single_dec CM param_list | var_type single_dec;
paratail: (CM para paratail) | ;

para: var_type IDENTIFIER isarrayindex;

isarrayindex: arrayindex | ;

arrayindex: 
	LP expr RP
|	LP RP;

//index: NUM1 | ;

body: return_stm| block|;

//STATEMENT

statement: 
	var_declare 
|	assignment
|	ifstm
|	forstm
|	break_stm
|	continue_stm
|	return_stm
|	func_call_stm
|	block ;

//Assignement Statement
assignment: lhs ASSIGN expr NL+;

//If Statement
ifstm: 
	IFOP LB expr RB NL* ifstm
|	IFOP LB expr RB NL* statement NL* (elifbranch)* elsebranch?;
elifbranch: 
	ELIFOP expr NL* ifstm
|	ELIFOP expr NL* statement NL*;
elsebranch: ELSEOP NL* statement NL*;

//For Statement
forstm: FOROP IDENTIFIER UNTILOP expr BYOP update NL* statement NL*;
update: SUBTR? literals;

//Break Statement
break_stm: BREAKOP NL+;

//Continue Statement
continue_stm: CONTOP NL+;

//Return Statement
return_stm: RETURNOP (expr)? NL+;

//Block Statement
block: BEGINOP NL+ (statement)* ENDOP NL+;

func_call_stm: IDENTIFIER LB arguments RB NL+;


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
| 	expr4;

expr4: 
	expr4 (MULOP | DIVOP | MODOP) expr5 
| 	expr5;

expr5: 
	<assoc=right> NOTOP expr6 
| 	expr6;

expr6: 
	<assoc=right> SUBTR expr7 
| 	expr7;


expr7: 
	IDENTIFIER LB arguments RB
|	IDENTIFIER LP expr8 RP 
| 	expr9;

arguments: arg argtail;

arg: expr |;

argtail: CM arg argtail
|;

expr8:
 	expr CM expr8
|	expr;


expr9: operand;

operand: literals | LB expr RB;

lhs: 
	IDENTIFIER
| 	IDENTIFIER LB arguments RB
| 	IDENTIFIER LP expr8 RP;

literals:
	arraylit
|	IDENTIFIER
|	SUBTR? NUMLIT
|	STRINGLIT
|	BOOLIT;

arraylit:
	LP literals arraylittail RP;

numlittail: CM SUBTR? NUMLIT numlittail 
| ;

stringlittail: CM STRINGLIT stringlittail 
| ;

boolittail: CM BOOLIT boolittail 
| ;

arraylittail: CM literals arraylittail 
| ;




//TYPE and VALUE

BOOL_TYPE: 'bool';
NUMBER_TYPE: 'number';
STR_TYPE: 'string';
DYNTYPE: 'dynamic';
VARTYPE: 'var';
FUNCTYPE: 'func';

//LEXICAL STRUCTRUE

//3.3. Identifiers:



//3.4. Keywords:

//3.5. Operators:

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
RELATION: '=' | '==' | '!=' | '<' | '>' | '<=' | '>=';



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