public void findMinimumX ( a , n ) {
    var st = set ( );
    for i in range ( n ) :
        st . add ( a { i } );
    if (( len ( st ) == 1 )) {
        return 0;
    }
     if (( len ( st ) == 2 )) {
        st = list ( st );
        el1 = st { 0 };
        el2 = st { 1 };
        if (( ( el2 - el1 ) % 2 == 0 )) {
            return int ( ( el2 - el1 ) / 2 );
        }
         else{
            return ( el2 - el1 );
        }
    }
     if (( len ( st ) == 3 )) {
        st = list ( st );
        var el1 = st { 0 };
        var el2 = st { 1 };
        var el3 = st { 2 };
        if (( ( el2 - el1 ) == ( el3 - el2 ) )) {
            return el2 - el1;
        }
         else{
            return - 1;
        }
    }
     return - 1;
}
if (var __name__ == '__main__') {
    var a = { 1 , 4 , 4 , 7 , 4 , 1 };
    var n = len ( a );
    System.out.println ( findMinimumX ( a , n ) );
}
 