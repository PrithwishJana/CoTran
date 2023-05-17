public void compute ( ) {
    var nine_pyramidal_pdf = { 1 };
    PYRAMIDAL_DIE_PDF = { 0 , 1 , 1 , 1 , 1 };
    for i in range ( 9 ) :
        nine_pyramidal_pdf = convolve ( nine_pyramidal_pdf , PYRAMIDAL_DIE_PDF );
    var six_cubic_pdf = { 1 };
    CUBIC_DIE_PDF = { 0 , 1 , 1 , 1 , 1 , 1 , 1 };
    for i in range ( 6 ) :
        six_cubic_pdf = convolve ( six_cubic_pdf , CUBIC_DIE_PDF );
    var ans = 0;
    for i in range ( len ( nine_pyramidal_pdf ) ) :
        ans += nine_pyramidal_pdf { i } * sum ( six_cubic_pdf { : i } );
    ans = float ( ans ) / ( sum ( nine_pyramidal_pdf ) * sum ( six_cubic_pdf ) );
    return f"{ans:.7f}";
}
public void convolve ( a , b ) {
    var c = { 0 } * ( len ( a ) + len ( b ) - 1 );
    for i in range ( len ( a ) ) :
        for j in range ( len ( b ) ) :
            c { i + j } += a { i } * b { j };
    return c;
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 