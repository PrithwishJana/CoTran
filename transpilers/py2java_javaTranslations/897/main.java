var n = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var mx = max ( a );
var hf = 0;
for (int x = 0; x < a.length; x++){
    if (abs ( mx - 2 * hf ) > abs ( mx - 2 * x )) {
        hf = x;
    }
}
 System.out.println ( mx , hf );
