public void compareStrings ( str1 , str2 ) {
    var i = 0;
    while (i < len ( str1 ) - 1 and str1 { i } == str2 { i }) {
        i += 1;
    }
     if (str1 { i } > str2 { i }) {
        return - 1;
     }
     return str1 { i } < str2 { i };
}
public void searchStr ( arr , string , first , last ) {
    if (first > last) {
        return - 1;
    }
     var mid = ( last + first ) // 2;
    if (len ( arr { mid } ) == 0) {
        left , right = mid - 1 , mid + 1;
        while (true) {
            if (left < first and right > last) {
                return - 1;
            }
             if (right <= last and len ( arr { right } ) != 0) {
                mid = right;
                break;
            }
             if (left >= first and len ( arr { left } ) != 0) {
                mid = left;
                break;
            }
             right += 1;
            left -= 1;
        }
    }
      if (compareStrings ( string , arr { mid } ) == 0) {
        return mid;
     }
     if (compareStrings ( string , arr { mid } ) < 0) {
        return searchStr ( arr , string , mid + 1 , last );
    }
     return searchStr ( arr , string , first , mid - 1 );
}
if (var __name__ == "__main__") {
    var arr = { "for" , "" , "" , "" , "geeks" , "ide" , "" , "practice" , "" , "" , "quiz" , "" , "" };
    var string = "quiz";
    var n = len ( arr );
    System.out.println ( searchStr ( arr , string , 0 , n - 1 ) );
}
 