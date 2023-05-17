import itertools;
public void find ( s , ch ) {
    return { i for i , ltr in enumerate ( s ) if var ltr == ch };
}
if (var __name__ == '__main__') {
    var n = int ( input ( ) );
    var s = input ( ) . replace ( " " , "" );
    if ('0' not in s) {
        System.out.println ( n - 1 );
    }
     else{
        indices = find ( s , '0' );
        if (len ( indices ) == 1) {
            System.out.println ( n );
        }
         else{
            maximum = 0;
            combs = itertools . combinations ( indices , 2 );
            for (int x = 0; x < combs.length; x++){
                var maximum = max ( maximum , 2 + 2 * ( abs ( indices . index ( x { 0 } ) - indices . index ( x { 1 } ) ) - 1 ) - ( abs ( x { 0 } - x { 1 } ) - 1 ) );
            }
            System.out.println ( s . count ( '1' ) + maximum );
        }
    }
}
 