var N = 10000 ;;
var MOD = 1000000007 ;;
var F = { 0 } * N ;;
public void precompute ( ) {
    F { 1 } = 2 ;;
    F { 2 } = 3 ;;
    F { 3 } = 4 ;;
    for i in range ( 4 , N ) :
        F { i } = ( F { i - 1 } + F { i - 2 } ) % MOD ;;
}
var n = 8 ;;
precompute ( ) ;;
System.out.println ( F { n } ) ;;
