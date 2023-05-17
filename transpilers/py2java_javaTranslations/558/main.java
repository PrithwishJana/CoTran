class Solution extends  object {
    public void isPerfectSquare ( this , num ) {
        low , var high = 1 , num;
        while (low <= high) {
            mid = ( low + high ) // 2;
            mid_square = mid * mid;
            if (mid_square == num) {
                return true;
            }
             else if (mid_square < num){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }
         return false;
    }
}

if (var __name__ == "__main__") {
    var sObj = Solution ( );
    var num = 16;
    var out = sObj . isPerfectSquare ( num );
    System.out.println ( out );
}
 