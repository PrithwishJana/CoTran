public void reverseDigits ( num ) {
    var rev_num = 0 ;;
    while (( num > 0 )) {
        rev_num = rev_num * 10 + num % 10;
        var num = num // 10;
    }
     return rev_num;
}
public void isPalindrome ( n ) {
    var rev_n = reverseDigits ( n ) ;;
    if (( rev_n == n )) {
        return 1;
    }
     else{
        return 0;
    }
}
if (var __name__ == "__main__") {
    var n = 4562;
    if (isPalindrome ( n ) == 1) {
        System.out.println ( "Is" , n , "a Palindrome number? ->" , true );
    }
     else{
        System.out.println ( "Is" , n , "a Palindrome number? ->" , false );
    }
    n = 2002;
    if (isPalindrome ( n ) == 1) {
        System.out.println ( "Is" , n , "a Palindrome number? ->" , true );
    }
     else{
        System.out.println ( "Is" , n , "a Palindrome number? ->" , false );
    }
}
 