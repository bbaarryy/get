#include <iostream>
using namespace std;

struct Matrix
{
    int** data;
    int n, m;
};

void init(Matrix *matrix){
    int** arr = new int*[matrix->n];
    for(int i = 0 ; i < matrix->n;i++){
        arr[i] = new int[matrix->m];
    }
    matrix->data = arr;
}

void clean(Matrix *matrix){
    for(int i = 0 ; i < matrix->n;i++){
        delete[] matrix->data[i];
    }
    delete[] matrix->data;
}
void expand(Matrix* matrix, int n_minus, int n_plus, int m_minus, int m_plus){
    int** new_a = new int*[matrix->n + n_minus + n_plus];
    int N = matrix->n + n_minus + n_plus;
    for(int i = 0 ; i < N;i++){
        new_a[i] = new int[matrix->m + m_minus + m_plus];
    }
    
    int M = matrix->m + m_minus + m_plus;
    for(int i = 0 ; i < N ; i ++){
        for(int j=0 ; j<M ; j++){
            new_a[i][j] = 0;
        }
    }
    for(int i = n_minus;i<n_minus + matrix->n;i++){
        for(int j= m_minus;j<m_minus+matrix->n;j++){
            new_a[i][j] = matrix->data[i-n_minus][j-m_minus];
        }
    }

    int** last = matrix->data;
    int last_n = matrix->n;
    int last_m = matrix->m;
    matrix->data = new_a;
    matrix->n = N;
    matrix->m = M;
    for(int i = 0 ; i < last_n;i++){
        delete[]last[i];
    }
    delete[] last;
}

int main()
{
    Matrix matrix;
    cin >> matrix.n >> matrix.m;
    init(&matrix);
    for (int i = 0; i < matrix.n; i++)
        for (int j = 0; j < matrix.m; j++)
            cin >> matrix.data[i][j];

    int n_minus, n_plus, m_minus, m_plus;
    cin >> n_minus >> n_plus >> m_minus >> m_plus;

    expand(&matrix, n_minus, n_plus, m_minus, m_plus);

    for (int i = 0; i < matrix.n; i++)
    {
        for (int j = 0; j < matrix.m; j++)
            cout << matrix.data[i][j];
        cout << endl;
    }

    clean(&matrix);
    return 0;
}