class MinStack extends  object {
    protected void init__ ( this ) {
        this . var stack = {};
        this . min_stack = {};
    }
    public void push ( this , x ) {
        this . stack . append ( x );
        if (len ( this . min_stack ) == 0) {
            this . min_stack . append ( x );
            return;
        }
         if (x <= this . min_stack { - 1 }) {
            this . min_stack . append ( x );
        }
         else{
            this . min_stack . append ( this . min_stack { - 1 } );
        }
    }
    public void pop ( this ) {
        if (len ( this . stack ) > 0) {
            this . min_stack . pop ( );
            this . stack . pop ( );
        }
     }
    public void top ( this ) {
        if (len ( this . stack ) > 0) {
            return this . stack { - 1 };
        }
         return None;
    }
    public void getMin ( this ) {
        if (len ( this . min_stack ) > 0) {
            return this . min_stack { - 1 };
        }
         return None;
    }
}

if (var __name__ == "__main__") {
    var m = MinStack ( );
    m . push ( - 2 );
    m . push ( 0 );
    m . push ( - 3 );
    System.out.println ( m . getMin ( ) );
    m . pop ( );
    System.out.println ( m . top ( ) );
    System.out.println ( m . getMin ( ) );
}
 