# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\u0255\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\7")
        buf.write("\2v\n\2\f\2\16\2y\13\2\3\2\3\2\7\2}\n\2\f\2\16\2\u0080")
        buf.write("\13\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u008b\n")
        buf.write("\4\3\5\3\5\5\5\u008f\n\5\3\6\3\6\3\6\5\6\u0094\n\6\3\7")
        buf.write("\3\7\5\7\u0098\n\7\3\7\3\7\3\7\6\7\u009d\n\7\r\7\16\7")
        buf.write("\u009e\3\b\3\b\3\t\3\t\5\t\u00a5\n\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\6\13\u00af\n\13\r\13\16\13\u00b0")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00be\n\16\3\17\3\17\3\17\5\17\u00c3\n\17\3\20\3\20\3")
        buf.write("\20\3\20\6\20\u00c9\n\20\r\20\16\20\u00ca\3\21\3\21\3")
        buf.write("\21\3\21\7\21\u00d1\n\21\f\21\16\21\u00d4\13\21\3\21\3")
        buf.write("\21\6\21\u00d8\n\21\r\21\16\21\u00d9\5\21\u00dc\n\21\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\5\23\u00e4\n\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u00ee\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\27\3\27\5\27\u00f6\n\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\5\30\u00fe\n\30\3\31\3\31\3\31\5\31\u0103")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32")
        buf.write("\u010e\n\32\3\33\3\33\3\33\3\33\6\33\u0114\n\33\r\33\16")
        buf.write("\33\u0115\3\34\3\34\3\34\3\34\3\34\7\34\u011d\n\34\f\34")
        buf.write("\16\34\u0120\13\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\7\34\u0129\n\34\f\34\16\34\u012c\13\34\3\34\3\34\7\34")
        buf.write("\u0130\n\34\f\34\16\34\u0133\13\34\3\34\7\34\u0136\n\34")
        buf.write("\f\34\16\34\u0139\13\34\3\34\5\34\u013c\n\34\5\34\u013e")
        buf.write("\n\34\3\35\3\35\3\35\7\35\u0143\n\35\f\35\16\35\u0146")
        buf.write("\13\35\3\35\3\35\3\35\3\35\3\35\7\35\u014d\n\35\f\35\16")
        buf.write("\35\u0150\13\35\3\35\3\35\7\35\u0154\n\35\f\35\16\35\u0157")
        buf.write("\13\35\5\35\u0159\n\35\3\36\3\36\7\36\u015d\n\36\f\36")
        buf.write("\16\36\u0160\13\36\3\36\3\36\7\36\u0164\n\36\f\36\16\36")
        buf.write("\u0167\13\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0170")
        buf.write("\n\37\f\37\16\37\u0173\13\37\3\37\3\37\7\37\u0177\n\37")
        buf.write("\f\37\16\37\u017a\13\37\3 \5 \u017d\n \3 \3 \3!\3!\6!")
        buf.write("\u0183\n!\r!\16!\u0184\3\"\3\"\6\"\u0189\n\"\r\"\16\"")
        buf.write("\u018a\3#\3#\5#\u018f\n#\3#\6#\u0192\n#\r#\16#\u0193\3")
        buf.write("$\3$\6$\u0198\n$\r$\16$\u0199\3$\7$\u019d\n$\f$\16$\u01a0")
        buf.write("\13$\3$\3$\6$\u01a4\n$\r$\16$\u01a5\3%\3%\3%\3%\3%\6%")
        buf.write("\u01ad\n%\r%\16%\u01ae\3&\3&\3&\3&\3&\3&\7&\u01b7\n&\f")
        buf.write("&\16&\u01ba\13&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u01c2\n\'")
        buf.write("\f\'\16\'\u01c5\13\'\3(\3(\3(\3(\3(\3(\7(\u01cd\n(\f(")
        buf.write("\16(\u01d0\13(\3)\3)\3)\3)\3)\3)\7)\u01d8\n)\f)\16)\u01db")
        buf.write("\13)\3*\3*\3*\3*\3*\3*\7*\u01e3\n*\f*\16*\u01e6\13*\3")
        buf.write("+\3+\3+\5+\u01eb\n+\3,\3,\3,\5,\u01f0\n,\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\5-\u01fd\n-\3.\3.\3.\3/\3/\5/\u0204")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\5\60\u020b\n\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\5\61\u0212\n\61\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\63\3\63\5\63\u021b\n\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u0228\n\64\3\65\3")
        buf.write("\65\3\65\5\65\u022d\n\65\3\65\3\65\3\65\5\65\u0232\n\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\67\3\67\5\67\u023b\n\67\3")
        buf.write("\67\3\67\3\67\5\67\u0240\n\67\38\38\38\38\58\u0246\n8")
        buf.write("\39\39\39\39\59\u024c\n9\3:\3:\3:\3:\3:\5:\u0253\n:\3")
        buf.write(":\2\7JLNPR;\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnpr\2\5")
        buf.write("\3\2\16\20\3\2\26\27\3\2\30\32\2\u026a\2w\3\2\2\2\4\u0083")
        buf.write("\3\2\2\2\6\u008a\3\2\2\2\b\u008e\3\2\2\2\n\u0093\3\2\2")
        buf.write("\2\f\u0097\3\2\2\2\16\u00a0\3\2\2\2\20\u00a4\3\2\2\2\22")
        buf.write("\u00a6\3\2\2\2\24\u00a9\3\2\2\2\26\u00b2\3\2\2\2\30\u00b6")
        buf.write("\3\2\2\2\32\u00bd\3\2\2\2\34\u00c2\3\2\2\2\36\u00c4\3")
        buf.write("\2\2\2 \u00cc\3\2\2\2\"\u00dd\3\2\2\2$\u00e3\3\2\2\2&")
        buf.write("\u00e5\3\2\2\2(\u00ed\3\2\2\2*\u00ef\3\2\2\2,\u00f5\3")
        buf.write("\2\2\2.\u00fd\3\2\2\2\60\u0102\3\2\2\2\62\u010d\3\2\2")
        buf.write("\2\64\u010f\3\2\2\2\66\u013d\3\2\2\28\u0158\3\2\2\2:\u015a")
        buf.write("\3\2\2\2<\u0168\3\2\2\2>\u017c\3\2\2\2@\u0180\3\2\2\2")
        buf.write("B\u0186\3\2\2\2D\u018c\3\2\2\2F\u0195\3\2\2\2H\u01a7\3")
        buf.write("\2\2\2J\u01b0\3\2\2\2L\u01bb\3\2\2\2N\u01c6\3\2\2\2P\u01d1")
        buf.write("\3\2\2\2R\u01dc\3\2\2\2T\u01ea\3\2\2\2V\u01ef\3\2\2\2")
        buf.write("X\u01fc\3\2\2\2Z\u01fe\3\2\2\2\\\u0203\3\2\2\2^\u020a")
        buf.write("\3\2\2\2`\u0211\3\2\2\2b\u0213\3\2\2\2d\u021a\3\2\2\2")
        buf.write("f\u0227\3\2\2\2h\u0231\3\2\2\2j\u0233\3\2\2\2l\u023f\3")
        buf.write("\2\2\2n\u0245\3\2\2\2p\u024b\3\2\2\2r\u0252\3\2\2\2tv")
        buf.write("\7-\2\2ut\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2xz\3\2")
        buf.write("\2\2yw\3\2\2\2z~\5\4\3\2{}\7-\2\2|{\3\2\2\2}\u0080\3\2")
        buf.write("\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0081\3\2\2\2\u0080~\3")
        buf.write("\2\2\2\u0081\u0082\7\2\2\3\u0082\3\3\2\2\2\u0083\u0084")
        buf.write("\5\b\5\2\u0084\u0085\5\6\4\2\u0085\5\3\2\2\2\u0086\u0087")
        buf.write("\5\b\5\2\u0087\u0088\5\6\4\2\u0088\u008b\3\2\2\2\u0089")
        buf.write("\u008b\3\2\2\2\u008a\u0086\3\2\2\2\u008a\u0089\3\2\2\2")
        buf.write("\u008b\7\3\2\2\2\u008c\u008f\5\n\6\2\u008d\u008f\5 \21")
        buf.write("\2\u008e\u008c\3\2\2\2\u008e\u008d\3\2\2\2\u008f\t\3\2")
        buf.write("\2\2\u0090\u0094\5\f\7\2\u0091\u0094\5\24\13\2\u0092\u0094")
        buf.write("\5\36\20\2\u0093\u0090\3\2\2\2\u0093\u0091\3\2\2\2\u0093")
        buf.write("\u0092\3\2\2\2\u0094\13\3\2\2\2\u0095\u0098\5\16\b\2\u0096")
        buf.write("\u0098\7\21\2\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2")
        buf.write("\2\u0098\u0099\3\2\2\2\u0099\u009a\7*\2\2\u009a\u009c")
        buf.write("\5\20\t\2\u009b\u009d\7-\2\2\u009c\u009b\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\r\3\2\2\2\u00a0\u00a1\t\2\2\2\u00a1\17\3\2\2\2")
        buf.write("\u00a2\u00a5\5\22\n\2\u00a3\u00a5\3\2\2\2\u00a4\u00a2")
        buf.write("\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\21\3\2\2\2\u00a6\u00a7")
        buf.write("\7\34\2\2\u00a7\u00a8\5J&\2\u00a8\23\3\2\2\2\u00a9\u00aa")
        buf.write("\5\16\b\2\u00aa\u00ab\7*\2\2\u00ab\u00ac\5\26\f\2\u00ac")
        buf.write("\u00ae\5\34\17\2\u00ad\u00af\7-\2\2\u00ae\u00ad\3\2\2")
        buf.write("\2\u00af\u00b0\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1")
        buf.write("\3\2\2\2\u00b1\25\3\2\2\2\u00b2\u00b3\7\37\2\2\u00b3\u00b4")
        buf.write("\5\30\r\2\u00b4\u00b5\7 \2\2\u00b5\27\3\2\2\2\u00b6\u00b7")
        buf.write("\7#\2\2\u00b7\u00b8\5\32\16\2\u00b8\31\3\2\2\2\u00b9\u00ba")
        buf.write("\7\36\2\2\u00ba\u00bb\7#\2\2\u00bb\u00be\5\32\16\2\u00bc")
        buf.write("\u00be\3\2\2\2\u00bd\u00b9\3\2\2\2\u00bd\u00bc\3\2\2\2")
        buf.write("\u00be\33\3\2\2\2\u00bf\u00c0\7\34\2\2\u00c0\u00c3\5J")
        buf.write("&\2\u00c1\u00c3\3\2\2\2\u00c2\u00bf\3\2\2\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c3\35\3\2\2\2\u00c4\u00c5\7\22\2\2\u00c5\u00c6")
        buf.write("\7*\2\2\u00c6\u00c8\5\22\n\2\u00c7\u00c9\7-\2\2\u00c8")
        buf.write("\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00c8\3\2\2\2")
        buf.write("\u00ca\u00cb\3\2\2\2\u00cb\37\3\2\2\2\u00cc\u00cd\7\23")
        buf.write("\2\2\u00cd\u00ce\7*\2\2\u00ce\u00d2\5\"\22\2\u00cf\u00d1")
        buf.write("\7-\2\2\u00d0\u00cf\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00db\3\2\2\2")
        buf.write("\u00d4\u00d2\3\2\2\2\u00d5\u00dc\5\60\31\2\u00d6\u00d8")
        buf.write("\7-\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dc\3\2\2\2")
        buf.write("\u00db\u00d5\3\2\2\2\u00db\u00d7\3\2\2\2\u00dc!\3\2\2")
        buf.write("\2\u00dd\u00de\7!\2\2\u00de\u00df\5$\23\2\u00df\u00e0")
        buf.write("\7\"\2\2\u00e0#\3\2\2\2\u00e1\u00e4\5&\24\2\u00e2\u00e4")
        buf.write("\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4")
        buf.write("%\3\2\2\2\u00e5\u00e6\5*\26\2\u00e6\u00e7\5(\25\2\u00e7")
        buf.write("\'\3\2\2\2\u00e8\u00e9\7\36\2\2\u00e9\u00ea\5*\26\2\u00ea")
        buf.write("\u00eb\5(\25\2\u00eb\u00ee\3\2\2\2\u00ec\u00ee\3\2\2\2")
        buf.write("\u00ed\u00e8\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee)\3\2\2")
        buf.write("\2\u00ef\u00f0\5\16\b\2\u00f0\u00f1\7*\2\2\u00f1\u00f2")
        buf.write("\5,\27\2\u00f2+\3\2\2\2\u00f3\u00f6\5.\30\2\u00f4\u00f6")
        buf.write("\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6")
        buf.write("-\3\2\2\2\u00f7\u00f8\7\37\2\2\u00f8\u00f9\5J&\2\u00f9")
        buf.write("\u00fa\7 \2\2\u00fa\u00fe\3\2\2\2\u00fb\u00fc\7\37\2\2")
        buf.write("\u00fc\u00fe\7 \2\2\u00fd\u00f7\3\2\2\2\u00fd\u00fb\3")
        buf.write("\2\2\2\u00fe/\3\2\2\2\u00ff\u0103\5D#\2\u0100\u0103\5")
        buf.write("F$\2\u0101\u0103\3\2\2\2\u0102\u00ff\3\2\2\2\u0102\u0100")
        buf.write("\3\2\2\2\u0102\u0101\3\2\2\2\u0103\61\3\2\2\2\u0104\u010e")
        buf.write("\5\n\6\2\u0105\u010e\5\64\33\2\u0106\u010e\5\66\34\2\u0107")
        buf.write("\u010e\5<\37\2\u0108\u010e\5@!\2\u0109\u010e\5B\"\2\u010a")
        buf.write("\u010e\5D#\2\u010b\u010e\5H%\2\u010c\u010e\5F$\2\u010d")
        buf.write("\u0104\3\2\2\2\u010d\u0105\3\2\2\2\u010d\u0106\3\2\2\2")
        buf.write("\u010d\u0107\3\2\2\2\u010d\u0108\3\2\2\2\u010d\u0109\3")
        buf.write("\2\2\2\u010d\u010a\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010c")
        buf.write("\3\2\2\2\u010e\63\3\2\2\2\u010f\u0110\5f\64\2\u0110\u0111")
        buf.write("\7\34\2\2\u0111\u0113\5J&\2\u0112\u0114\7-\2\2\u0113\u0112")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0113\3\2\2\2\u0115")
        buf.write("\u0116\3\2\2\2\u0116\65\3\2\2\2\u0117\u0118\7\3\2\2\u0118")
        buf.write("\u0119\7!\2\2\u0119\u011a\5J&\2\u011a\u011e\7\"\2\2\u011b")
        buf.write("\u011d\7-\2\2\u011c\u011b\3\2\2\2\u011d\u0120\3\2\2\2")
        buf.write("\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0121\3")
        buf.write("\2\2\2\u0120\u011e\3\2\2\2\u0121\u0122\5\66\34\2\u0122")
        buf.write("\u013e\3\2\2\2\u0123\u0124\7\3\2\2\u0124\u0125\7!\2\2")
        buf.write("\u0125\u0126\5J&\2\u0126\u012a\7\"\2\2\u0127\u0129\7-")
        buf.write("\2\2\u0128\u0127\3\2\2\2\u0129\u012c\3\2\2\2\u012a\u0128")
        buf.write("\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012d\3\2\2\2\u012c")
        buf.write("\u012a\3\2\2\2\u012d\u0131\5\62\32\2\u012e\u0130\7-\2")
        buf.write("\2\u012f\u012e\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f")
        buf.write("\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0137\3\2\2\2\u0133")
        buf.write("\u0131\3\2\2\2\u0134\u0136\58\35\2\u0135\u0134\3\2\2\2")
        buf.write("\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3")
        buf.write("\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u013c")
        buf.write("\5:\36\2\u013b\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("\u013e\3\2\2\2\u013d\u0117\3\2\2\2\u013d\u0123\3\2\2\2")
        buf.write("\u013e\67\3\2\2\2\u013f\u0140\7\4\2\2\u0140\u0144\5J&")
        buf.write("\2\u0141\u0143\7-\2\2\u0142\u0141\3\2\2\2\u0143\u0146")
        buf.write("\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145")
        buf.write("\u0147\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0148\5\66\34")
        buf.write("\2\u0148\u0159\3\2\2\2\u0149\u014a\7\4\2\2\u014a\u014e")
        buf.write("\5J&\2\u014b\u014d\7-\2\2\u014c\u014b\3\2\2\2\u014d\u0150")
        buf.write("\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f")
        buf.write("\u0151\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u0155\5\62\32")
        buf.write("\2\u0152\u0154\7-\2\2\u0153\u0152\3\2\2\2\u0154\u0157")
        buf.write("\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0158\u013f\3\2\2\2")
        buf.write("\u0158\u0149\3\2\2\2\u01599\3\2\2\2\u015a\u015e\7\5\2")
        buf.write("\2\u015b\u015d\7-\2\2\u015c\u015b\3\2\2\2\u015d\u0160")
        buf.write("\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f")
        buf.write("\u0161\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0165\5\62\32")
        buf.write("\2\u0162\u0164\7-\2\2\u0163\u0162\3\2\2\2\u0164\u0167")
        buf.write("\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166")
        buf.write(";\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0169\7\6\2\2\u0169")
        buf.write("\u016a\7*\2\2\u016a\u016b\7\7\2\2\u016b\u016c\5J&\2\u016c")
        buf.write("\u016d\7\b\2\2\u016d\u0171\5> \2\u016e\u0170\7-\2\2\u016f")
        buf.write("\u016e\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2")
        buf.write("\u0171\u0172\3\2\2\2\u0172\u0174\3\2\2\2\u0173\u0171\3")
        buf.write("\2\2\2\u0174\u0178\5\62\32\2\u0175\u0177\7-\2\2\u0176")
        buf.write("\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179=\3\2\2\2\u017a\u0178\3\2\2")
        buf.write("\2\u017b\u017d\7\27\2\2\u017c\u017b\3\2\2\2\u017c\u017d")
        buf.write("\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f\5h\65\2\u017f")
        buf.write("?\3\2\2\2\u0180\u0182\7\t\2\2\u0181\u0183\7-\2\2\u0182")
        buf.write("\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185A\3\2\2\2\u0186\u0188\7\n\2")
        buf.write("\2\u0187\u0189\7-\2\2\u0188\u0187\3\2\2\2\u0189\u018a")
        buf.write("\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("C\3\2\2\2\u018c\u018e\7\13\2\2\u018d\u018f\5J&\2\u018e")
        buf.write("\u018d\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0191\3\2\2\2")
        buf.write("\u0190\u0192\7-\2\2\u0191\u0190\3\2\2\2\u0192\u0193\3")
        buf.write("\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194E")
        buf.write("\3\2\2\2\u0195\u0197\7\f\2\2\u0196\u0198\7-\2\2\u0197")
        buf.write("\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u0197\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019a\u019e\3\2\2\2\u019b\u019d\5")
        buf.write("\62\32\2\u019c\u019b\3\2\2\2\u019d\u01a0\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a1\3\2\2\2")
        buf.write("\u01a0\u019e\3\2\2\2\u01a1\u01a3\7\r\2\2\u01a2\u01a4\7")
        buf.write("-\2\2\u01a3\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6G\3\2\2\2\u01a7\u01a8")
        buf.write("\7*\2\2\u01a8\u01a9\7!\2\2\u01a9\u01aa\5Z.\2\u01aa\u01ac")
        buf.write("\7\"\2\2\u01ab\u01ad\7-\2\2\u01ac\u01ab\3\2\2\2\u01ad")
        buf.write("\u01ae\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01afI\3\2\2\2\u01b0\u01b1\b&\1\2\u01b1\u01b2\5L\'\2")
        buf.write("\u01b2\u01b8\3\2\2\2\u01b3\u01b4\f\4\2\2\u01b4\u01b5\7")
        buf.write("\33\2\2\u01b5\u01b7\5L\'\2\u01b6\u01b3\3\2\2\2\u01b7\u01ba")
        buf.write("\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9")
        buf.write("K\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc\b\'\1\2\u01bc")
        buf.write("\u01bd\5N(\2\u01bd\u01c3\3\2\2\2\u01be\u01bf\f\4\2\2\u01bf")
        buf.write("\u01c0\7\25\2\2\u01c0\u01c2\5N(\2\u01c1\u01be\3\2\2\2")
        buf.write("\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3")
        buf.write("\2\2\2\u01c4M\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7")
        buf.write("\b(\1\2\u01c7\u01c8\5P)\2\u01c8\u01ce\3\2\2\2\u01c9\u01ca")
        buf.write("\f\4\2\2\u01ca\u01cb\7\35\2\2\u01cb\u01cd\5P)\2\u01cc")
        buf.write("\u01c9\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cfO\3\2\2\2\u01d0\u01ce\3\2\2")
        buf.write("\2\u01d1\u01d2\b)\1\2\u01d2\u01d3\5R*\2\u01d3\u01d9\3")
        buf.write("\2\2\2\u01d4\u01d5\f\4\2\2\u01d5\u01d6\t\3\2\2\u01d6\u01d8")
        buf.write("\5R*\2\u01d7\u01d4\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7")
        buf.write("\3\2\2\2\u01d9\u01da\3\2\2\2\u01daQ\3\2\2\2\u01db\u01d9")
        buf.write("\3\2\2\2\u01dc\u01dd\b*\1\2\u01dd\u01de\5T+\2\u01de\u01e4")
        buf.write("\3\2\2\2\u01df\u01e0\f\4\2\2\u01e0\u01e1\t\4\2\2\u01e1")
        buf.write("\u01e3\5T+\2\u01e2\u01df\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4")
        buf.write("\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5S\3\2\2\2\u01e6")
        buf.write("\u01e4\3\2\2\2\u01e7\u01e8\7\24\2\2\u01e8\u01eb\5V,\2")
        buf.write("\u01e9\u01eb\5V,\2\u01ea\u01e7\3\2\2\2\u01ea\u01e9\3\2")
        buf.write("\2\2\u01ebU\3\2\2\2\u01ec\u01ed\7\27\2\2\u01ed\u01f0\5")
        buf.write("X-\2\u01ee\u01f0\5X-\2\u01ef\u01ec\3\2\2\2\u01ef\u01ee")
        buf.write("\3\2\2\2\u01f0W\3\2\2\2\u01f1\u01f2\7*\2\2\u01f2\u01f3")
        buf.write("\7!\2\2\u01f3\u01f4\5Z.\2\u01f4\u01f5\7\"\2\2\u01f5\u01fd")
        buf.write("\3\2\2\2\u01f6\u01f7\7*\2\2\u01f7\u01f8\7\37\2\2\u01f8")
        buf.write("\u01f9\5`\61\2\u01f9\u01fa\7 \2\2\u01fa\u01fd\3\2\2\2")
        buf.write("\u01fb\u01fd\5b\62\2\u01fc\u01f1\3\2\2\2\u01fc\u01f6\3")
        buf.write("\2\2\2\u01fc\u01fb\3\2\2\2\u01fdY\3\2\2\2\u01fe\u01ff")
        buf.write("\5\\/\2\u01ff\u0200\5^\60\2\u0200[\3\2\2\2\u0201\u0204")
        buf.write("\5J&\2\u0202\u0204\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0202")
        buf.write("\3\2\2\2\u0204]\3\2\2\2\u0205\u0206\7\36\2\2\u0206\u0207")
        buf.write("\5\\/\2\u0207\u0208\5^\60\2\u0208\u020b\3\2\2\2\u0209")
        buf.write("\u020b\3\2\2\2\u020a\u0205\3\2\2\2\u020a\u0209\3\2\2\2")
        buf.write("\u020b_\3\2\2\2\u020c\u020d\5J&\2\u020d\u020e\7\36\2\2")
        buf.write("\u020e\u020f\5`\61\2\u020f\u0212\3\2\2\2\u0210\u0212\5")
        buf.write("J&\2\u0211\u020c\3\2\2\2\u0211\u0210\3\2\2\2\u0212a\3")
        buf.write("\2\2\2\u0213\u0214\5d\63\2\u0214c\3\2\2\2\u0215\u021b")
        buf.write("\5h\65\2\u0216\u0217\7!\2\2\u0217\u0218\5J&\2\u0218\u0219")
        buf.write("\7\"\2\2\u0219\u021b\3\2\2\2\u021a\u0215\3\2\2\2\u021a")
        buf.write("\u0216\3\2\2\2\u021be\3\2\2\2\u021c\u0228\7*\2\2\u021d")
        buf.write("\u021e\7*\2\2\u021e\u021f\7!\2\2\u021f\u0220\5Z.\2\u0220")
        buf.write("\u0221\7\"\2\2\u0221\u0228\3\2\2\2\u0222\u0223\7*\2\2")
        buf.write("\u0223\u0224\7\37\2\2\u0224\u0225\5`\61\2\u0225\u0226")
        buf.write("\7 \2\2\u0226\u0228\3\2\2\2\u0227\u021c\3\2\2\2\u0227")
        buf.write("\u021d\3\2\2\2\u0227\u0222\3\2\2\2\u0228g\3\2\2\2\u0229")
        buf.write("\u0232\5j\66\2\u022a\u0232\7*\2\2\u022b\u022d\7\27\2\2")
        buf.write("\u022c\u022b\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022e\3")
        buf.write("\2\2\2\u022e\u0232\7#\2\2\u022f\u0232\7)\2\2\u0230\u0232")
        buf.write("\7(\2\2\u0231\u0229\3\2\2\2\u0231\u022a\3\2\2\2\u0231")
        buf.write("\u022c\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0230\3\2\2\2")
        buf.write("\u0232i\3\2\2\2\u0233\u0234\7\37\2\2\u0234\u0235\5h\65")
        buf.write("\2\u0235\u0236\5r:\2\u0236\u0237\7 \2\2\u0237k\3\2\2\2")
        buf.write("\u0238\u023a\7\36\2\2\u0239\u023b\7\27\2\2\u023a\u0239")
        buf.write("\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u023c\3\2\2\2\u023c")
        buf.write("\u023d\7#\2\2\u023d\u0240\5l\67\2\u023e\u0240\3\2\2\2")
        buf.write("\u023f\u0238\3\2\2\2\u023f\u023e\3\2\2\2\u0240m\3\2\2")
        buf.write("\2\u0241\u0242\7\36\2\2\u0242\u0243\7)\2\2\u0243\u0246")
        buf.write("\5n8\2\u0244\u0246\3\2\2\2\u0245\u0241\3\2\2\2\u0245\u0244")
        buf.write("\3\2\2\2\u0246o\3\2\2\2\u0247\u0248\7\36\2\2\u0248\u0249")
        buf.write("\7(\2\2\u0249\u024c\5p9\2\u024a\u024c\3\2\2\2\u024b\u0247")
        buf.write("\3\2\2\2\u024b\u024a\3\2\2\2\u024cq\3\2\2\2\u024d\u024e")
        buf.write("\7\36\2\2\u024e\u024f\5h\65\2\u024f\u0250\5r:\2\u0250")
        buf.write("\u0253\3\2\2\2\u0251\u0253\3\2\2\2\u0252\u024d\3\2\2\2")
        buf.write("\u0252\u0251\3\2\2\2\u0253s\3\2\2\2Cw~\u008a\u008e\u0093")
        buf.write("\u0097\u009e\u00a4\u00b0\u00bd\u00c2\u00ca\u00d2\u00d9")
        buf.write("\u00db\u00e3\u00ed\u00f5\u00fd\u0102\u010d\u0115\u011e")
        buf.write("\u012a\u0131\u0137\u013b\u013d\u0144\u014e\u0155\u0158")
        buf.write("\u015e\u0165\u0171\u0178\u017c\u0184\u018a\u018e\u0193")
        buf.write("\u0199\u019e\u01a5\u01ae\u01b8\u01c3\u01ce\u01d9\u01e4")
        buf.write("\u01ea\u01ef\u01fc\u0203\u020a\u0211\u021a\u0227\u022c")
        buf.write("\u0231\u023a\u023f\u0245\u024b\u0252")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'elif'", "'else'", "'for'", "'until'", 
                     "'by'", "'break'", "'continue'", "'return'", "'begin'", 
                     "'end'", "'bool'", "'number'", "'string'", "'dynamic'", 
                     "'var'", "'func'", "'not'", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'...'", "'<-'", "<INVALID>", 
                     "','", "'['", "']'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "IFOP", "ELIFOP", "ELSEOP", "FOROP", 
                      "UNTILOP", "BYOP", "BREAKOP", "CONTOP", "RETURNOP", 
                      "BEGINOP", "ENDOP", "BOOL_TYPE", "NUMBER_TYPE", "STR_TYPE", 
                      "DYNTYPE", "VARTYPE", "FUNCTYPE", "NOTOP", "ANDOR", 
                      "ADDOP", "SUBTR", "MULOP", "DIVOP", "MODOP", "CONCAT", 
                      "ASSIGN", "RELATION", "CM", "LP", "RP", "LB", "RB", 
                      "NUMLIT", "NUM1", "NUM2", "NUM3", "NUM4", "BOOLIT", 
                      "STRINGLIT", "IDENTIFIER", "COMMENT", "WS", "NL", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_declaretail = 2
    RULE_declare = 3
    RULE_var_declare = 4
    RULE_normaldeclare = 5
    RULE_var_type = 6
    RULE_initialnormal = 7
    RULE_assignmentexpr = 8
    RULE_arraydeclare = 9
    RULE_array = 10
    RULE_dimension = 11
    RULE_dimtail = 12
    RULE_initialarray = 13
    RULE_vartypedeclare = 14
    RULE_func_declare = 15
    RULE_parameters = 16
    RULE_param_here = 17
    RULE_param_list = 18
    RULE_paratail = 19
    RULE_para = 20
    RULE_isarrayindex = 21
    RULE_arrayindex = 22
    RULE_body = 23
    RULE_statement = 24
    RULE_assignment = 25
    RULE_ifstm = 26
    RULE_elifbranch = 27
    RULE_elsebranch = 28
    RULE_forstm = 29
    RULE_update = 30
    RULE_break_stm = 31
    RULE_continue_stm = 32
    RULE_return_stm = 33
    RULE_block = 34
    RULE_func_call_stm = 35
    RULE_expr = 36
    RULE_expr1 = 37
    RULE_expr2 = 38
    RULE_expr3 = 39
    RULE_expr4 = 40
    RULE_expr5 = 41
    RULE_expr6 = 42
    RULE_expr7 = 43
    RULE_arguments = 44
    RULE_arg = 45
    RULE_argtail = 46
    RULE_expr8 = 47
    RULE_expr9 = 48
    RULE_operand = 49
    RULE_lhs = 50
    RULE_literals = 51
    RULE_arraylit = 52
    RULE_numlittail = 53
    RULE_stringlittail = 54
    RULE_boolittail = 55
    RULE_arraylittail = 56

    ruleNames =  [ "program", "declaration", "declaretail", "declare", "var_declare", 
                   "normaldeclare", "var_type", "initialnormal", "assignmentexpr", 
                   "arraydeclare", "array", "dimension", "dimtail", "initialarray", 
                   "vartypedeclare", "func_declare", "parameters", "param_here", 
                   "param_list", "paratail", "para", "isarrayindex", "arrayindex", 
                   "body", "statement", "assignment", "ifstm", "elifbranch", 
                   "elsebranch", "forstm", "update", "break_stm", "continue_stm", 
                   "return_stm", "block", "func_call_stm", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "arguments", "arg", "argtail", "expr8", "expr9", "operand", 
                   "lhs", "literals", "arraylit", "numlittail", "stringlittail", 
                   "boolittail", "arraylittail" ]

    EOF = Token.EOF
    IFOP=1
    ELIFOP=2
    ELSEOP=3
    FOROP=4
    UNTILOP=5
    BYOP=6
    BREAKOP=7
    CONTOP=8
    RETURNOP=9
    BEGINOP=10
    ENDOP=11
    BOOL_TYPE=12
    NUMBER_TYPE=13
    STR_TYPE=14
    DYNTYPE=15
    VARTYPE=16
    FUNCTYPE=17
    NOTOP=18
    ANDOR=19
    ADDOP=20
    SUBTR=21
    MULOP=22
    DIVOP=23
    MODOP=24
    CONCAT=25
    ASSIGN=26
    RELATION=27
    CM=28
    LP=29
    RP=30
    LB=31
    RB=32
    NUMLIT=33
    NUM1=34
    NUM2=35
    NUM3=36
    NUM4=37
    BOOLIT=38
    STRINGLIT=39
    IDENTIFIER=40
    COMMENT=41
    WS=42
    NL=43
    ERROR_CHAR=44
    UNCLOSE_STRING=45
    ILLEGAL_ESCAPE=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 114
                self.match(ZCodeParser.NL)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.declaration()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 121
                self.match(ZCodeParser.NL)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare(self):
            return self.getTypedRuleContext(ZCodeParser.DeclareContext,0)


        def declaretail(self):
            return self.getTypedRuleContext(ZCodeParser.DeclaretailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.declare()
            self.state = 130
            self.declaretail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaretailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare(self):
            return self.getTypedRuleContext(ZCodeParser.DeclareContext,0)


        def declaretail(self):
            return self.getTypedRuleContext(ZCodeParser.DeclaretailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaretail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaretail" ):
                return visitor.visitDeclaretail(self)
            else:
                return visitor.visitChildren(self)




    def declaretail(self):

        localctx = ZCodeParser.DeclaretailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaretail)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.STR_TYPE, ZCodeParser.DYNTYPE, ZCodeParser.VARTYPE, ZCodeParser.FUNCTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.declare()
                self.state = 133
                self.declaretail()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NL]:
                self.enterOuterAlt(localctx, 2)

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


    class DeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declareContext,0)


        def func_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declareContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare" ):
                return visitor.visitDeclare(self)
            else:
                return visitor.visitChildren(self)




    def declare(self):

        localctx = ZCodeParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declare)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.STR_TYPE, ZCodeParser.DYNTYPE, ZCodeParser.VARTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.var_declare()
                pass
            elif token in [ZCodeParser.FUNCTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.func_declare()
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


    class Var_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normaldeclare(self):
            return self.getTypedRuleContext(ZCodeParser.NormaldeclareContext,0)


        def arraydeclare(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydeclareContext,0)


        def vartypedeclare(self):
            return self.getTypedRuleContext(ZCodeParser.VartypedeclareContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = ZCodeParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 142
                self.normaldeclare()
                pass

            elif la_ == 2:
                self.state = 143
                self.arraydeclare()
                pass

            elif la_ == 3:
                self.state = 144
                self.vartypedeclare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormaldeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def initialnormal(self):
            return self.getTypedRuleContext(ZCodeParser.InitialnormalContext,0)


        def var_type(self):
            return self.getTypedRuleContext(ZCodeParser.Var_typeContext,0)


        def DYNTYPE(self):
            return self.getToken(ZCodeParser.DYNTYPE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_normaldeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormaldeclare" ):
                return visitor.visitNormaldeclare(self)
            else:
                return visitor.visitChildren(self)




    def normaldeclare(self):

        localctx = ZCodeParser.NormaldeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_normaldeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.STR_TYPE]:
                self.state = 147
                self.var_type()
                pass
            elif token in [ZCodeParser.DYNTYPE]:
                self.state = 148
                self.match(ZCodeParser.DYNTYPE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 151
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 152
            self.initialnormal()
            self.state = 154 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 153
                    self.match(ZCodeParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 156 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_TYPE(self):
            return self.getToken(ZCodeParser.NUMBER_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(ZCodeParser.BOOL_TYPE, 0)

        def STR_TYPE(self):
            return self.getToken(ZCodeParser.STR_TYPE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_var_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_type" ):
                return visitor.visitVar_type(self)
            else:
                return visitor.visitChildren(self)




    def var_type(self):

        localctx = ZCodeParser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.BOOL_TYPE) | (1 << ZCodeParser.NUMBER_TYPE) | (1 << ZCodeParser.STR_TYPE))) != 0)):
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


    class InitialnormalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentexpr(self):
            return self.getTypedRuleContext(ZCodeParser.AssignmentexprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_initialnormal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialnormal" ):
                return visitor.visitInitialnormal(self)
            else:
                return visitor.visitChildren(self)




    def initialnormal(self):

        localctx = ZCodeParser.InitialnormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_initialnormal)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.assignmentexpr()
                pass
            elif token in [ZCodeParser.NL]:
                self.enterOuterAlt(localctx, 2)

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


    class AssignmentexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignmentexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentexpr" ):
                return visitor.visitAssignmentexpr(self)
            else:
                return visitor.visitChildren(self)




    def assignmentexpr(self):

        localctx = ZCodeParser.AssignmentexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignmentexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(ZCodeParser.ASSIGN)
            self.state = 165
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(ZCodeParser.Var_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def initialarray(self):
            return self.getTypedRuleContext(ZCodeParser.InitialarrayContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydeclare" ):
                return visitor.visitArraydeclare(self)
            else:
                return visitor.visitChildren(self)




    def arraydeclare(self):

        localctx = ZCodeParser.ArraydeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arraydeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.var_type()
            self.state = 168
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 169
            self.array()
            self.state = 170
            self.initialarray()
            self.state = 172 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 171
                    self.match(ZCodeParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 174 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def dimension(self):
            return self.getTypedRuleContext(ZCodeParser.DimensionContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(ZCodeParser.LP)
            self.state = 177
            self.dimension()
            self.state = 178
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def dimtail(self):
            return self.getTypedRuleContext(ZCodeParser.DimtailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = ZCodeParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(ZCodeParser.NUMLIT)
            self.state = 181
            self.dimtail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimtailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def dimtail(self):
            return self.getTypedRuleContext(ZCodeParser.DimtailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dimtail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimtail" ):
                return visitor.visitDimtail(self)
            else:
                return visitor.visitChildren(self)




    def dimtail(self):

        localctx = ZCodeParser.DimtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dimtail)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(ZCodeParser.CM)
                self.state = 184
                self.match(ZCodeParser.NUMLIT)
                self.state = 185
                self.dimtail()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class InitialarrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_initialarray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialarray" ):
                return visitor.visitInitialarray(self)
            else:
                return visitor.visitChildren(self)




    def initialarray(self):

        localctx = ZCodeParser.InitialarrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_initialarray)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(ZCodeParser.ASSIGN)
                self.state = 190
                self.expr(0)
                pass
            elif token in [ZCodeParser.NL]:
                self.enterOuterAlt(localctx, 2)

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


    class VartypedeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARTYPE(self):
            return self.getToken(ZCodeParser.VARTYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def assignmentexpr(self):
            return self.getTypedRuleContext(ZCodeParser.AssignmentexprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vartypedeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartypedeclare" ):
                return visitor.visitVartypedeclare(self)
            else:
                return visitor.visitChildren(self)




    def vartypedeclare(self):

        localctx = ZCodeParser.VartypedeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_vartypedeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(ZCodeParser.VARTYPE)
            self.state = 195
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 196
            self.assignmentexpr()
            self.state = 198 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 197
                    self.match(ZCodeParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 200 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTYPE(self):
            return self.getToken(ZCodeParser.FUNCTYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def parameters(self):
            return self.getTypedRuleContext(ZCodeParser.ParametersContext,0)


        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declare" ):
                return visitor.visitFunc_declare(self)
            else:
                return visitor.visitChildren(self)




    def func_declare(self):

        localctx = ZCodeParser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(ZCodeParser.FUNCTYPE)
            self.state = 203
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 204
            self.parameters()
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 205
                    self.match(ZCodeParser.NL) 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 211
                self.body()
                pass

            elif la_ == 2:
                self.state = 213 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 212
                        self.match(ZCodeParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 215 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def param_here(self):
            return self.getTypedRuleContext(ZCodeParser.Param_hereContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = ZCodeParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(ZCodeParser.LB)
            self.state = 220
            self.param_here()
            self.state = 221
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_hereContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_here

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_here" ):
                return visitor.visitParam_here(self)
            else:
                return visitor.visitChildren(self)




    def param_here(self):

        localctx = ZCodeParser.Param_hereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_param_here)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.STR_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.param_list()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(ZCodeParser.ParaContext,0)


        def paratail(self):
            return self.getTypedRuleContext(ZCodeParser.ParatailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.para()
            self.state = 228
            self.paratail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParatailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def para(self):
            return self.getTypedRuleContext(ZCodeParser.ParaContext,0)


        def paratail(self):
            return self.getTypedRuleContext(ZCodeParser.ParatailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paratail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParatail" ):
                return visitor.visitParatail(self)
            else:
                return visitor.visitChildren(self)




    def paratail(self):

        localctx = ZCodeParser.ParatailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_paratail)
        try:
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(ZCodeParser.CM)
                self.state = 231
                self.para()
                self.state = 232
                self.paratail()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(ZCodeParser.Var_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def isarrayindex(self):
            return self.getTypedRuleContext(ZCodeParser.IsarrayindexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = ZCodeParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.var_type()
            self.state = 238
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 239
            self.isarrayindex()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IsarrayindexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayindex(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayindexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_isarrayindex

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsarrayindex" ):
                return visitor.visitIsarrayindex(self)
            else:
                return visitor.visitChildren(self)




    def isarrayindex(self):

        localctx = ZCodeParser.IsarrayindexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_isarrayindex)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.arrayindex()
                pass
            elif token in [ZCodeParser.CM, ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class ArrayindexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayindex

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayindex" ):
                return visitor.visitArrayindex(self)
            else:
                return visitor.visitChildren(self)




    def arrayindex(self):

        localctx = ZCodeParser.ArrayindexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_arrayindex)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(ZCodeParser.LP)
                self.state = 246
                self.expr(0)
                self.state = 247
                self.match(ZCodeParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(ZCodeParser.LP)
                self.state = 250
                self.match(ZCodeParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmContext,0)


        def block(self):
            return self.getTypedRuleContext(ZCodeParser.BlockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = ZCodeParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_body)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURNOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.return_stm()
                pass
            elif token in [ZCodeParser.BEGINOP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.block()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.BOOL_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.STR_TYPE, ZCodeParser.DYNTYPE, ZCodeParser.VARTYPE, ZCodeParser.FUNCTYPE, ZCodeParser.NL]:
                self.enterOuterAlt(localctx, 3)

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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declareContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ZCodeParser.AssignmentContext,0)


        def ifstm(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmContext,0)


        def forstm(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmContext,0)


        def break_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmContext,0)


        def continue_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmContext,0)


        def return_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmContext,0)


        def func_call_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_stmContext,0)


        def block(self):
            return self.getTypedRuleContext(ZCodeParser.BlockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_statement)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.var_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
                self.ifstm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 261
                self.forstm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 262
                self.break_stm()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 263
                self.continue_stm()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 264
                self.return_stm()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 265
                self.func_call_stm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 266
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ZCodeParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.lhs()
            self.state = 270
            self.match(ZCodeParser.ASSIGN)
            self.state = 271
            self.expr(0)
            self.state = 273 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 272
                    self.match(ZCodeParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 275 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IFOP(self):
            return self.getToken(ZCodeParser.IFOP, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def ifstm(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def elifbranch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ElifbranchContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ElifbranchContext,i)


        def elsebranch(self):
            return self.getTypedRuleContext(ZCodeParser.ElsebranchContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstm" ):
                return visitor.visitIfstm(self)
            else:
                return visitor.visitChildren(self)




    def ifstm(self):

        localctx = ZCodeParser.IfstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ifstm)
        self._la = 0 # Token type
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(ZCodeParser.IFOP)
                self.state = 278
                self.match(ZCodeParser.LB)
                self.state = 279
                self.expr(0)
                self.state = 280
                self.match(ZCodeParser.RB)
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NL:
                    self.state = 281
                    self.match(ZCodeParser.NL)
                    self.state = 286
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 287
                self.ifstm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.match(ZCodeParser.IFOP)
                self.state = 290
                self.match(ZCodeParser.LB)
                self.state = 291
                self.expr(0)
                self.state = 292
                self.match(ZCodeParser.RB)
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NL:
                    self.state = 293
                    self.match(ZCodeParser.NL)
                    self.state = 298
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 299
                self.statement()
                self.state = 303
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 300
                        self.match(ZCodeParser.NL) 
                    self.state = 305
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 306
                        self.elifbranch() 
                    self.state = 311
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                self.state = 313
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 312
                    self.elsebranch()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifbranchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIFOP(self):
            return self.getToken(ZCodeParser.ELIFOP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def ifstm(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifbranch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifbranch" ):
                return visitor.visitElifbranch(self)
            else:
                return visitor.visitChildren(self)




    def elifbranch(self):

        localctx = ZCodeParser.ElifbranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_elifbranch)
        self._la = 0 # Token type
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(ZCodeParser.ELIFOP)
                self.state = 318
                self.expr(0)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NL:
                    self.state = 319
                    self.match(ZCodeParser.NL)
                    self.state = 324
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 325
                self.ifstm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.match(ZCodeParser.ELIFOP)
                self.state = 328
                self.expr(0)
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NL:
                    self.state = 329
                    self.match(ZCodeParser.NL)
                    self.state = 334
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 335
                self.statement()
                self.state = 339
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 336
                        self.match(ZCodeParser.NL) 
                    self.state = 341
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsebranchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEOP(self):
            return self.getToken(ZCodeParser.ELSEOP, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elsebranch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsebranch" ):
                return visitor.visitElsebranch(self)
            else:
                return visitor.visitChildren(self)




    def elsebranch(self):

        localctx = ZCodeParser.ElsebranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elsebranch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(ZCodeParser.ELSEOP)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 345
                self.match(ZCodeParser.NL)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 351
            self.statement()
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 352
                    self.match(ZCodeParser.NL) 
                self.state = 357
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOROP(self):
            return self.getToken(ZCodeParser.FOROP, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTILOP(self):
            return self.getToken(ZCodeParser.UNTILOP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def BYOP(self):
            return self.getToken(ZCodeParser.BYOP, 0)

        def update(self):
            return self.getTypedRuleContext(ZCodeParser.UpdateContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_forstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstm" ):
                return visitor.visitForstm(self)
            else:
                return visitor.visitChildren(self)




    def forstm(self):

        localctx = ZCodeParser.ForstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forstm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(ZCodeParser.FOROP)
            self.state = 359
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 360
            self.match(ZCodeParser.UNTILOP)
            self.state = 361
            self.expr(0)
            self.state = 362
            self.match(ZCodeParser.BYOP)
            self.state = 363
            self.update()
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 364
                self.match(ZCodeParser.NL)
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 370
            self.statement()
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 371
                    self.match(ZCodeParser.NL) 
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


        def SUBTR(self):
            return self.getToken(ZCodeParser.SUBTR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = ZCodeParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 377
                self.match(ZCodeParser.SUBTR)


            self.state = 380
            self.literals()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAKOP(self):
            return self.getToken(ZCodeParser.BREAKOP, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stm" ):
                return visitor.visitBreak_stm(self)
            else:
                return visitor.visitChildren(self)




    def break_stm(self):

        localctx = ZCodeParser.Break_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(ZCodeParser.BREAKOP)
            self.state = 384 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 383
                    self.match(ZCodeParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 386 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTOP(self):
            return self.getToken(ZCodeParser.CONTOP, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stm" ):
                return visitor.visitContinue_stm(self)
            else:
                return visitor.visitChildren(self)




    def continue_stm(self):

        localctx = ZCodeParser.Continue_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(ZCodeParser.CONTOP)
            self.state = 390 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 389
                    self.match(ZCodeParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 392 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURNOP(self):
            return self.getToken(ZCodeParser.RETURNOP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = ZCodeParser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_return_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(ZCodeParser.RETURNOP)
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOTOP) | (1 << ZCodeParser.SUBTR) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 395
                self.expr(0)


            self.state = 399 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 398
                    self.match(ZCodeParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 401 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGINOP(self):
            return self.getToken(ZCodeParser.BEGINOP, 0)

        def ENDOP(self):
            return self.getToken(ZCodeParser.ENDOP, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ZCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(ZCodeParser.BEGINOP)
            self.state = 405 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 404
                self.match(ZCodeParser.NL)
                self.state = 407 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NL):
                    break

            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.IFOP) | (1 << ZCodeParser.FOROP) | (1 << ZCodeParser.BREAKOP) | (1 << ZCodeParser.CONTOP) | (1 << ZCodeParser.RETURNOP) | (1 << ZCodeParser.BEGINOP) | (1 << ZCodeParser.BOOL_TYPE) | (1 << ZCodeParser.NUMBER_TYPE) | (1 << ZCodeParser.STR_TYPE) | (1 << ZCodeParser.DYNTYPE) | (1 << ZCodeParser.VARTYPE) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 409
                self.statement()
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 415
            self.match(ZCodeParser.ENDOP)
            self.state = 417 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 416
                    self.match(ZCodeParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 419 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def arguments(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentsContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stm" ):
                return visitor.visitFunc_call_stm(self)
            else:
                return visitor.visitChildren(self)




    def func_call_stm(self):

        localctx = ZCodeParser.Func_call_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_func_call_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 422
            self.match(ZCodeParser.LB)
            self.state = 423
            self.arguments()
            self.state = 424
            self.match(ZCodeParser.RB)
            self.state = 426 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 425
                    self.match(ZCodeParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 428 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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

        def expr1(self):
            return self.getTypedRuleContext(ZCodeParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 433
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 434
                    self.match(ZCodeParser.CONCAT)
                    self.state = 435
                    self.expr1(0) 
                self.state = 440
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(ZCodeParser.Expr1Context,0)


        def ANDOR(self):
            return self.getToken(ZCodeParser.ANDOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 449
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 444
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 445
                    self.match(ZCodeParser.ANDOR)
                    self.state = 446
                    self.expr2(0) 
                self.state = 451
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def RELATION(self):
            return self.getToken(ZCodeParser.RELATION, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 460
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 455
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 456
                    self.match(ZCodeParser.RELATION)
                    self.state = 457
                    self.expr3(0) 
                self.state = 462
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADDOP(self):
            return self.getToken(ZCodeParser.ADDOP, 0)

        def SUBTR(self):
            return self.getToken(ZCodeParser.SUBTR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 471
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 466
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 467
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADDOP or _la==ZCodeParser.SUBTR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 468
                    self.expr4(0) 
                self.state = 473
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MULOP(self):
            return self.getToken(ZCodeParser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(ZCodeParser.DIVOP, 0)

        def MODOP(self):
            return self.getToken(ZCodeParser.MODOP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 477
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 478
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULOP) | (1 << ZCodeParser.DIVOP) | (1 << ZCodeParser.MODOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 479
                    self.expr5() 
                self.state = 484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTOP(self):
            return self.getToken(ZCodeParser.NOTOP, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr5)
        try:
            self.state = 488
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.match(ZCodeParser.NOTOP)
                self.state = 486
                self.expr6()
                pass
            elif token in [ZCodeParser.SUBTR, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NUMLIT, ZCodeParser.BOOLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.expr6()
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBTR(self):
            return self.getToken(ZCodeParser.SUBTR, 0)

        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr6)
        try:
            self.state = 493
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.match(ZCodeParser.SUBTR)
                self.state = 491
                self.expr7()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
                self.expr7()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def arguments(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentsContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def expr9(self):
            return self.getTypedRuleContext(ZCodeParser.Expr9Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr7)
        try:
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 496
                self.match(ZCodeParser.LB)
                self.state = 497
                self.arguments()
                self.state = 498
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 501
                self.match(ZCodeParser.LP)
                self.state = 502
                self.expr8()
                self.state = 503
                self.match(ZCodeParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 505
                self.expr9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self):
            return self.getTypedRuleContext(ZCodeParser.ArgContext,0)


        def argtail(self):
            return self.getTypedRuleContext(ZCodeParser.ArgtailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = ZCodeParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.arg()
            self.state = 509
            self.argtail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = ZCodeParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arg)
        try:
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOTOP, ZCodeParser.SUBTR, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NUMLIT, ZCodeParser.BOOLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.expr(0)
                pass
            elif token in [ZCodeParser.CM, ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class ArgtailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def arg(self):
            return self.getTypedRuleContext(ZCodeParser.ArgContext,0)


        def argtail(self):
            return self.getTypedRuleContext(ZCodeParser.ArgtailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argtail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgtail" ):
                return visitor.visitArgtail(self)
            else:
                return visitor.visitChildren(self)




    def argtail(self):

        localctx = ZCodeParser.ArgtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_argtail)
        try:
            self.state = 520
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.match(ZCodeParser.CM)
                self.state = 516
                self.arg()
                self.state = 517
                self.argtail()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr8)
        try:
            self.state = 527
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 522
                self.expr(0)
                self.state = 523
                self.match(ZCodeParser.CM)
                self.state = 524
                self.expr8()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 526
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = ZCodeParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expr9)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_operand)
        try:
            self.state = 536
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUBTR, ZCodeParser.LP, ZCodeParser.NUMLIT, ZCodeParser.BOOLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.literals()
                pass
            elif token in [ZCodeParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
                self.match(ZCodeParser.LB)
                self.state = 533
                self.expr(0)
                self.state = 534
                self.match(ZCodeParser.RB)
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


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def arguments(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentsContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_lhs)
        try:
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 540
                self.match(ZCodeParser.LB)
                self.state = 541
                self.arguments()
                self.state = 542
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 544
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 545
                self.match(ZCodeParser.LP)
                self.state = 546
                self.expr8()
                self.state = 547
                self.match(ZCodeParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraylit(self):
            return self.getTypedRuleContext(ZCodeParser.ArraylitContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def SUBTR(self):
            return self.getToken(ZCodeParser.SUBTR, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def BOOLIT(self):
            return self.getToken(ZCodeParser.BOOLIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = ZCodeParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.state = 559
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.arraylit()
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [ZCodeParser.SUBTR, ZCodeParser.NUMLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 554
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.SUBTR:
                    self.state = 553
                    self.match(ZCodeParser.SUBTR)


                self.state = 556
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 557
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.BOOLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 558
                self.match(ZCodeParser.BOOLIT)
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


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


        def arraylittail(self):
            return self.getTypedRuleContext(ZCodeParser.ArraylittailContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = ZCodeParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.match(ZCodeParser.LP)
            self.state = 562
            self.literals()
            self.state = 563
            self.arraylittail()
            self.state = 564
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumlittailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def numlittail(self):
            return self.getTypedRuleContext(ZCodeParser.NumlittailContext,0)


        def SUBTR(self):
            return self.getToken(ZCodeParser.SUBTR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_numlittail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumlittail" ):
                return visitor.visitNumlittail(self)
            else:
                return visitor.visitChildren(self)




    def numlittail(self):

        localctx = ZCodeParser.NumlittailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_numlittail)
        self._la = 0 # Token type
        try:
            self.state = 573
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.match(ZCodeParser.CM)
                self.state = 568
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.SUBTR:
                    self.state = 567
                    self.match(ZCodeParser.SUBTR)


                self.state = 570
                self.match(ZCodeParser.NUMLIT)
                self.state = 571
                self.numlittail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringlittailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def stringlittail(self):
            return self.getTypedRuleContext(ZCodeParser.StringlittailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stringlittail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringlittail" ):
                return visitor.visitStringlittail(self)
            else:
                return visitor.visitChildren(self)




    def stringlittail(self):

        localctx = ZCodeParser.StringlittailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_stringlittail)
        try:
            self.state = 579
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 575
                self.match(ZCodeParser.CM)
                self.state = 576
                self.match(ZCodeParser.STRINGLIT)
                self.state = 577
                self.stringlittail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolittailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def BOOLIT(self):
            return self.getToken(ZCodeParser.BOOLIT, 0)

        def boolittail(self):
            return self.getTypedRuleContext(ZCodeParser.BoolittailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_boolittail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolittail" ):
                return visitor.visitBoolittail(self)
            else:
                return visitor.visitChildren(self)




    def boolittail(self):

        localctx = ZCodeParser.BoolittailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_boolittail)
        try:
            self.state = 585
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.match(ZCodeParser.CM)
                self.state = 582
                self.match(ZCodeParser.BOOLIT)
                self.state = 583
                self.boolittail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylittailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


        def arraylittail(self):
            return self.getTypedRuleContext(ZCodeParser.ArraylittailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arraylittail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylittail" ):
                return visitor.visitArraylittail(self)
            else:
                return visitor.visitChildren(self)




    def arraylittail(self):

        localctx = ZCodeParser.ArraylittailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_arraylittail)
        try:
            self.state = 592
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 587
                self.match(ZCodeParser.CM)
                self.state = 588
                self.literals()
                self.state = 589
                self.arraylittail()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[36] = self.expr_sempred
        self._predicates[37] = self.expr1_sempred
        self._predicates[38] = self.expr2_sempred
        self._predicates[39] = self.expr3_sempred
        self._predicates[40] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




