public void solve ( M , N , s ) {
    if (( N % var s == 0 )) {
        N = N // s;
    }
     else{
        N = ( N // s ) + 1;
    }
    if (( M % s == 0 )) {
        M = M // s;
    }
     else{
        M = ( M // s ) + 1;
    }
    return M * N;
}
if (__name__ == "__main__") {
    N , M , s = 12 , 13 , 4;
    System.out.println ( solve ( M , N , s ) );
}
 