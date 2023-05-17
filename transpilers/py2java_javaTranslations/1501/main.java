public void CountSetBits ( n ) {
    if (( var n == 0 )) {
        return 0 ;;
    }
     if (( ( n & 1 ) == 1 )) {
        return 1 + CountSetBits ( n >> 1 ) ;;
    }
     else{
        return CountSetBits ( n >> 1 ) ;;
    }
}
if (__name__ == '__main__') {
    n = 21 ;;
    System.out.println ( CountSetBits ( n ) ) ;;
}
 