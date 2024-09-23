import java.util.Scanner;
class AddTwoNumbers
{
    public static void main(String[] args)
    {
        int a,b;
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        int c = a+b;
        System.out.println("The sum of the numbers "+a+" and "+b+" is "+c);
    }
}