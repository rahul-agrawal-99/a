// 2 Write a program to implement Parallel Bubble Sort and Merge sort using OpenMP. Use
// existing algorithms and measure the performance of sequential and parallel algorithms.


//  g++ 2Bubble.cpp -lgomp -o bubble
//  ./bubble 10000000    means array size is 10000000

#include <omp.h>
#include <stdlib.h>
#include <iostream>

using namespace std;
void s_bubble(int *, int);
void p_bubble(int *, int);
void swap(int &, int &);


void s_bubble(int *a, int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1 ; j < n; j++)
        {
            if (a[j] < a[i])
            {
                swap(a[j], a[i]);
            }
        }
}

// print sorted array
cout << "\nSorted array: \n";
for (int i = 0; i < n; i++)
{
    cout << a[i] << " ";
}
}

void p_bubble(int *a, int n)
{

    for (int i = 0; i < n; i++)
    {
        // int first = i % 2;
#pragma omp parallel for shared(a, i+1) num_threads(16)
        for (int j = i+ 1 ; j < n; j++)
        {
            if (a[j] < a[i])
            {
                swap(a[j], a[i]);
            }
        }
    }

    // print sorted array
    cout << "\nSorted array: \n";
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
}
void swap(int &a, int &b)
{
    int test;
    test = a;
    a = b;
    b = test;
}

int main()

{
    int n = 10;
    int a[n] ;
    srand(time(0));
    for (int i = 0; i < n; i++)
    {
        a[i] = rand() % 10000;
    }

    //  print init array
    cout << "Initial array: \n";
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }

    // sequential bubble sort
    double start_time = omp_get_wtime();
    s_bubble(a, n);
    double end_time = omp_get_wtime();
    cout << "Sequential time: " << (end_time - start_time) << "seconds" << endl;
    double sq_time = (end_time - start_time);

    // parallel bubble sort
     start_time = omp_get_wtime();
    p_bubble(a, n);
     end_time = omp_get_wtime();
    cout << "Parallel time: " << (end_time - start_time) << "seconds" << endl;
    double p_time = (end_time - start_time);

    double speedup = sq_time / p_time;
    cout << "Speedup: " << speedup << endl;

    double efficiency = speedup / 16;  // 16 is number of threads
    cout << "Efficiency: " << efficiency << endl;


    return 0;
}