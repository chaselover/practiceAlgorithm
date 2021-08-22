#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
 
using namespace std;
 
typedef pair<int, int> pii;
 
const int INF = 1e9 + 1;
 
pii init(vector<int> &arr, vector<pii> &tree, int node, int start, int end)
{
    if (start == end)
        return tree[node] = { arr[start], start };
    
    int mid = (start + end) / 2;
 
    return tree[node] = min(init(arr, tree, node * 2, start, mid), init(arr, tree, node * 2 + 1, mid + 1, end));
}
 
pii update(vector<pii> &tree, int node, int start, int end, int idx, int val)
{
    if (!(start <= idx && idx <= end))
        return tree[node];
 
    if (start == end)
        return tree[node] = { val, start };
    
    int mid = (start + end) / 2;
 
    return tree[node] = min(update(tree, node * 2, start, mid, idx, val), update(tree, node * 2 + 1, mid + 1, end, idx, val));
}
 
pii query(vector<pii> &tree, int node, int start, int end, int left, int right)
{
    if (right < start || left > end)
        return{ INF, INF };
 
    if (left <= start && end <= right)
        return tree[node];
    
    int mid = (start + end) / 2;
 
    return min(query(tree, node * 2, start, mid, left, right), query(tree, node * 2 + 1, mid + 1, end, left, right));
}
int main()
{
    int n;
    scanf("%d", &n);
 
    vector<int> arr(n);
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
 
    int h = (int)ceil(log2(n));
    int tree_size = (1 << (h + 1));
 
    vector<pii> tree(tree_size);
 
    init(arr, tree, 1, 0, n - 1);
    
    int m;
    scanf("%d", &m);
 
    while (m--)
    {
        int num, i, j;
        scanf("%d %d %d", &num, &i, &j);
 
        if (num == 1)
            update(tree, 1, 0, n - 1, i - 1, j);
        else
            printf("%d\n", query(tree, 1, 0, n - 1, i - 1, j - 1).second + 1);
    }
 
    return 0;
}


출처: https://www.crocus.co.kr/1208 [Crocus]