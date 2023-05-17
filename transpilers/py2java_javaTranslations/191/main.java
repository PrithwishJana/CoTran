public void longest_subseq ( n , k , s ) {
    var dp = { 0 } * n;
    var max_length = { 0 } * 26;
    for i in range ( n ) :
        var curr = ord ( s { i } ) - ord ( 'a' );
        var lower = max ( 0 , curr - k );
        var upper = min ( 25 , curr + k );
        for j in range ( lower , upper + 1 ) :
            dp { i } = max ( dp { i } , max_length { j } + 1 );
        max_length { curr } = max ( dp { i } , max_length { curr } );
    return max ( dp );
}
public void main ( ) {
    var s = "geeksforgeeks";
    var n = len ( s );
    var k = 3;
    System.out.println ( longest_subseq ( n , k , s ) );
}
main ( );
