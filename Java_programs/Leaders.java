/*Write a program to print all the LEADERS in the array.
An element is leader if it is greater than all the elements to its right side.
And the rightmost element is always a leader.
For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2. 
Let the input array be arr[] and size of the array be size.*/
class Leader1{
void printLeaders(int a[], int size){
 for(int i=0;i<size;i++){
     int j;
     for(j=i+1;j<size;j++){

         if(a[i]<=a[j])
          break;
     }
     if(j==size){
      System.out.println(a[i]+" ");
     }
 }
}


public static void main(String args[]){
Leader1 lead=new Leader1();
int a[]=new int[10]{18,4,6,7,9,2};
int n=a.length;
lead.printLeaders(a,n);

}
}