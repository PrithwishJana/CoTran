var T = int ( input ( ) );
for case in range ( 1 , T + 1 ) :
    N , var L = ( int ( i ) for i in input ( ) . split ( ) );
    var a = sorted ( int ( i , 2 ) for i in input ( ) . split ( ) );
    var b = sorted ( int ( i , 2 ) for i in input ( ) . split ( ) );
    var ans = L + 1;
    for (int i = 0; i < b.length; i++){
        if (sorted ( a { 0 } ^ i ^ j for j in a ) == b) {
            ans = min ( ans , bin ( a { 0 } ^ i ) . count ( '1' ) );
        }
    }
     if (ans == L + 1) {
        ans = 'NOT POSSIBLE';
    }
     System.out.println ( "Case; //{}: {}" . format ( case , ans ) )
