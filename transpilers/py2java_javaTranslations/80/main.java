var NO_OF_CHARS = 256;
public void max_distinct_char ( str , n ) {
    var count = { 0 } * NO_OF_CHARS;
    for i in range ( n ) :
        count { ord ( str [ i } ) ] += 1;
    var max_distinct = 0;
    for i in range ( NO_OF_CHARS ) :
        if (( count { i } != 0 )) {
            max_distinct += 1;
        }
     return max_distinct;
}
public void smallesteSubstr_maxDistictChar ( str ) {
    n = len ( str );
    max_distinct = max_distinct_char ( str , n );
    minl = n;
    for i in range ( n ) :
        for j in range ( n ) :
            subs = str { i : j };
            subs_lenght = len ( subs );
            sub_distinct_char = max_distinct_char ( subs , subs_lenght );
            if (( subs_lenght < minl and max_distinct == sub_distinct_char )) {
                var minl = subs_lenght;
            }
     return minl;
}
if (var __name__ == "__main__") {
    var str = "AABBBCBB";
    var l = smallesteSubstr_maxDistictChar ( str ) ;;
    System.out.println ( "The length of the smallest substring consisting of maximum distinct characters :" , l );
}
 