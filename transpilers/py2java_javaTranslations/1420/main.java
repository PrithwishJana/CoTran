var a = input ( );
var b = input ( );
var numOf0 = { 0 for i in range ( len ( b ) + 1 ) };
var numOf1 = { 0 for i in range ( len ( b ) + 1 ) };
var r = 0;
for i in range ( len ( b ) ) :
    numOf0 { i } = numOf0 { i - 1 } + ( b { i } == '0' );
    numOf1 { i } = numOf1 { i - 1 } + ( b { i } == '1' );
for i in range ( len ( a ) ) :
    r += ( numOf1 { len ( b ) - len ( a ) + i } - numOf1 { i - 1 } ) if a { i } == '0' else ( numOf0 { len ( b ) - len ( a ) + i } - numOf0 { i - 1 } );
System.out.println ( r );
