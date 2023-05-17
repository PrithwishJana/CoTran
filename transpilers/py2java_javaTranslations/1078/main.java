public void sumOfDigitsSingle ( x ) {
    var ans = 0;
    while (x) {
        ans += x % 10;
        x //= 10;
    }
     return ans;
}
public void closest ( x ) {
    ans = 0;
    while (( ans * 10 + 9 <= x )) {
        ans = ans * 10 + 9;
    }
     return ans;
}
public void sumOfDigitsTwoParts ( N ) {
    var A = closest ( N );
    return sumOfDigitsSingle ( A ) + sumOfDigitsSingle ( N - A );
}
if (var __name__ == "__main__") {
    var N = 35;
    System.out.println ( sumOfDigitsTwoParts ( N ) );
}
 