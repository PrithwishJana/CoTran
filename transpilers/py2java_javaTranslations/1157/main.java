var line1 = input ( ) . split ( );
var line2 = input ( ) . split ( );
var n = int ( line1 { 0 } );
var b = int ( line1 { 1 } );
var l1 = {};
for (int i = 0; i < line2.length; i++){
    l1 . append ( int ( i ) );
}
var l2 = {};
var num_of_cuts = 0;
for i in range ( len ( l1 ) ) :
    if (i != 0) {
        var num_of_odds = 0;
        var num_of_evens = 0;
        for j in l1 { : i } :
            if (j % 2 == 0) {
                num_of_evens += 1;
            }
             else{
                num_of_odds += 1;
            }
        if (num_of_evens == num_of_odds) {
            l2 . append ( abs ( l1 { i } - l1 { i - 1 } ) );
        }
     }
 l2 . sort ( );
for (int i = 0; i < l2.length; i++){
    if (i <= b) {
        num_of_cuts += 1;
        b -= i;
    }
}
 System.out.println ( num_of_cuts );
