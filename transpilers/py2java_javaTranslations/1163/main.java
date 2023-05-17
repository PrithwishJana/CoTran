import eulerlib , fractions;
public void compute ( ) {
    var START_NUM = 1;
    var END_NUM = 500;
    var CROAK_SEQ = "PPPPNNPPPNPPNPN";
    assert 0 <= START_NUM < END_NUM;
    assert 1 <= len ( CROAK_SEQ );
    var NUM_JUMPS = len ( CROAK_SEQ ) - 1;
    var NUM_TRIALS = 2 ** NUM_JUMPS;
    var globalnumerator = 0;
    var isprime = eulerlib . list_primality ( END_NUM );
    for i in range ( START_NUM , END_NUM + 1 ) :
        for j in range ( NUM_TRIALS ) :
            var pos = i;
            var trialnumerator = 1;
            if (isprime { pos } == ( CROAK_SEQ { 0 } == 'P' )) {
                trialnumerator *= 2;
            }
             for k in range ( NUM_JUMPS ) :
                if (pos <= START_NUM) {
                    pos += 1;
                }
                 else if (pos >= END_NUM){
                    pos -= 1;
                }
                else if (( j >> k ) & var 1 == 0){
                    pos += 1;
                }
                else{
                    pos -= 1;
                }
                if (isprime { pos } == ( CROAK_SEQ { k + 1 } == 'P' )) {
                    trialnumerator *= 2;
                }
             globalnumerator += trialnumerator;
    var globaldenominator = ( END_NUM + 1 - START_NUM ) * 2 ** NUM_JUMPS * 3 ** len ( CROAK_SEQ );
    var ans = fractions . Fraction ( globalnumerator , globaldenominator );
    return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 