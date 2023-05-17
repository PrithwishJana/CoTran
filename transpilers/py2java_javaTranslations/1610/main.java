public void getSecondMostFreq ( str ) {
    var NO_OF_CHARS = 256;
    var count = { 0 } * NO_OF_CHARS;
    for i in range ( len ( str ) ) :
        count { ord ( str [ i } ) ] += 1;
    first , var second = 0 , 0;
    for i in range ( NO_OF_CHARS ) :
        if (count { i } > count { first }) {
            second = first;
            first = i;
        }
         else if (( count { i } > count { second } and count { i } != count { first } )){
            second = i;
        }
    return chr ( second );
}
if (var __name__ == "__main__") {
    var str = "geeksforgeeks";
    var res = getSecondMostFreq ( str );
    if (res != '\0') {
        System.out.println ( "Second most frequent char is" , res );
    }
     else{
        System.out.println ( "No second most frequent character" );
    }
}
 