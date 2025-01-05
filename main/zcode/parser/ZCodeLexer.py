# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\60")
        buf.write("\u0172\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u00c7\n\24\3")
        buf.write("\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\5\34\u00e4\n\34\3\35\3\35\3")
        buf.write("\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3\"\5\"\u00f4")
        buf.write("\n\"\3#\6#\u00f7\n#\r#\16#\u00f8\3$\6$\u00fc\n$\r$\16")
        buf.write("$\u00fd\3$\5$\u0101\n$\3$\7$\u0104\n$\f$\16$\u0107\13")
        buf.write("$\3%\6%\u010a\n%\r%\16%\u010b\3%\3%\5%\u0110\n%\3%\6%")
        buf.write("\u0113\n%\r%\16%\u0114\3&\6&\u0118\n&\r&\16&\u0119\3&")
        buf.write("\3&\6&\u011e\n&\r&\16&\u011f\3&\3&\5&\u0124\n&\3&\6&\u0127")
        buf.write("\n&\r&\16&\u0128\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5")
        buf.write("\'\u0134\n\'\3(\3(\3(\3(\3(\7(\u013b\n(\f(\16(\u013e\13")
        buf.write("(\3(\3(\3(\3)\3)\7)\u0145\n)\f)\16)\u0148\13)\3*\3*\3")
        buf.write("*\3*\7*\u014e\n*\f*\16*\u0151\13*\3*\3*\3+\6+\u0156\n")
        buf.write("+\r+\16+\u0157\3+\3+\3,\3,\3,\3,\5,\u0160\n,\3-\3-\3-")
        buf.write("\3.\3.\3.\3.\7.\u0169\n.\f.\16.\u016c\13.\3.\3.\3/\3/")
        buf.write("\3/\2\2\60\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60\3\2\r\4\2>>@@\3\2\62;\4\2")
        buf.write("GGgg\4\2--//\5\2\f\f\17\17$$\6\2\n\13\16\16))^^\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\3\2\f\f\5\2\n\13\16\16\"\"\6\2\n\13")
        buf.write("\16\16\"#%\u0080\2\u0190\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\3_\3\2\2\2\5b\3\2\2\2\7g")
        buf.write("\3\2\2\2\tl\3\2\2\2\13p\3\2\2\2\rv\3\2\2\2\17y\3\2\2\2")
        buf.write("\21\177\3\2\2\2\23\u0088\3\2\2\2\25\u008f\3\2\2\2\27\u0095")
        buf.write("\3\2\2\2\31\u0099\3\2\2\2\33\u009e\3\2\2\2\35\u00a5\3")
        buf.write("\2\2\2\37\u00ac\3\2\2\2!\u00b4\3\2\2\2#\u00b8\3\2\2\2")
        buf.write("%\u00bd\3\2\2\2\'\u00c6\3\2\2\2)\u00c8\3\2\2\2+\u00ca")
        buf.write("\3\2\2\2-\u00cc\3\2\2\2/\u00ce\3\2\2\2\61\u00d0\3\2\2")
        buf.write("\2\63\u00d2\3\2\2\2\65\u00d6\3\2\2\2\67\u00e3\3\2\2\2")
        buf.write("9\u00e5\3\2\2\2;\u00e7\3\2\2\2=\u00e9\3\2\2\2?\u00eb\3")
        buf.write("\2\2\2A\u00ed\3\2\2\2C\u00f3\3\2\2\2E\u00f6\3\2\2\2G\u00fb")
        buf.write("\3\2\2\2I\u0109\3\2\2\2K\u0117\3\2\2\2M\u0133\3\2\2\2")
        buf.write("O\u0135\3\2\2\2Q\u0142\3\2\2\2S\u0149\3\2\2\2U\u0155\3")
        buf.write("\2\2\2W\u015f\3\2\2\2Y\u0161\3\2\2\2[\u0164\3\2\2\2]\u016f")
        buf.write("\3\2\2\2_`\7k\2\2`a\7h\2\2a\4\3\2\2\2bc\7g\2\2cd\7n\2")
        buf.write("\2de\7k\2\2ef\7h\2\2f\6\3\2\2\2gh\7g\2\2hi\7n\2\2ij\7")
        buf.write("u\2\2jk\7g\2\2k\b\3\2\2\2lm\7h\2\2mn\7q\2\2no\7t\2\2o")
        buf.write("\n\3\2\2\2pq\7w\2\2qr\7p\2\2rs\7v\2\2st\7k\2\2tu\7n\2")
        buf.write("\2u\f\3\2\2\2vw\7d\2\2wx\7{\2\2x\16\3\2\2\2yz\7d\2\2z")
        buf.write("{\7t\2\2{|\7g\2\2|}\7c\2\2}~\7m\2\2~\20\3\2\2\2\177\u0080")
        buf.write("\7e\2\2\u0080\u0081\7q\2\2\u0081\u0082\7p\2\2\u0082\u0083")
        buf.write("\7v\2\2\u0083\u0084\7k\2\2\u0084\u0085\7p\2\2\u0085\u0086")
        buf.write("\7w\2\2\u0086\u0087\7g\2\2\u0087\22\3\2\2\2\u0088\u0089")
        buf.write("\7t\2\2\u0089\u008a\7g\2\2\u008a\u008b\7v\2\2\u008b\u008c")
        buf.write("\7w\2\2\u008c\u008d\7t\2\2\u008d\u008e\7p\2\2\u008e\24")
        buf.write("\3\2\2\2\u008f\u0090\7d\2\2\u0090\u0091\7g\2\2\u0091\u0092")
        buf.write("\7i\2\2\u0092\u0093\7k\2\2\u0093\u0094\7p\2\2\u0094\26")
        buf.write("\3\2\2\2\u0095\u0096\7g\2\2\u0096\u0097\7p\2\2\u0097\u0098")
        buf.write("\7f\2\2\u0098\30\3\2\2\2\u0099\u009a\7d\2\2\u009a\u009b")
        buf.write("\7q\2\2\u009b\u009c\7q\2\2\u009c\u009d\7n\2\2\u009d\32")
        buf.write("\3\2\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7w\2\2\u00a0\u00a1")
        buf.write("\7o\2\2\u00a1\u00a2\7d\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\34\3\2\2\2\u00a5\u00a6\7u\2\2\u00a6\u00a7")
        buf.write("\7v\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa")
        buf.write("\7p\2\2\u00aa\u00ab\7i\2\2\u00ab\36\3\2\2\2\u00ac\u00ad")
        buf.write("\7f\2\2\u00ad\u00ae\7{\2\2\u00ae\u00af\7p\2\2\u00af\u00b0")
        buf.write("\7c\2\2\u00b0\u00b1\7o\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3")
        buf.write("\7e\2\2\u00b3 \3\2\2\2\u00b4\u00b5\7x\2\2\u00b5\u00b6")
        buf.write("\7c\2\2\u00b6\u00b7\7t\2\2\u00b7\"\3\2\2\2\u00b8\u00b9")
        buf.write("\7h\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc")
        buf.write("\7e\2\2\u00bc$\3\2\2\2\u00bd\u00be\7p\2\2\u00be\u00bf")
        buf.write("\7q\2\2\u00bf\u00c0\7v\2\2\u00c0&\3\2\2\2\u00c1\u00c2")
        buf.write("\7c\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c7\7f\2\2\u00c4\u00c5")
        buf.write("\7q\2\2\u00c5\u00c7\7t\2\2\u00c6\u00c1\3\2\2\2\u00c6\u00c4")
        buf.write("\3\2\2\2\u00c7(\3\2\2\2\u00c8\u00c9\7-\2\2\u00c9*\3\2")
        buf.write("\2\2\u00ca\u00cb\7/\2\2\u00cb,\3\2\2\2\u00cc\u00cd\7,")
        buf.write("\2\2\u00cd.\3\2\2\2\u00ce\u00cf\7\61\2\2\u00cf\60\3\2")
        buf.write("\2\2\u00d0\u00d1\7\'\2\2\u00d1\62\3\2\2\2\u00d2\u00d3")
        buf.write("\7\60\2\2\u00d3\u00d4\7\60\2\2\u00d4\u00d5\7\60\2\2\u00d5")
        buf.write("\64\3\2\2\2\u00d6\u00d7\7>\2\2\u00d7\u00d8\7/\2\2\u00d8")
        buf.write("\66\3\2\2\2\u00d9\u00da\7?\2\2\u00da\u00e4\7?\2\2\u00db")
        buf.write("\u00dc\7@\2\2\u00dc\u00e4\7?\2\2\u00dd\u00de\7>\2\2\u00de")
        buf.write("\u00e4\7?\2\2\u00df\u00e4\t\2\2\2\u00e0\u00e1\7#\2\2\u00e1")
        buf.write("\u00e4\7?\2\2\u00e2\u00e4\7?\2\2\u00e3\u00d9\3\2\2\2\u00e3")
        buf.write("\u00db\3\2\2\2\u00e3\u00dd\3\2\2\2\u00e3\u00df\3\2\2\2")
        buf.write("\u00e3\u00e0\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e48\3\2\2")
        buf.write("\2\u00e5\u00e6\7.\2\2\u00e6:\3\2\2\2\u00e7\u00e8\7]\2")
        buf.write("\2\u00e8<\3\2\2\2\u00e9\u00ea\7_\2\2\u00ea>\3\2\2\2\u00eb")
        buf.write("\u00ec\7*\2\2\u00ec@\3\2\2\2\u00ed\u00ee\7+\2\2\u00ee")
        buf.write("B\3\2\2\2\u00ef\u00f4\5E#\2\u00f0\u00f4\5G$\2\u00f1\u00f4")
        buf.write("\5I%\2\u00f2\u00f4\5K&\2\u00f3\u00ef\3\2\2\2\u00f3\u00f0")
        buf.write("\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4")
        buf.write("D\3\2\2\2\u00f5\u00f7\t\3\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("\u00f8\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9F\3\2\2\2\u00fa\u00fc\t\3\2\2\u00fb\u00fa\3\2\2")
        buf.write("\2\u00fc\u00fd\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe")
        buf.write("\3\2\2\2\u00fe\u0100\3\2\2\2\u00ff\u0101\7\60\2\2\u0100")
        buf.write("\u00ff\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0105\3\2\2\2")
        buf.write("\u0102\u0104\t\3\2\2\u0103\u0102\3\2\2\2\u0104\u0107\3")
        buf.write("\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106H")
        buf.write("\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u010a\t\3\2\2\u0109")
        buf.write("\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u0109\3\2\2\2")
        buf.write("\u010b\u010c\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010f\t")
        buf.write("\4\2\2\u010e\u0110\t\5\2\2\u010f\u010e\3\2\2\2\u010f\u0110")
        buf.write("\3\2\2\2\u0110\u0112\3\2\2\2\u0111\u0113\t\3\2\2\u0112")
        buf.write("\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0112\3\2\2\2")
        buf.write("\u0114\u0115\3\2\2\2\u0115J\3\2\2\2\u0116\u0118\t\3\2")
        buf.write("\2\u0117\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u0117")
        buf.write("\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\3\2\2\2\u011b")
        buf.write("\u011d\7\60\2\2\u011c\u011e\t\3\2\2\u011d\u011c\3\2\2")
        buf.write("\2\u011e\u011f\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0123\t\4\2\2\u0122")
        buf.write("\u0124\t\5\2\2\u0123\u0122\3\2\2\2\u0123\u0124\3\2\2\2")
        buf.write("\u0124\u0126\3\2\2\2\u0125\u0127\t\3\2\2\u0126\u0125\3")
        buf.write("\2\2\2\u0127\u0128\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129")
        buf.write("\3\2\2\2\u0129L\3\2\2\2\u012a\u012b\7v\2\2\u012b\u012c")
        buf.write("\7t\2\2\u012c\u012d\7w\2\2\u012d\u0134\7g\2\2\u012e\u012f")
        buf.write("\7h\2\2\u012f\u0130\7c\2\2\u0130\u0131\7n\2\2\u0131\u0132")
        buf.write("\7u\2\2\u0132\u0134\7g\2\2\u0133\u012a\3\2\2\2\u0133\u012e")
        buf.write("\3\2\2\2\u0134N\3\2\2\2\u0135\u013c\7$\2\2\u0136\u013b")
        buf.write("\n\6\2\2\u0137\u013b\t\7\2\2\u0138\u0139\7)\2\2\u0139")
        buf.write("\u013b\7$\2\2\u013a\u0136\3\2\2\2\u013a\u0137\3\2\2\2")
        buf.write("\u013a\u0138\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3")
        buf.write("\2\2\2\u013c\u013d\3\2\2\2\u013d\u013f\3\2\2\2\u013e\u013c")
        buf.write("\3\2\2\2\u013f\u0140\7$\2\2\u0140\u0141\b(\2\2\u0141P")
        buf.write("\3\2\2\2\u0142\u0146\t\b\2\2\u0143\u0145\t\t\2\2\u0144")
        buf.write("\u0143\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2")
        buf.write("\u0146\u0147\3\2\2\2\u0147R\3\2\2\2\u0148\u0146\3\2\2")
        buf.write("\2\u0149\u014a\7%\2\2\u014a\u014b\7%\2\2\u014b\u014f\3")
        buf.write("\2\2\2\u014c\u014e\n\n\2\2\u014d\u014c\3\2\2\2\u014e\u0151")
        buf.write("\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150")
        buf.write("\u0152\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0153\b*\3\2")
        buf.write("\u0153T\3\2\2\2\u0154\u0156\t\13\2\2\u0155\u0154\3\2\2")
        buf.write("\2\u0156\u0157\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158")
        buf.write("\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\b+\3\2\u015a")
        buf.write("V\3\2\2\2\u015b\u0160\7\f\2\2\u015c\u015d\7\17\2\2\u015d")
        buf.write("\u0160\7\f\2\2\u015e\u0160\7\17\2\2\u015f\u015b\3\2\2")
        buf.write("\2\u015f\u015c\3\2\2\2\u015f\u015e\3\2\2\2\u0160X\3\2")
        buf.write("\2\2\u0161\u0162\13\2\2\2\u0162\u0163\b-\4\2\u0163Z\3")
        buf.write("\2\2\2\u0164\u016a\7$\2\2\u0165\u0169\t\f\2\2\u0166\u0167")
        buf.write("\7)\2\2\u0167\u0169\7$\2\2\u0168\u0165\3\2\2\2\u0168\u0166")
        buf.write("\3\2\2\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u016d\3\2\2\2\u016c\u016a\3\2\2\2")
        buf.write("\u016d\u016e\b.\5\2\u016e\\\3\2\2\2\u016f\u0170\13\2\2")
        buf.write("\2\u0170\u0171\b/\6\2\u0171^\3\2\2\2\32\2\u00c6\u00e3")
        buf.write("\u00f3\u00f8\u00fd\u0100\u0105\u010b\u010f\u0114\u0119")
        buf.write("\u011f\u0123\u0128\u0133\u013a\u013c\u0146\u014f\u0157")
        buf.write("\u015f\u0168\u016a\7\3(\2\b\2\2\3-\3\3.\4\3/\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IFOP = 1
    ELIFOP = 2
    ELSEOP = 3
    FOROP = 4
    UNTILOP = 5
    BYOP = 6
    BREAKOP = 7
    CONTOP = 8
    RETURNOP = 9
    BEGINOP = 10
    ENDOP = 11
    BOOL_TYPE = 12
    NUMBER_TYPE = 13
    STR_TYPE = 14
    DYNTYPE = 15
    VARTYPE = 16
    FUNCTYPE = 17
    NOTOP = 18
    ANDOR = 19
    ADDOP = 20
    SUBTR = 21
    MULOP = 22
    DIVOP = 23
    MODOP = 24
    CONCAT = 25
    ASSIGN = 26
    RELATION = 27
    CM = 28
    LP = 29
    RP = 30
    LB = 31
    RB = 32
    NUMLIT = 33
    NUM1 = 34
    NUM2 = 35
    NUM3 = 36
    NUM4 = 37
    BOOLIT = 38
    STRINGLIT = 39
    IDENTIFIER = 40
    COMMENT = 41
    WS = 42
    NL = 43
    ERROR_CHAR = 44
    UNCLOSE_STRING = 45
    ILLEGAL_ESCAPE = 46

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'elif'", "'else'", "'for'", "'until'", "'by'", "'break'", 
            "'continue'", "'return'", "'begin'", "'end'", "'bool'", "'number'", 
            "'string'", "'dynamic'", "'var'", "'func'", "'not'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'...'", "'<-'", "','", "'['", "']'", 
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "IFOP", "ELIFOP", "ELSEOP", "FOROP", "UNTILOP", "BYOP", "BREAKOP", 
            "CONTOP", "RETURNOP", "BEGINOP", "ENDOP", "BOOL_TYPE", "NUMBER_TYPE", 
            "STR_TYPE", "DYNTYPE", "VARTYPE", "FUNCTYPE", "NOTOP", "ANDOR", 
            "ADDOP", "SUBTR", "MULOP", "DIVOP", "MODOP", "CONCAT", "ASSIGN", 
            "RELATION", "CM", "LP", "RP", "LB", "RB", "NUMLIT", "NUM1", 
            "NUM2", "NUM3", "NUM4", "BOOLIT", "STRINGLIT", "IDENTIFIER", 
            "COMMENT", "WS", "NL", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IFOP", "ELIFOP", "ELSEOP", "FOROP", "UNTILOP", "BYOP", 
                  "BREAKOP", "CONTOP", "RETURNOP", "BEGINOP", "ENDOP", "BOOL_TYPE", 
                  "NUMBER_TYPE", "STR_TYPE", "DYNTYPE", "VARTYPE", "FUNCTYPE", 
                  "NOTOP", "ANDOR", "ADDOP", "SUBTR", "MULOP", "DIVOP", 
                  "MODOP", "CONCAT", "ASSIGN", "RELATION", "CM", "LP", "RP", 
                  "LB", "RB", "NUMLIT", "NUM1", "NUM2", "NUM3", "NUM4", 
                  "BOOLIT", "STRINGLIT", "IDENTIFIER", "COMMENT", "WS", 
                  "NL", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[38] = self.STRINGLIT_action 
            actions[43] = self.ERROR_CHAR_action 
            actions[44] = self.UNCLOSE_STRING_action 
            actions[45] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

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
            		
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text)
     


