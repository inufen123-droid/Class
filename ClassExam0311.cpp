#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void printArray(int arr[], int n){
    for(int i=0;i<n;i++)
        cout<<arr[i]<<" ";
    cout<<endl;
}

void copyArray(int source[], int target[], int n){
    for(int i=0;i<n;i++)
        target[i]=source[i];
}

// Bubble Sort
void bubbleSortProcess(int arr[], int n){
    cout<<"\nBubble Sort Process:\n";
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(arr[j] > arr[j+1])
                swap(arr[j],arr[j+1]);
        }
        cout<<"Step "<<i+1<<": ";
        printArray(arr,n);
    }
}

// Insertion Sort
void insertionSortProcess(int arr[], int n){
    cout<<"\nInsertion Sort Process:\n";
    for(int i=1;i<n;i++){
        int key=arr[i];
        int j=i-1;
        while(j>=0 && arr[j]>key){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=key;
        cout<<"Step "<<i<<": ";
        printArray(arr,n);
    }
}

// Merge Sort
void merge(int arr[], int l, int m, int r){
    int i=l,j=m+1,k=0;
    int temp[100];
    while(i<=m && j<=r){
        if(arr[i]<=arr[j])
            temp[k++]=arr[i++];
        else
            temp[k++]=arr[j++];
    }
    while(i<=m) temp[k++]=arr[i++];
    while(j<=r) temp[k++]=arr[j++];
    for(i=l,k=0;i<=r;i++,k++) arr[i]=temp[k];
}

void mergeSortProcess(int arr[], int l, int r){
    if(l<r){
        int m=(l+r)/2;
        mergeSortProcess(arr,l,m);
        mergeSortProcess(arr,m+1,r);
        merge(arr,l,m,r);
        // 每次 merge 後顯示
        cout<<"Merge from "<<l<<" to "<<r<<": ";
        printArray(arr,r-l+1);
    }
}

// Quick Sort
int partition(int arr[], int low, int high){
    int pivot=arr[high],i=low-1;
    for(int j=low;j<high;j++){
        if(arr[j]<pivot){
            i++;
            swap(arr[i],arr[j]);
        }
    }
    swap(arr[i+1],arr[high]);
    return i+1;
}

void quickSortProcess(int arr[], int low, int high){
    if(low<high){
        int pi=partition(arr,low,high);
        quickSortProcess(arr,low,pi-1);
        quickSortProcess(arr,pi+1,high);
        // 每次 partition 後顯示
        cout<<"QuickSort pivot at "<<pi<<": ";
        for(int i=low;i<=high;i++) cout<<arr[i]<<" ";
        cout<<endl;
    }
}

int main(){
    srand(time(0));

    const int n=10;
    int arr[n];
    for(int i=0;i<n;i++)
        arr[i]=rand()%50;

    cout<<"Original Array:\n";
    printArray(arr,n);

    int temp[n];
    clock_t start,end;

    // Bubble
    copyArray(arr,temp,n);
    start=clock();
    bubbleSortProcess(temp,n);
    end=clock();
    cout<<"Bubble Sorted Result:\n";
    printArray(temp,n);
    cout<<"Bubble Sort Time: "<<(double)(end-start)/CLOCKS_PER_SEC<<" sec\n\n";

    // Insertion
    copyArray(arr,temp,n);
    start=clock();
    insertionSortProcess(temp,n);
    end=clock();
    cout<<"Insertion Sorted Result:\n";
    printArray(temp,n);
    cout<<"Insertion Sort Time: "<<(double)(end-start)/CLOCKS_PER_SEC<<" sec\n\n";

    // Merge
    copyArray(arr,temp,n);
    start=clock();
    mergeSortProcess(temp,0,n-1);
    end=clock();
    cout<<"Merge Sorted Result:\n";
    printArray(temp,n);
    cout<<"Merge Sort Time: "<<(double)(end-start)/CLOCKS_PER_SEC<<" sec\n\n";

    // Quick
    copyArray(arr,temp,n);
    start=clock();
    quickSortProcess(temp,0,n-1);
    end=clock();
    cout<<"Quick Sorted Result:\n";
    printArray(temp,n);
    cout<<"Quick Sort Time: "<<(double)(end-start)/CLOCKS_PER_SEC<<" sec\n";

    return 0;
}
