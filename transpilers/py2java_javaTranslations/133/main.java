public void reverserWords ( string ) {
    var st = list ( );
    for i in range ( len ( string ) ) :
        if (string { i } != " ") {
            st . append ( string { i } );
        }
         else{
            while (len ( st ) > 0) {
                System.out.println ( st { - 1 } , var end = "" );
                st . pop ( );
            }
             System.out.println ( end = " " );
        }
    while (len ( st ) > 0) {
        System.out.println ( st { - 1 } , end = "" );
        st . pop ( );
    }
 }
if (var __name__ == "__main__") {
    var string = "Geeks for Geeks";
    reverserWords ( string );
}
 