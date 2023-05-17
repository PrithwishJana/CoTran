public void LCSubStr ( X , Y , m , n ) {
    var LCSuff = { [ 0 for k in range ( n + 1 ) } for l in range ( m + 1 ) ];
    var result = 0;
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            if (( i == 0 or j == 0 )) {
                LCSuff { i } { j } = 0;
            }
             else if (( X { i - 1 } == Y { j - 1 } )){
                LCSuff { i } { j } = LCSuff { i - 1 } { j - 1 } + 1;
                result = max ( result , LCSuff { i } { j } );
            }
            else{
                LCSuff { i } { j } = 0;
            }
    return result;
}
var X = 'OldSite:GeeksforGeeks.org';
var Y = 'NewSite:GeeksQuiz.com';
var m = len ( X );
var n = len ( Y );
System.out.println ( 'Length of Longest Common Substring is' , LCSubStr ( X , Y , m , n ) );
