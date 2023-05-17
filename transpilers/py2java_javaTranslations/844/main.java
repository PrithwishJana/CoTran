class Solution extends  object {
    public void findRadius ( this , houses , heaters ) {
        var heaters = sorted ( heaters ) + { float ( 'inf' ) };
        i = r = 0;
        for x in sorted ( houses ) :
            while x >= sum ( heaters { i : i + 2 } ) / 2. :
                i += 1;
            r = max ( r , abs ( heaters { i } - x ) );
        return r;
    }
}

if (__name__ == "__main__") {
    sObj = Solution ( );
    houses = { 1 , 2 , 3 };
    heaters = { 2 };
    var out = sObj . findRadius ( houses , heaters );
    System.out.println ( out );
}
 