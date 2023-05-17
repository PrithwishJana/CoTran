public void areVowelsInOrder ( s ) {
    var n = len ( s );
    var c = chr ( 64 );
    for i in range ( 1 , n ) :
        if (( s { i } == 'a' or s { i } == 'e' or s { i } == 'i' or s { i } == 'o' or s { i } == 'u' )) {
            if (s { i } < c) {
                return false;
            }
             else{
                c = s { i };
            }
        }
     return true;
}
if (var __name__ == "__main__") {
    var s = "aabbbddeecc";
    if (areVowelsInOrder ( s )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 