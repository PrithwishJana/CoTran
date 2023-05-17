public void minSwaps ( s1 , s2 ) {
    var c0 = 0 ; c1 = 0 ;;
    for i in range ( len ( s1 ) ) :
        if (( s1 { i } == '0' and s2 { i } == '1' )) {
            c0 += 1 ;;
        }
         else if (( s1 { i } == '1' and s2 { i } == '0' )){
            c1 += 1 ;;
        }
    var ans = c0 // 2 + c1 // 2 ;;
    if (( c0 % 2 == 0 and c1 % 2 == 0 )) {
        return ans ;;
    }
     else if (( ( c0 + c1 ) % 2 == 0 )){
        return ans + 2 ;;
    }
    else{
        return - 1 ;;
    }
}
if (__name__ == "__main__") {
    s1 = "0011" ; s2 = "1111" ;;
    ans = minSwaps ( s1 , s2 ) ;;
    System.out.println ( ans ) ;;
}
 