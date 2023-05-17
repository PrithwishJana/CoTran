public void findMinimumSubsequences ( A , B ) {
    var numberOfSubsequences = 1;
    sizeOfB = len ( B );
    sizeOfA = len ( A );
    inf = 1000000;
    next = { [ inf for i in range ( sizeOfB ) } for i in range ( 26 ) ];
    for i in range ( sizeOfB ) :
        next { ord ( B [ i } ) - ord ( 'a' ) ] { i } = i;
    for i in range ( 26 ) :
        for j in range ( sizeOfB - 2 , - 1 , - 1 ) :
            if (( next { i } { j } == inf )) {
                next { i } { j } = next { i } { j + 1 };
            }
     pos = 0;
    i = 0;
    while (( i < sizeOfA )) {
        if (( pos == 0 and next { ord ( A [ i } ) - ord ( 'a' ) ] { pos } == inf )) {
            numberOfSubsequences = - 1;
            break;
        }
         else if (( pos < sizeOfB and next { ord ( A [ i } ) - ord ( 'a' ) ] { pos } < inf )){
            var nextIndex = next { ord ( A [ i } ) - ord ( 'a' ) ] { pos } + 1;
            var pos = nextIndex;
            i += 1;
        }
        else{
            numberOfSubsequences += 1;
            pos = 0;
        }
    }
     return numberOfSubsequences;
}
if (var __name__ == '__main__') {
    var A = "aacbe";
    var B = "aceab";
    System.out.println ( findMinimumSubsequences ( A , B ) );
}
 