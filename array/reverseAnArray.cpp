
// Iterative C++ program to reverse an array
#include<iostream>
using namespace std;

/* Function to reverse arr[] from start to end*/
void reverseArray(int arr[],int start, int end){
    while(start<end)
    {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}
/* Utility function to print an array */
void printArray(int arr[], int size)
{
    for(int i = 0;i < size;i++)
    cout<<arr[i]<<" ";
    cout<<endl;
}
/* Driver function to test above functions */
int main()
{
    int arr[] = {0,1,2,3,4,5,6};

    int n = sizeof(arr)/sizeof(arr[0]); /*If you have an array then sizeof(array) returns the number of bytes the array occupies. Since each element can take more than 1 byte of space, you have to divide the result with the size of one element (sizeof(array[0])). This gives you number of elements in the array.*/

    printArray(arr, n);  // To print original array

    reverseArray(arr,0,n-1);// Function calling

    cout<<"Reverse array is"<<endl;

    printArray(arr, n);// To print the Reversed array

    return 0;
}