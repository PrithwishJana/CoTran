class Solution extends  object {
    public void productExceptSelf ( this , nums ) {
        var ans = { 1 } * len ( nums );
        for i in range ( 1 , len ( nums ) ) :
            ans { i } = ans { i - 1 } * nums { i - 1 };
        var right = 1;
        for i in range ( len ( nums ) - 1 , - 1 , - 1 ) :
            ans { i } *= right;
            right *= nums { i };
        return ans;
    }
}

if (var __name__ == "__main__") {
    var sObj = Solution ( );
    var nums = { 1 , 2 , 3 , 4 };
    var out = sObj . productExceptSelf ( nums );
    System.out.println ( out );
}
 