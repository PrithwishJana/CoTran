public void lps ( str ) {
    var n = len ( str );
    L = { [ 0 for x in range ( n ) } for y in range ( n ) ];
    for i in range ( n ) :
        L { i } { i } = 1;
    for cl in range ( 2 , n + 1 ) :
        for i in range ( n - cl + 1 ) :
            j = i + cl - 1;
            if (( str { i } == str { j } and cl == 2 )) {
                L { i } { j } = 2;
            }
             else if (( str { i } == str { j } )){
                L { i } { j } = L { i + 1 } { j - 1 } + 2;
            }
            else{
                L { i } { j } = max ( L { i } { j - 1 } , L { i + 1 } { j } );
            }
    return L { 0 } { n - 1 };
}
public void minimumNumberOfDeletions ( str ) {
    n = len ( str );
    var l = lps ( str );
    return ( n - l );
}
if (var __name__ == "__main__") {
    var str = "geeksforgeeks";
    System.out.println ( "Minimum number of var deletions = " , minimumNumberOfDeletions ( str ) );
}
 