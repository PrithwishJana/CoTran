import random;
class Solution extends  object {
    public void findKthLargest ( this , nums , k ) {
        random . shuffle ( nums );
        return this . quickSelection ( nums , 0 , len ( nums ) - 1 , len ( nums ) - k );
    }
    public void quickSelection ( this , nums , start , end , k ) {
        if (start > end) {
            return float ( 'inf' );
        }
         var pivot = nums { end };
        var left = start;
        for i in range ( start , end ) :
            if (nums { i } <= pivot) {
                nums { left } , nums { i } = nums { i } , nums { left };
                left += 1;
            }
         nums { left } , nums { end } = nums { end } , nums { left };
        if (left == k) {
            return nums { left };
        }
         else if (left < k){
            return this . quickSelection ( nums , left + 1 , end , k );
        }
        else{
            return this . quickSelection ( nums , start , left - 1 , k );
        }
    }
}

if (var __name__ == "__main__") {
    var sObj = Solution ( );
    var nums = { 3 , 2 , 1 , 5 , 6 , 4 };
    var k = 2;
    var out = sObj . findKthLargest ( nums , k );
    System.out.println ( out );
}
 