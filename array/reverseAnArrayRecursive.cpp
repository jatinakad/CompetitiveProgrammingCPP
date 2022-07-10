// Recursive C++ program to reverse an array
#include<iostream>
using namespace std;


/* Function to reverse arr[] from start to end*/

void reverseArray(int arr[],int start,int end)
{
    if(start >= end)
    return;
    {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        reverseArray(arr,start+1,end-1); // Recursive Function calling
    }
}
/* Utility function to print an array */
void printArray(int arr[],int size)
{
    for(int i =0;i<size;i++)
    cout<<arr[i]<<" ";
    cout<<endl;
}
/* Driver function to test above functions */
int main()
{
    int arr[] = {1,2,3,4,5,6};

    // To print original array
    printArray(arr ,6); 
    // Function calling
    reverseArray(arr,0,5);
     // To print the Reversed array
    cout<<"Reversed array is"<<endl;

    printArray(arr,6);

    return 0;
}