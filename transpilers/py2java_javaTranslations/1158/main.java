public void maxOperations ( str ) {
    i , g , gk , var gks = 0 , 0 , 0 , 0;
    for i in range ( len ( str ) ) :
        if (( str { i } == 'g' )) {
            g += 1;
        }
         else if (( str { i } == 'k' )){
            if (( g > 0 )) {
                g -= 1;
                gk += 1;
            }
         }
        else if (( str { i } == 's' )){
            if (( gk > 0 )) {
                gk -= 1;
                gks += 1;
            }
         }
    return gks;
}
if (var __name__ == "__main__") {
    var a = "ggkssk";
    System.out.println ( maxOperations ( a ) );
}
 