import java.util.*;
/**
 * gcd
 */
public class gcd {


    public static int GCD(int x, int y){
        int p=x%y;
        if(p!=0)
        {return GCD(y,p);}
        return y;
    }
    public static void main(String[] args){
            Scanner sc = new Scanner(System.in);
            int a = sc.nextInt();
            int b = sc.nextInt();
           ;
            System.out.println(GCD(a,b));
    }
}