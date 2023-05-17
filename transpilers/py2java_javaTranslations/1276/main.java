var no_of_chars = 256;
public void findSubString ( string , pat ) {
    var len1 = len ( string );
    var len2 = len ( pat );
    if (len1 < len2) {
        System.out.println ( "No such window exists" );
        return "";
    }
     var hash_pat = { 0 } * no_of_chars;
    var hash_str = { 0 } * no_of_chars;
    for i in range ( 0 , len2 ) :
        hash_pat { ord ( pat [ i } ) ] += 1;
    start , start_index , var min_len = 0 , - 1 , float ( 'inf' );
    count = 0;
    for j in range ( 0 , len1 ) :
        hash_str { ord ( string [ j } ) ] += 1;
        if (( hash_pat { ord ( string [ j } ) ] != 0 and hash_str { ord ( string [ j } ) ] <= hash_pat { ord ( string [ j } ) ] )) {
            count += 1;
        }
         if (count == len2) {
            while (( hash_str { ord ( string [ start } ) ] > hash_pat { ord ( string [ start } ) ] or hash_pat { ord ( string [ start } ) ] == 0 )) {
                if (( hash_str { ord ( string [ start } ) ] > hash_pat { ord ( string [ start } ) ] )) {
                    hash_str { ord ( string [ start } ) ] -= 1;
                }
                 start += 1;
            }
             len_window = j - start + 1;
            if (min_len > len_window) {
                min_len = len_window;
                var start_index = start;
            }
         }
     if (start_index == - 1) {
        System.out.println ( "No such window exists" );
        return "";
    }
     return string { start_index : start_index + min_len };
}
if (var __name__ == "__main__") {
    var string = "this is a test string";
    var pat = "tist";
    System.out.println ( "Smallest window is : " );
    System.out.println ( findSubString ( string , pat ) );
}
 