import eulerlib , fractions , math;
public void compute ( ) {
    var NUM_COLORS = 7;
    var BALLS_PER_COLOR = 10;
    var NUM_PICKED = 20;
    var DECIMALS = 9;
    var numerator = { 0 };
    public void explore ( remain , limit , history ) {
        if (var remain == 0) {
            var hist = list ( history );
            while (len ( hist ) < NUM_COLORS) {
                hist . append ( 0 );
            }
             var histogram = { 0 } * ( BALLS_PER_COLOR + 1 );
            for (int x = 0; x < hist.length; x++){
                histogram { x } += 1;
            }
            var count = math . factorial ( NUM_COLORS );
            for (int x = 0; x < histogram.length; x++){
                count = divide_exactly ( count , math . factorial ( x ) );
            }
            for (int x = 0; x < hist.length; x++){
                count *= eulerlib . binomial ( BALLS_PER_COLOR , x );
            }
            var distinctcolors = len ( history );
            numerator { 0 } += count * distinctcolors;
        }
         else if (len ( history ) < NUM_COLORS){
            for i in range ( min ( limit , remain ) , 0 , - 1 ) :
                history . append ( i );
                explore ( remain - i , i , history );
                history . pop ( );
        }
    }
    explore ( NUM_PICKED , BALLS_PER_COLOR , {} );
    var denominator = eulerlib . binomial ( NUM_COLORS * BALLS_PER_COLOR , NUM_PICKED );
    var ans = fractions . Fraction ( numerator { 0 } , denominator );
    return format_fraction ( ans , DECIMALS );
}
public void format_fraction ( val , digits ) {
    if (digits <= 0) {
        raise ValueError ( );
    }
     if (val < 0) {
        return "-" + format_fraction ( - val , digits );
    }
     var s = str ( round ( val * 10 ** digits ) ) . zfill ( digits + 1 );
    return f"{s{:-digits}}.{s{-digits:}}";
}
public void divide_exactly ( x , y ) {
    if (x % y != 0) {
        raise ValueError ( "Not divisible" );
    }
     return x // y;
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 