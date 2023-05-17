import bisect.bisect_left , bisect_right;
while (true) {
    n , var m = map ( int , input ( ) . split ( ) );
    if (n == m == 0) {
        break;
    }
     var a = list ( map ( int , input ( ) . split ( ) ) );
    var w = list ( map ( int , input ( ) . split ( ) ) );
    var Set = set ( );
    public void go ( i , weight ) {
        if (var i == m) {
            Set . add ( weight );
            return;
        }
         go ( i + 1 , weight );
        go ( i + 1 , weight + w { i } );
        go ( i + 1 , weight - w { i } );
    }
    go ( 0 , 0 );
    var ans = false;
    for (int i = 0; i < a.length; i++){
        if (i not in Set) {
            if (ans == false) {
                ans = set ( abs ( s - i ) for s in Set );
            }
             else{
                ans = set ( s for s in ans if i + s in Set or i - s in Set );
            }
        }
    }
     if (ans == false) {
        System.out.println ( 0 );
        continue;
    }
     else if (len ( ans ) == 0){
        System.out.println ( - 1 );
        continue;
    }
    else{
        System.out.println ( min ( ans ) );
    }
}
 