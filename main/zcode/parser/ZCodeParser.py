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
        buf.write("\u01eb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\7\2t\n")
        buf.write("\2\f\2\16\2w\13\2\3\2\6\2z\n\2\r\2\16\2{\3\2\7\2\177\n")
        buf.write("\2\f\2\16\2\u0082\13\2\3\2\3\2\3\3\3\3\5\3\u0088\n\3\3")
        buf.write("\3\6\3\u008b\n\3\r\3\16\3\u008c\3\4\3\4\3\4\5\4\u0092")
        buf.write("\n\4\3\5\3\5\5\5\u0096\n\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\7\5\7\u00a0\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00b2\n\13\3\f\3")
        buf.write("\f\3\f\5\f\u00b7\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00c0")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u00c7\n\16\3\17\3\17")
        buf.write("\3\17\5\17\u00cc\n\17\3\17\3\17\3\17\5\17\u00d1\n\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\7\21\u00de\n\21\f\21\16\21\u00e1\13\21\3\21\3\21\3\22")
        buf.write("\3\22\5\22\u00e7\n\22\3\23\3\23\3\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\5\24\u00f1\n\24\3\25\3\25\3\25\3\25\5\25\u00f7")
        buf.write("\n\25\3\26\3\26\5\26\u00fb\n\26\3\27\3\27\5\27\u00ff\n")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u010a\n\30\3\30\6\30\u010d\n\30\r\30\16\30\u010e\5\30")
        buf.write("\u0111\n\30\3\31\3\31\3\31\3\31\3\32\3\32\5\32\u0119\n")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\5\34\u0122\n\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\5\36\u012c\n")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\7\37\u0133\n\37\f\37\16\37")
        buf.write("\u0136\13\37\3\37\3\37\3\37\3\37\3 \3 \5 \u013e\n \3!")
        buf.write("\3!\5!\u0142\n!\3\"\3\"\3\"\3\"\3\"\7\"\u0149\n\"\f\"")
        buf.write("\16\"\u014c\13\"\3\"\3\"\3\"\3#\3#\5#\u0153\n#\3$\3$\7")
        buf.write("$\u0157\n$\f$\16$\u015a\13$\3$\3$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\7%\u0165\n%\f%\16%\u0168\13%\3%\3%\3&\3&\3\'\3\'\3(")
        buf.write("\3(\3)\3)\3*\3*\5*\u0176\n*\3+\3+\3+\3+\3+\3,\3,\5,\u017f")
        buf.write("\n,\3-\3-\3-\3.\3.\3.\3.\3.\5.\u0189\n.\3/\3/\6/\u018d")
        buf.write("\n/\r/\16/\u018e\3/\7/\u0192\n/\f/\16/\u0195\13/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u019f\n\60\f\60\16")
        buf.write("\60\u01a2\13\60\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u01aa")
        buf.write("\n\61\f\61\16\61\u01ad\13\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\7\62\u01b5\n\62\f\62\16\62\u01b8\13\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\7\63\u01c0\n\63\f\63\16\63\u01c3")
        buf.write("\13\63\3\64\3\64\3\64\3\64\3\64\3\64\7\64\u01cb\n\64\f")
        buf.write("\64\16\64\u01ce\13\64\3\65\3\65\3\65\5\65\u01d3\n\65\3")
        buf.write("\66\3\66\3\66\5\66\u01d8\n\66\3\67\3\67\3\67\5\67\u01dd")
        buf.write("\n\67\38\38\38\38\38\39\39\39\39\39\59\u01e9\n9\39\2\7")
        buf.write("^`bdf:\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\5\3\2\16")
        buf.write("\20\3\2\26\27\3\2\30\32\2\u01ec\2u\3\2\2\2\4\u0087\3\2")
        buf.write("\2\2\6\u0091\3\2\2\2\b\u0095\3\2\2\2\n\u009a\3\2\2\2\f")
        buf.write("\u009f\3\2\2\2\16\u00a1\3\2\2\2\20\u00a6\3\2\2\2\22\u00aa")
        buf.write("\3\2\2\2\24\u00b1\3\2\2\2\26\u00b6\3\2\2\2\30\u00bf\3")
        buf.write("\2\2\2\32\u00c6\3\2\2\2\34\u00d0\3\2\2\2\36\u00d2\3\2")
        buf.write("\2\2 \u00d7\3\2\2\2\"\u00e6\3\2\2\2$\u00e8\3\2\2\2&\u00f0")
        buf.write("\3\2\2\2(\u00f2\3\2\2\2*\u00fa\3\2\2\2,\u00fe\3\2\2\2")
        buf.write(".\u0110\3\2\2\2\60\u0112\3\2\2\2\62\u0118\3\2\2\2\64\u011a")
        buf.write("\3\2\2\2\66\u0121\3\2\2\28\u0123\3\2\2\2:\u012b\3\2\2")
        buf.write("\2<\u012d\3\2\2\2>\u013d\3\2\2\2@\u0141\3\2\2\2B\u0143")
        buf.write("\3\2\2\2D\u0152\3\2\2\2F\u0154\3\2\2\2H\u015d\3\2\2\2")
        buf.write("J\u016b\3\2\2\2L\u016d\3\2\2\2N\u016f\3\2\2\2P\u0171\3")
        buf.write("\2\2\2R\u0173\3\2\2\2T\u0177\3\2\2\2V\u017e\3\2\2\2X\u0180")
        buf.write("\3\2\2\2Z\u0188\3\2\2\2\\\u018a\3\2\2\2^\u0198\3\2\2\2")
        buf.write("`\u01a3\3\2\2\2b\u01ae\3\2\2\2d\u01b9\3\2\2\2f\u01c4\3")
        buf.write("\2\2\2h\u01d2\3\2\2\2j\u01d7\3\2\2\2l\u01dc\3\2\2\2n\u01de")
        buf.write("\3\2\2\2p\u01e8\3\2\2\2rt\7-\2\2sr\3\2\2\2tw\3\2\2\2u")
        buf.write("s\3\2\2\2uv\3\2\2\2vy\3\2\2\2wu\3\2\2\2xz\5\4\3\2yx\3")
        buf.write("\2\2\2z{\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\u0080\3\2\2\2}\177")
        buf.write("\7-\2\2~}\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080")
        buf.write("\u0081\3\2\2\2\u0081\u0083\3\2\2\2\u0082\u0080\3\2\2\2")
        buf.write("\u0083\u0084\7\2\2\3\u0084\3\3\2\2\2\u0085\u0088\5\6\4")
        buf.write("\2\u0086\u0088\5 \21\2\u0087\u0085\3\2\2\2\u0087\u0086")
        buf.write("\3\2\2\2\u0088\u008a\3\2\2\2\u0089\u008b\7-\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008a\3\2\2\2")
        buf.write("\u008c\u008d\3\2\2\2\u008d\5\3\2\2\2\u008e\u0092\5\b\5")
        buf.write("\2\u008f\u0092\5\16\b\2\u0090\u0092\5\36\20\2\u0091\u008e")
        buf.write("\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092")
        buf.write("\7\3\2\2\2\u0093\u0096\5\n\6\2\u0094\u0096\7\21\2\2\u0095")
        buf.write("\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\u0098\7*\2\2\u0098\u0099\5\f\7\2\u0099\t\3\2\2")
        buf.write("\2\u009a\u009b\t\2\2\2\u009b\13\3\2\2\2\u009c\u009d\7")
        buf.write("\34\2\2\u009d\u00a0\5^\60\2\u009e\u00a0\3\2\2\2\u009f")
        buf.write("\u009c\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\r\3\2\2\2\u00a1")
        buf.write("\u00a2\5\n\6\2\u00a2\u00a3\7*\2\2\u00a3\u00a4\5\20\t\2")
        buf.write("\u00a4\u00a5\5\26\f\2\u00a5\17\3\2\2\2\u00a6\u00a7\7\37")
        buf.write("\2\2\u00a7\u00a8\5\22\n\2\u00a8\u00a9\7 \2\2\u00a9\21")
        buf.write("\3\2\2\2\u00aa\u00ab\7#\2\2\u00ab\u00ac\5\24\13\2\u00ac")
        buf.write("\23\3\2\2\2\u00ad\u00ae\7\36\2\2\u00ae\u00af\7#\2\2\u00af")
        buf.write("\u00b2\5\24\13\2\u00b0\u00b2\3\2\2\2\u00b1\u00ad\3\2\2")
        buf.write("\2\u00b1\u00b0\3\2\2\2\u00b2\25\3\2\2\2\u00b3\u00b4\7")
        buf.write("\34\2\2\u00b4\u00b7\5^\60\2\u00b5\u00b7\3\2\2\2\u00b6")
        buf.write("\u00b3\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\27\3\2\2\2\u00b8")
        buf.write("\u00b9\7\37\2\2\u00b9\u00ba\5\34\17\2\u00ba\u00bb\5\32")
        buf.write("\16\2\u00bb\u00bc\7 \2\2\u00bc\u00c0\3\2\2\2\u00bd\u00be")
        buf.write("\7\37\2\2\u00be\u00c0\7 \2\2\u00bf\u00b8\3\2\2\2\u00bf")
        buf.write("\u00bd\3\2\2\2\u00c0\31\3\2\2\2\u00c1\u00c2\7\36\2\2\u00c2")
        buf.write("\u00c3\5\34\17\2\u00c3\u00c4\5\32\16\2\u00c4\u00c7\3\2")
        buf.write("\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c1\3\2\2\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7\33\3\2\2\2\u00c8\u00d1\5\30\r\2\u00c9\u00d1")
        buf.write("\7*\2\2\u00ca\u00cc\7\27\2\2\u00cb\u00ca\3\2\2\2\u00cb")
        buf.write("\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00d1\7#\2\2")
        buf.write("\u00ce\u00d1\7)\2\2\u00cf\u00d1\7(\2\2\u00d0\u00c8\3\2")
        buf.write("\2\2\u00d0\u00c9\3\2\2\2\u00d0\u00cb\3\2\2\2\u00d0\u00ce")
        buf.write("\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1\35\3\2\2\2\u00d2\u00d3")
        buf.write("\7\22\2\2\u00d3\u00d4\7*\2\2\u00d4\u00d5\7\34\2\2\u00d5")
        buf.write("\u00d6\5^\60\2\u00d6\37\3\2\2\2\u00d7\u00d8\7\23\2\2\u00d8")
        buf.write("\u00d9\7*\2\2\u00d9\u00da\7!\2\2\u00da\u00db\5\"\22\2")
        buf.write("\u00db\u00df\7\"\2\2\u00dc\u00de\7-\2\2\u00dd\u00dc\3")
        buf.write("\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0")
        buf.write("\3\2\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2")
        buf.write("\u00e3\5*\26\2\u00e3!\3\2\2\2\u00e4\u00e7\5$\23\2\u00e5")
        buf.write("\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2")
        buf.write("\u00e7#\3\2\2\2\u00e8\u00e9\5(\25\2\u00e9\u00ea\5&\24")
        buf.write("\2\u00ea%\3\2\2\2\u00eb\u00ec\7\36\2\2\u00ec\u00ed\5(")
        buf.write("\25\2\u00ed\u00ee\5&\24\2\u00ee\u00f1\3\2\2\2\u00ef\u00f1")
        buf.write("\3\2\2\2\u00f0\u00eb\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1")
        buf.write("\'\3\2\2\2\u00f2\u00f6\5\n\6\2\u00f3\u00f7\7*\2\2\u00f4")
        buf.write("\u00f5\7*\2\2\u00f5\u00f7\5\20\t\2\u00f6\u00f3\3\2\2\2")
        buf.write("\u00f6\u00f4\3\2\2\2\u00f7)\3\2\2\2\u00f8\u00fb\5,\27")
        buf.write("\2\u00f9\u00fb\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9")
        buf.write("\3\2\2\2\u00fb+\3\2\2\2\u00fc\u00ff\5R*\2\u00fd\u00ff")
        buf.write("\5\\/\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff")
        buf.write("-\3\2\2\2\u0100\u0111\5<\37\2\u0101\u0111\5H%\2\u0102")
        buf.write("\u010a\5\6\4\2\u0103\u010a\5\60\31\2\u0104\u010a\5N(\2")
        buf.write("\u0105\u010a\5P)\2\u0106\u010a\5R*\2\u0107\u010a\5T+\2")
        buf.write("\u0108\u010a\5\\/\2\u0109\u0102\3\2\2\2\u0109\u0103\3")
        buf.write("\2\2\2\u0109\u0104\3\2\2\2\u0109\u0105\3\2\2\2\u0109\u0106")
        buf.write("\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a")
        buf.write("\u010c\3\2\2\2\u010b\u010d\7-\2\2\u010c\u010b\3\2\2\2")
        buf.write("\u010d\u010e\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3")
        buf.write("\2\2\2\u010f\u0111\3\2\2\2\u0110\u0100\3\2\2\2\u0110\u0101")
        buf.write("\3\2\2\2\u0110\u0109\3\2\2\2\u0111/\3\2\2\2\u0112\u0113")
        buf.write("\5\62\32\2\u0113\u0114\7\34\2\2\u0114\u0115\5^\60\2\u0115")
        buf.write("\61\3\2\2\2\u0116\u0119\7*\2\2\u0117\u0119\5\64\33\2\u0118")
        buf.write("\u0116\3\2\2\2\u0118\u0117\3\2\2\2\u0119\63\3\2\2\2\u011a")
        buf.write("\u011b\5\66\34\2\u011b\u011c\7\37\2\2\u011c\u011d\58\35")
        buf.write("\2\u011d\u011e\7 \2\2\u011e\65\3\2\2\2\u011f\u0122\7*")
        buf.write("\2\2\u0120\u0122\5n8\2\u0121\u011f\3\2\2\2\u0121\u0120")
        buf.write("\3\2\2\2\u0122\67\3\2\2\2\u0123\u0124\5^\60\2\u0124\u0125")
        buf.write("\5:\36\2\u01259\3\2\2\2\u0126\u0127\7\36\2\2\u0127\u0128")
        buf.write("\5^\60\2\u0128\u0129\5:\36\2\u0129\u012c\3\2\2\2\u012a")
        buf.write("\u012c\3\2\2\2\u012b\u0126\3\2\2\2\u012b\u012a\3\2\2\2")
        buf.write("\u012c;\3\2\2\2\u012d\u012e\7\3\2\2\u012e\u012f\7!\2\2")
        buf.write("\u012f\u0130\5^\60\2\u0130\u0134\7\"\2\2\u0131\u0133\7")
        buf.write("-\2\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2\u0134\u0132")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0137\3\2\2\2\u0136")
        buf.write("\u0134\3\2\2\2\u0137\u0138\5.\30\2\u0138\u0139\5> \2\u0139")
        buf.write("\u013a\5@!\2\u013a=\3\2\2\2\u013b\u013e\5B\"\2\u013c\u013e")
        buf.write("\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013c\3\2\2\2\u013e")
        buf.write("?\3\2\2\2\u013f\u0142\5F$\2\u0140\u0142\3\2\2\2\u0141")
        buf.write("\u013f\3\2\2\2\u0141\u0140\3\2\2\2\u0142A\3\2\2\2\u0143")
        buf.write("\u0144\7\4\2\2\u0144\u0145\7!\2\2\u0145\u0146\5^\60\2")
        buf.write("\u0146\u014a\7\"\2\2\u0147\u0149\7-\2\2\u0148\u0147\3")
        buf.write("\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b")
        buf.write("\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014a\3\2\2\2\u014d")
        buf.write("\u014e\5.\30\2\u014e\u014f\5D#\2\u014fC\3\2\2\2\u0150")
        buf.write("\u0153\5B\"\2\u0151\u0153\3\2\2\2\u0152\u0150\3\2\2\2")
        buf.write("\u0152\u0151\3\2\2\2\u0153E\3\2\2\2\u0154\u0158\7\5\2")
        buf.write("\2\u0155\u0157\7-\2\2\u0156\u0155\3\2\2\2\u0157\u015a")
        buf.write("\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159")
        buf.write("\u015b\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015c\5.\30\2")
        buf.write("\u015cG\3\2\2\2\u015d\u015e\7\6\2\2\u015e\u015f\7*\2\2")
        buf.write("\u015f\u0160\7\7\2\2\u0160\u0161\5J&\2\u0161\u0162\7\b")
        buf.write("\2\2\u0162\u0166\5L\'\2\u0163\u0165\7-\2\2\u0164\u0163")
        buf.write("\3\2\2\2\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0166")
        buf.write("\u0167\3\2\2\2\u0167\u0169\3\2\2\2\u0168\u0166\3\2\2\2")
        buf.write("\u0169\u016a\5.\30\2\u016aI\3\2\2\2\u016b\u016c\5^\60")
        buf.write("\2\u016cK\3\2\2\2\u016d\u016e\5^\60\2\u016eM\3\2\2\2\u016f")
        buf.write("\u0170\7\t\2\2\u0170O\3\2\2\2\u0171\u0172\7\n\2\2\u0172")
        buf.write("Q\3\2\2\2\u0173\u0175\7\13\2\2\u0174\u0176\5^\60\2\u0175")
        buf.write("\u0174\3\2\2\2\u0175\u0176\3\2\2\2\u0176S\3\2\2\2\u0177")
        buf.write("\u0178\7*\2\2\u0178\u0179\7!\2\2\u0179\u017a\5V,\2\u017a")
        buf.write("\u017b\7\"\2\2\u017bU\3\2\2\2\u017c\u017f\5X-\2\u017d")
        buf.write("\u017f\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017d\3\2\2\2")
        buf.write("\u017fW\3\2\2\2\u0180\u0181\5^\60\2\u0181\u0182\5Z.\2")
        buf.write("\u0182Y\3\2\2\2\u0183\u0184\7\36\2\2\u0184\u0185\5^\60")
        buf.write("\2\u0185\u0186\5Z.\2\u0186\u0189\3\2\2\2\u0187\u0189\3")
        buf.write("\2\2\2\u0188\u0183\3\2\2\2\u0188\u0187\3\2\2\2\u0189[")
        buf.write("\3\2\2\2\u018a\u018c\7\f\2\2\u018b\u018d\7-\2\2\u018c")
        buf.write("\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018c\3\2\2\2")
        buf.write("\u018e\u018f\3\2\2\2\u018f\u0193\3\2\2\2\u0190\u0192\5")
        buf.write(".\30\2\u0191\u0190\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191")
        buf.write("\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0196\3\2\2\2\u0195")
        buf.write("\u0193\3\2\2\2\u0196\u0197\7\r\2\2\u0197]\3\2\2\2\u0198")
        buf.write("\u0199\b\60\1\2\u0199\u019a\5`\61\2\u019a\u01a0\3\2\2")
        buf.write("\2\u019b\u019c\f\4\2\2\u019c\u019d\7\33\2\2\u019d\u019f")
        buf.write("\5`\61\2\u019e\u019b\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1_\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a3\u01a4\b\61\1\2\u01a4\u01a5\5b\62")
        buf.write("\2\u01a5\u01ab\3\2\2\2\u01a6\u01a7\f\4\2\2\u01a7\u01a8")
        buf.write("\7\25\2\2\u01a8\u01aa\5b\62\2\u01a9\u01a6\3\2\2\2\u01aa")
        buf.write("\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2")
        buf.write("\u01aca\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01af\b\62\1")
        buf.write("\2\u01af\u01b0\5d\63\2\u01b0\u01b6\3\2\2\2\u01b1\u01b2")
        buf.write("\f\4\2\2\u01b2\u01b3\7\35\2\2\u01b3\u01b5\5d\63\2\u01b4")
        buf.write("\u01b1\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b7\3\2\2\2\u01b7c\3\2\2\2\u01b8\u01b6\3\2\2")
        buf.write("\2\u01b9\u01ba\b\63\1\2\u01ba\u01bb\5f\64\2\u01bb\u01c1")
        buf.write("\3\2\2\2\u01bc\u01bd\f\4\2\2\u01bd\u01be\t\3\2\2\u01be")
        buf.write("\u01c0\5f\64\2\u01bf\u01bc\3\2\2\2\u01c0\u01c3\3\2\2\2")
        buf.write("\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2e\3\2\2")
        buf.write("\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5\b\64\1\2\u01c5\u01c6")
        buf.write("\5h\65\2\u01c6\u01cc\3\2\2\2\u01c7\u01c8\f\4\2\2\u01c8")
        buf.write("\u01c9\t\4\2\2\u01c9\u01cb\5h\65\2\u01ca\u01c7\3\2\2\2")
        buf.write("\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3")
        buf.write("\2\2\2\u01cdg\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d0")
        buf.write("\7\24\2\2\u01d0\u01d3\5j\66\2\u01d1\u01d3\5j\66\2\u01d2")
        buf.write("\u01cf\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3i\3\2\2\2\u01d4")
        buf.write("\u01d5\7\27\2\2\u01d5\u01d8\5l\67\2\u01d6\u01d8\5l\67")
        buf.write("\2\u01d7\u01d4\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8k\3\2")
        buf.write("\2\2\u01d9\u01dd\5\64\33\2\u01da\u01dd\5n8\2\u01db\u01dd")
        buf.write("\5p9\2\u01dc\u01d9\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01db")
        buf.write("\3\2\2\2\u01ddm\3\2\2\2\u01de\u01df\7*\2\2\u01df\u01e0")
        buf.write("\7!\2\2\u01e0\u01e1\5V,\2\u01e1\u01e2\7\"\2\2\u01e2o\3")
        buf.write("\2\2\2\u01e3\u01e9\5\34\17\2\u01e4\u01e5\7!\2\2\u01e5")
        buf.write("\u01e6\5^\60\2\u01e6\u01e7\7\"\2\2\u01e7\u01e9\3\2\2\2")
        buf.write("\u01e8\u01e3\3\2\2\2\u01e8\u01e4\3\2\2\2\u01e9q\3\2\2")
        buf.write("\2\61u{\u0080\u0087\u008c\u0091\u0095\u009f\u00b1\u00b6")
        buf.write("\u00bf\u00c6\u00cb\u00d0\u00df\u00e6\u00f0\u00f6\u00fa")
        buf.write("\u00fe\u0109\u010e\u0110\u0118\u0121\u012b\u0134\u013d")
        buf.write("\u0141\u014a\u0152\u0158\u0166\u0175\u017e\u0188\u018e")
        buf.write("\u0193\u01a0\u01ab\u01b6\u01c1\u01cc\u01d2\u01d7\u01dc")
        buf.write("\u01e8")
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
    RULE_var_declare = 2
    RULE_normaldeclare = 3
    RULE_var_type = 4
    RULE_initialnormal = 5
    RULE_arraydeclare = 6
    RULE_array = 7
    RULE_dimension = 8
    RULE_dimtail = 9
    RULE_initialarray = 10
    RULE_arraylit = 11
    RULE_arraylittail = 12
    RULE_literals = 13
    RULE_vartypedeclare = 14
    RULE_func_declare = 15
    RULE_param_here = 16
    RULE_param_list = 17
    RULE_paratail = 18
    RULE_para = 19
    RULE_bodyhere = 20
    RULE_body = 21
    RULE_statement = 22
    RULE_assignment = 23
    RULE_lhs = 24
    RULE_arrayindex = 25
    RULE_arr_expr = 26
    RULE_cell = 27
    RULE_exprtail = 28
    RULE_ifstm = 29
    RULE_elif_here = 30
    RULE_else_here = 31
    RULE_elifbranch = 32
    RULE_eliftail = 33
    RULE_elsebranch = 34
    RULE_forstm = 35
    RULE_cond_expr = 36
    RULE_update_expr = 37
    RULE_break_stm = 38
    RULE_continue_stm = 39
    RULE_return_stm = 40
    RULE_func_call_stm = 41
    RULE_argumentlist = 42
    RULE_arguments = 43
    RULE_argtail = 44
    RULE_block = 45
    RULE_expr = 46
    RULE_expr1 = 47
    RULE_expr2 = 48
    RULE_expr3 = 49
    RULE_expr4 = 50
    RULE_expr5 = 51
    RULE_expr6 = 52
    RULE_expr7 = 53
    RULE_func_call_expr = 54
    RULE_operand = 55

    ruleNames =  [ "program", "declaration", "var_declare", "normaldeclare", 
                   "var_type", "initialnormal", "arraydeclare", "array", 
                   "dimension", "dimtail", "initialarray", "arraylit", "arraylittail", 
                   "literals", "vartypedeclare", "func_declare", "param_here", 
                   "param_list", "paratail", "para", "bodyhere", "body", 
                   "statement", "assignment", "lhs", "arrayindex", "arr_expr", 
                   "cell", "exprtail", "ifstm", "elif_here", "else_here", 
                   "elifbranch", "eliftail", "elsebranch", "forstm", "cond_expr", 
                   "update_expr", "break_stm", "continue_stm", "return_stm", 
                   "func_call_stm", "argumentlist", "arguments", "argtail", 
                   "block", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "func_call_expr", "operand" ]

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

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DeclarationContext,i)


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
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 112
                self.match(ZCodeParser.NL)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 118
                self.declaration()
                self.state = 121 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.BOOL_TYPE) | (1 << ZCodeParser.NUMBER_TYPE) | (1 << ZCodeParser.STR_TYPE) | (1 << ZCodeParser.DYNTYPE) | (1 << ZCodeParser.VARTYPE) | (1 << ZCodeParser.FUNCTYPE))) != 0)):
                    break

            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 123
                self.match(ZCodeParser.NL)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
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

        def var_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declareContext,0)


        def func_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declareContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

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
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.STR_TYPE, ZCodeParser.DYNTYPE, ZCodeParser.VARTYPE]:
                self.state = 131
                self.var_declare()
                pass
            elif token in [ZCodeParser.FUNCTYPE]:
                self.state = 132
                self.func_declare()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 136 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 135
                    self.match(ZCodeParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 138 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self.enterRule(localctx, 4, self.RULE_var_declare)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.normaldeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.arraydeclare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_normaldeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormaldeclare" ):
                return visitor.visitNormaldeclare(self)
            else:
                return visitor.visitChildren(self)




    def normaldeclare(self):

        localctx = ZCodeParser.NormaldeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_normaldeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.STR_TYPE]:
                self.state = 145
                self.var_type()
                pass
            elif token in [ZCodeParser.DYNTYPE]:
                self.state = 146
                self.match(ZCodeParser.DYNTYPE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 149
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 150
            self.initialnormal()
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
        self.enterRule(localctx, 8, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
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

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_initialnormal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialnormal" ):
                return visitor.visitInitialnormal(self)
            else:
                return visitor.visitChildren(self)




    def initialnormal(self):

        localctx = ZCodeParser.InitialnormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_initialnormal)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(ZCodeParser.ASSIGN)
                self.state = 155
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydeclare" ):
                return visitor.visitArraydeclare(self)
            else:
                return visitor.visitChildren(self)




    def arraydeclare(self):

        localctx = ZCodeParser.ArraydeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arraydeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.var_type()
            self.state = 160
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 161
            self.array()
            self.state = 162
            self.initialarray()
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
        self.enterRule(localctx, 14, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(ZCodeParser.LP)
            self.state = 165
            self.dimension()
            self.state = 166
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
        self.enterRule(localctx, 16, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ZCodeParser.NUMLIT)
            self.state = 169
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
        self.enterRule(localctx, 18, self.RULE_dimtail)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(ZCodeParser.CM)
                self.state = 172
                self.match(ZCodeParser.NUMLIT)
                self.state = 173
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
        self.enterRule(localctx, 20, self.RULE_initialarray)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(ZCodeParser.ASSIGN)
                self.state = 178
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
        self.enterRule(localctx, 22, self.RULE_arraylit)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(ZCodeParser.LP)
                self.state = 183
                self.literals()
                self.state = 184
                self.arraylittail()
                self.state = 185
                self.match(ZCodeParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(ZCodeParser.LP)
                self.state = 188
                self.match(ZCodeParser.RP)
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
        self.enterRule(localctx, 24, self.RULE_arraylittail)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(ZCodeParser.CM)
                self.state = 192
                self.literals()
                self.state = 193
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
        self.enterRule(localctx, 26, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.arraylit()
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [ZCodeParser.SUBTR, ZCodeParser.NUMLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.SUBTR:
                    self.state = 200
                    self.match(ZCodeParser.SUBTR)


                self.state = 203
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.BOOLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 205
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


    class VartypedeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARTYPE(self):
            return self.getToken(ZCodeParser.VARTYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


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
            self.state = 208
            self.match(ZCodeParser.VARTYPE)
            self.state = 209
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 210
            self.match(ZCodeParser.ASSIGN)
            self.state = 211
            self.expr(0)
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

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def param_here(self):
            return self.getTypedRuleContext(ZCodeParser.Param_hereContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def bodyhere(self):
            return self.getTypedRuleContext(ZCodeParser.BodyhereContext,0)


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
            self.state = 213
            self.match(ZCodeParser.FUNCTYPE)
            self.state = 214
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 215
            self.match(ZCodeParser.LB)
            self.state = 216
            self.param_here()
            self.state = 217
            self.match(ZCodeParser.RB)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 218
                    self.match(ZCodeParser.NL) 
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 224
            self.bodyhere()
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
        self.enterRule(localctx, 32, self.RULE_param_here)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.STR_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
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
        self.enterRule(localctx, 34, self.RULE_param_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.para()
            self.state = 231
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
        self.enterRule(localctx, 36, self.RULE_paratail)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(ZCodeParser.CM)
                self.state = 234
                self.para()
                self.state = 235
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

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = ZCodeParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.var_type()
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 241
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 242
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 243
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyhereContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_bodyhere

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyhere" ):
                return visitor.visitBodyhere(self)
            else:
                return visitor.visitChildren(self)




    def bodyhere(self):

        localctx = ZCodeParser.BodyhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_bodyhere)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURNOP, ZCodeParser.BEGINOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.body()
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
        self.enterRule(localctx, 42, self.RULE_body)
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURNOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.return_stm()
                pass
            elif token in [ZCodeParser.BEGINOP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.block()
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

        def ifstm(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmContext,0)


        def forstm(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmContext,0)


        def var_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declareContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ZCodeParser.AssignmentContext,0)


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


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IFOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.ifstm()
                pass
            elif token in [ZCodeParser.FOROP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.forstm()
                pass
            elif token in [ZCodeParser.BREAKOP, ZCodeParser.CONTOP, ZCodeParser.RETURNOP, ZCodeParser.BEGINOP, ZCodeParser.BOOL_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.STR_TYPE, ZCodeParser.DYNTYPE, ZCodeParser.VARTYPE, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 263
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 256
                    self.var_declare()
                    pass

                elif la_ == 2:
                    self.state = 257
                    self.assignment()
                    pass

                elif la_ == 3:
                    self.state = 258
                    self.break_stm()
                    pass

                elif la_ == 4:
                    self.state = 259
                    self.continue_stm()
                    pass

                elif la_ == 5:
                    self.state = 260
                    self.return_stm()
                    pass

                elif la_ == 6:
                    self.state = 261
                    self.func_call_stm()
                    pass

                elif la_ == 7:
                    self.state = 262
                    self.block()
                    pass


                self.state = 266 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 265
                    self.match(ZCodeParser.NL)
                    self.state = 268 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

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


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ZCodeParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.lhs()
            self.state = 273
            self.match(ZCodeParser.ASSIGN)
            self.state = 274
            self.expr(0)
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

        def arrayindex(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayindexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_lhs)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.arrayindex()
                pass


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

        def arr_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_exprContext,0)


        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def cell(self):
            return self.getTypedRuleContext(ZCodeParser.CellContext,0)


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
        self.enterRule(localctx, 50, self.RULE_arrayindex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.arr_expr()
            self.state = 281
            self.match(ZCodeParser.LP)
            self.state = 282
            self.cell()
            self.state = 283
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def func_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_expr" ):
                return visitor.visitArr_expr(self)
            else:
                return visitor.visitChildren(self)




    def arr_expr(self):

        localctx = ZCodeParser.Arr_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arr_expr)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.func_call_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def exprtail(self):
            return self.getTypedRuleContext(ZCodeParser.ExprtailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_cell

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCell" ):
                return visitor.visitCell(self)
            else:
                return visitor.visitChildren(self)




    def cell(self):

        localctx = ZCodeParser.CellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_cell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.expr(0)
            self.state = 290
            self.exprtail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprtailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def exprtail(self):
            return self.getTypedRuleContext(ZCodeParser.ExprtailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprtail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprtail" ):
                return visitor.visitExprtail(self)
            else:
                return visitor.visitChildren(self)




    def exprtail(self):

        localctx = ZCodeParser.ExprtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exprtail)
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(ZCodeParser.CM)
                self.state = 293
                self.expr(0)
                self.state = 294
                self.exprtail()
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

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def elif_here(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_hereContext,0)


        def else_here(self):
            return self.getTypedRuleContext(ZCodeParser.Else_hereContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstm" ):
                return visitor.visitIfstm(self)
            else:
                return visitor.visitChildren(self)




    def ifstm(self):

        localctx = ZCodeParser.IfstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_ifstm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(ZCodeParser.IFOP)
            self.state = 300
            self.match(ZCodeParser.LB)
            self.state = 301
            self.expr(0)
            self.state = 302
            self.match(ZCodeParser.RB)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 303
                self.match(ZCodeParser.NL)
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 309
            self.statement()
            self.state = 310
            self.elif_here()
            self.state = 311
            self.else_here()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_hereContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifbranch(self):
            return self.getTypedRuleContext(ZCodeParser.ElifbranchContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_here

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_here" ):
                return visitor.visitElif_here(self)
            else:
                return visitor.visitChildren(self)




    def elif_here(self):

        localctx = ZCodeParser.Elif_hereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_elif_here)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.elifbranch()
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


    class Else_hereContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elsebranch(self):
            return self.getTypedRuleContext(ZCodeParser.ElsebranchContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_here

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_here" ):
                return visitor.visitElse_here(self)
            else:
                return visitor.visitChildren(self)




    def else_here(self):

        localctx = ZCodeParser.Else_hereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_else_here)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.elsebranch()
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


    class ElifbranchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIFOP(self):
            return self.getToken(ZCodeParser.ELIFOP, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def eliftail(self):
            return self.getTypedRuleContext(ZCodeParser.EliftailContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elifbranch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifbranch" ):
                return visitor.visitElifbranch(self)
            else:
                return visitor.visitChildren(self)




    def elifbranch(self):

        localctx = ZCodeParser.ElifbranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_elifbranch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(ZCodeParser.ELIFOP)
            self.state = 322
            self.match(ZCodeParser.LB)
            self.state = 323
            self.expr(0)
            self.state = 324
            self.match(ZCodeParser.RB)
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 325
                self.match(ZCodeParser.NL)
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 331
            self.statement()
            self.state = 332
            self.eliftail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliftailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifbranch(self):
            return self.getTypedRuleContext(ZCodeParser.ElifbranchContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_eliftail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliftail" ):
                return visitor.visitEliftail(self)
            else:
                return visitor.visitChildren(self)




    def eliftail(self):

        localctx = ZCodeParser.EliftailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_eliftail)
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.elifbranch()
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
        self.enterRule(localctx, 68, self.RULE_elsebranch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(ZCodeParser.ELSEOP)
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 339
                self.match(ZCodeParser.NL)
                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 345
            self.statement()
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

        def cond_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Cond_exprContext,0)


        def BYOP(self):
            return self.getToken(ZCodeParser.BYOP, 0)

        def update_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Update_exprContext,0)


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
        self.enterRule(localctx, 70, self.RULE_forstm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(ZCodeParser.FOROP)
            self.state = 348
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 349
            self.match(ZCodeParser.UNTILOP)
            self.state = 350
            self.cond_expr()
            self.state = 351
            self.match(ZCodeParser.BYOP)
            self.state = 352
            self.update_expr()
            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 353
                self.match(ZCodeParser.NL)
                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 359
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_cond_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond_expr" ):
                return visitor.visitCond_expr(self)
            else:
                return visitor.visitChildren(self)




    def cond_expr(self):

        localctx = ZCodeParser.Cond_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_cond_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_update_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_expr" ):
                return visitor.visitUpdate_expr(self)
            else:
                return visitor.visitChildren(self)




    def update_expr(self):

        localctx = ZCodeParser.Update_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_update_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.expr(0)
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stm" ):
                return visitor.visitBreak_stm(self)
            else:
                return visitor.visitChildren(self)




    def break_stm(self):

        localctx = ZCodeParser.Break_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(ZCodeParser.BREAKOP)
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stm" ):
                return visitor.visitContinue_stm(self)
            else:
                return visitor.visitChildren(self)




    def continue_stm(self):

        localctx = ZCodeParser.Continue_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(ZCodeParser.CONTOP)
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = ZCodeParser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_return_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(ZCodeParser.RETURNOP)
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOTOP) | (1 << ZCodeParser.SUBTR) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 370
                self.expr(0)


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

        def argumentlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentlistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stm" ):
                return visitor.visitFunc_call_stm(self)
            else:
                return visitor.visitChildren(self)




    def func_call_stm(self):

        localctx = ZCodeParser.Func_call_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_func_call_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 374
            self.match(ZCodeParser.LB)
            self.state = 375
            self.argumentlist()
            self.state = 376
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arguments(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argumentlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentlist" ):
                return visitor.visitArgumentlist(self)
            else:
                return visitor.visitChildren(self)




    def argumentlist(self):

        localctx = ZCodeParser.ArgumentlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_argumentlist)
        try:
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOTOP, ZCodeParser.SUBTR, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NUMLIT, ZCodeParser.BOOLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.arguments()
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


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


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
        self.enterRule(localctx, 86, self.RULE_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.expr(0)
            self.state = 383
            self.argtail()
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

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


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
        self.enterRule(localctx, 88, self.RULE_argtail)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.match(ZCodeParser.CM)
                self.state = 386
                self.expr(0)
                self.state = 387
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
        self.enterRule(localctx, 90, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(ZCodeParser.BEGINOP)
            self.state = 394 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 393
                self.match(ZCodeParser.NL)
                self.state = 396 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NL):
                    break

            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.IFOP) | (1 << ZCodeParser.FOROP) | (1 << ZCodeParser.BREAKOP) | (1 << ZCodeParser.CONTOP) | (1 << ZCodeParser.RETURNOP) | (1 << ZCodeParser.BEGINOP) | (1 << ZCodeParser.BOOL_TYPE) | (1 << ZCodeParser.NUMBER_TYPE) | (1 << ZCodeParser.STR_TYPE) | (1 << ZCodeParser.DYNTYPE) | (1 << ZCodeParser.VARTYPE) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 398
                self.statement()
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 404
            self.match(ZCodeParser.ENDOP)
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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 414
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 409
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 410
                    self.match(ZCodeParser.CONCAT)
                    self.state = 411
                    self.expr1(0) 
                self.state = 416
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 420
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 421
                    self.match(ZCodeParser.ANDOR)
                    self.state = 422
                    self.expr2(0) 
                self.state = 427
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 436
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 431
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 432
                    self.match(ZCodeParser.RELATION)
                    self.state = 433
                    self.expr3(0) 
                self.state = 438
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 447
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 442
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 443
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADDOP or _la==ZCodeParser.SUBTR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 444
                    self.expr4(0) 
                self.state = 449
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 458
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 453
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 454
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULOP) | (1 << ZCodeParser.DIVOP) | (1 << ZCodeParser.MODOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 455
                    self.expr5() 
                self.state = 460
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        self.enterRule(localctx, 102, self.RULE_expr5)
        try:
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.match(ZCodeParser.NOTOP)
                self.state = 462
                self.expr6()
                pass
            elif token in [ZCodeParser.SUBTR, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NUMLIT, ZCodeParser.BOOLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
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
        self.enterRule(localctx, 104, self.RULE_expr6)
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.match(ZCodeParser.SUBTR)
                self.state = 467
                self.expr7()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
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

        def arrayindex(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayindexContext,0)


        def func_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_exprContext,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_expr7)
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.arrayindex()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
                self.func_call_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 473
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentlistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_expr" ):
                return visitor.visitFunc_call_expr(self)
            else:
                return visitor.visitChildren(self)




    def func_call_expr(self):

        localctx = ZCodeParser.Func_call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_func_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 477
            self.match(ZCodeParser.LB)
            self.state = 478
            self.argumentlist()
            self.state = 479
            self.match(ZCodeParser.RB)
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
        self.enterRule(localctx, 110, self.RULE_operand)
        try:
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUBTR, ZCodeParser.LP, ZCodeParser.NUMLIT, ZCodeParser.BOOLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.literals()
                pass
            elif token in [ZCodeParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
                self.match(ZCodeParser.LB)
                self.state = 483
                self.expr(0)
                self.state = 484
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[46] = self.expr_sempred
        self._predicates[47] = self.expr1_sempred
        self._predicates[48] = self.expr2_sempred
        self._predicates[49] = self.expr3_sempred
        self._predicates[50] = self.expr4_sempred
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
         




