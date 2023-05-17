public void minReplacement ( string ) {
    if (len ( string ) > 26) {
        System.out.println ( "IMPOSSIBLE" );
    }
     else{
        var Hash = { 0 } * 26;
        for i in range ( 0 , len ( string ) ) :
            Hash { ord ( string [ i } ) - ord ( 'a' ) ] += 1;
        var count = 0;
        for i in range ( 0 , len ( string ) ) :
            if (Hash { ord ( string [ i } ) - ord ( 'a' ) ] > 1) {
                for j in range ( 0 , 26 ) :
                    if (Hash { j } == 0) {
                        Hash { ord ( string [ i } ) - ord ( 'a' ) ] -= 1;
                        string { i } = chr ( j + ord ( 'a' ) );
                        Hash { j } += 1;
                        break;
                    }
             }
         System.out.println ( '' . join ( string ) );
    }
}
if (var __name__ == "__main__") {
    var string = "xxxxyyyy";
    minReplacement ( list ( string ) );
}
 