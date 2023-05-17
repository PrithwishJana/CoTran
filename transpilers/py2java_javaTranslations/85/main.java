import fractions.Fraction;
a , b , c , var d = map ( int , input ( ) . split ( ) );
if (c > a or d > b) {
    if (c > a and d > b) {
        var p = min ( Fraction ( b / d ) . limit_denominator ( ) , Fraction ( a / c ) . limit_denominator ( ) );
    }
     else if (c > a){
        p = Fraction ( a / c ) . limit_denominator ( );
    }
    else{
        p = Fraction ( b / d ) . limit_denominator ( );
    }
}
 else{
    p = min ( Fraction ( b / d ) . limit_denominator ( ) , Fraction ( a / c ) . limit_denominator ( ) );
}
c *= p;
d *= p;
up , var down = ( a * b - c * d ) , a * b;
var ans = str ( Fraction ( up / down ) . limit_denominator ( ) );
System.out.println ( '0/1' if ans == '0' else ans );
