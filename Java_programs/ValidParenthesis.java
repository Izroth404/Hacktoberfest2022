//Valid Parenthesis Problem solution in java.
import java.util.Scanner;
import java.util.Stack;

public class ValidParenthesis {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String str = input.nextLine();
        if(check(str))  System.out.println("Valid Parenthesis.");
        else System.out.println("Invalid Parenthesis.");
    }

    private static boolean check(String str) {
        if(str == null){
            return true;
        }

        if(str.length() % 2 == 1) return false;

        Stack<Character> stk = new Stack<>();

        for(char ch : str.toCharArray()){
            if(ch == '(' || ch == '[' || ch == '{'){
                stk.push(ch);
            }else if(ch == ')' && !stk.isEmpty() && stk.peek() == '('){
                stk.pop();
            }else if(ch == ']' && !stk.isEmpty() && stk.peek() == '['){
                stk.pop();
            }else if(ch == '}' && !stk.isEmpty() && stk.peek() == '{'){
                stk.pop();
            }else{
                return false;
            }
        }
        return stk.isEmpty();
    }
}
