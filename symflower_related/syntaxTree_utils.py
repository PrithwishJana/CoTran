"""
This file contains util functions for Syntax Tree
"""
#from pygments.lexers.c_cpp import CppLexer
from pygments.lexers.jvm import JavaLexer
#from pygments.lexers import InputStream
#from pygments.lexers.dotnet import CSharpLexer
import javalang
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
from LexersParsers.java import JavaParser, JavaLexer

import antlr4
from antlr4 import *

#https://stackoverflow.com/questions/60617218/parsing-some-java-code-with-python-using-antlr
#https://github.com/antlr/antlr4/blob/master/doc/python-target.md

def getJavaAncestorMask(code):
    root_folder = "./AVATAR_data/third_party"
    jProcessor = JavaProcessor(root_folder=root_folder)

    decodedfile = jProcessor.detokenize_code(code)

    lexer = JavaLexer.JavaLexer(antlr4.InputStream(decodedfile))

    '''
    tokens = lexer.getAllTokens()
    for t in tokens:
        print(t) #t.text, t.type
    '''
    
    stream = antlr4.CommonTokenStream(lexer)
    parser = JavaParser.JavaParser(stream)
    tree = parser.compilationUnit()
    print(tree.toStringTree(recog=parser))
    print()

    #walker = antlr4.ParseTreeWalker()
    #walker.walk(tree)
    #print (tree.findAllTokenNodes())
    #print (getAncestors(tree))
    #stream = antlr4.CommonTokenStream(lexer)
    #parser = Java8Parser.Java8Parser(stream)
    #tree = parser.compilationUnit()
    #print(tree.toStringTree(recog=parser))
    tree = 0

    '''
    tokens = list(javalang.tokenizer.tokenize(decodedfile))
    #for tok in tokens:
    #    print (tok)
    parser = javalang.parser.Parser(tokens)
    #for xx in parser:
    #    print (xx)
    tree = parser.parse()
    #for path, node in tree:
    #    print (node.getLineNumber(0), "\n")
    #tree = javalang.parse.parse(decodedfile)
    '''
    return tree

def getPyAncestorMask(code):
    root_folder = "./AVATAR_data/third_party"
    pyProcessor = PythonProcessor(root_folder=root_folder)

    decodedfile = pyProcessor.detokenize_code(code)



if __name__ == "__main__":
    javaOneLineCode1 = '''import java . io . IOException ; import java . io . InputStream ; import java . io . PrintWriter ; import java . util . * ; public class Main { public static void main ( String [ ] args ) { PrintWriter out = new PrintWriter ( System . out ) ; InputStreamScanner in = new InputStreamScanner ( System . in ) ; new Main ( ) . solve ( in , out ) ; out . flush ( ) ; } private void solve ( InputStreamScanner in , PrintWriter out ) { int a = in . nextInt ( ) ; List < Integer > c = Arrays . asList ( 3 , 5 , 7 ) ; out . println ( c . contains ( a ) ? " YES " : " NO " ) ; } static class InputStreamScanner { private InputStream in ; private byte [ ] buf = new byte [ 1024 ] ; private int len = 0 ; private int off = 0 ; InputStreamScanner ( InputStream in ) { this . in = in ; } String next ( ) { StringBuilder sb = new StringBuilder ( ) ; for ( int b = skip ( ) ; ! isSpace ( b ) ; ) { sb . appendCodePoint ( b ) ; b = read ( ) ; } return sb . toString ( ) ; } int nextInt ( ) { return Integer . parseInt ( next ( ) ) ; } long nextLong ( ) { return Long . parseLong ( next ( ) ) ; } double nextDouble ( ) { return Double . parseDouble ( next ( ) ) ; } char nextChar ( ) { return ( char ) skip ( ) ; } int skip ( ) { for ( int b ; ( b = read ( ) ) != - 1 ; ) { if ( ! isSpace ( b ) ) { return b ; } } return - 1 ; } private boolean isSpace ( int c ) { return c < 33 || c > 126 ; } private int read ( ) { if ( len == - 1 ) { throw new InputMismatchException ( " End ▁ of ▁ Input " ) ; } if ( off >= len ) { off = 0 ; try { len = in . read ( buf ) ; } catch ( IOException e ) { throw new InputMismatchException ( e . getMessage ( ) ) ; } if ( len <= 0 ) { return - 1 ; } } return buf [ off ++ ] ; } } }'''
    javaOneLineCode2 = '''public class Main { public static void main ( String [ ] args ) { java . util . Scanner sc = new java . util . Scanner ( System . in ) ; int N = sc . nextInt ( ) ; double mLT1 [ ] = new double [ N ] ; double mST1 [ ] = new double [ N ] ; int c1 = 0 ; int c2 = 0 ; int c3 = 0 ; int c4 = 0 ; int c5 = 0 ; int c6 = 0 ; for ( int i = 0 ; i < N ; i ++ ) { mLT1 [ i ] = sc . nextDouble ( ) ; mST1 [ i ] = sc . nextDouble ( ) ; if ( 35 <= mLT1 [ i ] ) { c1 ++ ; } if ( 30 <= mLT1 [ i ] & mLT1 [ i ] < 35 ) { c2 ++ ; } if ( 25 <= mLT1 [ i ] & mLT1 [ i ] < 30 ) { c3 ++ ; } if ( 25 <= mST1 [ i ] ) { c4 ++ ; } if ( 0 <= mLT1 [ i ] & mST1 [ i ] < 0 ) { c5 ++ ; } if ( mLT1 [ i ] < 0 ) { c6 ++ ; } } System . out . println ( c1 + " ▁ " + c2 + " ▁ " + c3 + " ▁ " + c4 + " ▁ " + c5 + " ▁ " + c6 ) ; } }'''
    javaOneLineCode3 = '''import java . util . Arrays ; class GFG { static long mod = 1000000007 ; static long [ ] [ ] arr = new long [ 1001 ] [ 1001 ] ; static void Preprocess ( ) { arr [ 0 ] [ 0 ] = 1 ; for ( int i = 1 ; i <= 1000 ; ++ i ) { arr [ i ] [ 0 ] = 1 ; for ( int j = 1 ; j < i ; ++ j ) { arr [ i ] [ j ] = ( arr [ i - 1 ] [ j - 1 ] + arr [ i - 1 ] [ j ] ) % mod ; } arr [ i ] [ i ] = 1 ; } } static long powmod ( long a , long n ) { if ( n == 0 ) { return 1 ; } long pt = powmod ( a , n / 2 ) ; pt = ( pt * pt ) % mod ; if ( n % 2 == 1 ) { return ( pt * a ) % mod ; } else { return pt ; } } static long CountSubset ( int [ ] val , int n ) { long ans = powmod ( 2 , n - 1 ) ; Arrays . sort ( val ) ; for ( int i = 0 ; i < n ; ++ i ) { int j = i + 1 ; while ( j < n && val [ j ] == val [ i ] ) { int r = n - 1 - j ; int l = i ; ans = ( ans + arr [ l + r ] [ l ] ) % mod ; j ++ ; } } return ans ; } public static void main ( String [ ] args ) { Preprocess ( ) ; int val [ ] = { 2 , 3 , 2 } ; int n = val . length ; System . out . println ( CountSubset ( val , n ) ) ; } }'''

    tree = getJavaAncestorMask(javaOneLineCode1)
    #print (tree.toStringTree())
    #for path, node in tree:
    #    print (path)
    #    break
