N , A , B , C , var D = map ( int , input ( ) . split ( ) );
if (( A <= N or C <= N )) {
    if (N % var A == 0) {
        var X = int ( N / A ) * B;
    }
     else{
        X = int ( N / A + 1 ) * B;
    }
    if (N % C == 0) {
        Y = int ( N / C ) * D;
    }
     else{
        Y = int ( N / C + 1 ) * D;
    }
}
 else{
    X = B;
    var Y = D;
}
if (X <= Y) {
    System.out.println ( int ( X ) );
}
 else{
    System.out.println ( int ( Y ) );
}
