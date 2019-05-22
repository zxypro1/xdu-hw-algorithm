# Practice 3

> We highly encourage being environment friendly and trying all problems on your own.

我们强烈建议您保持环境友好并自行解决所有问题

## 1

> **Knapsack Problem** . There are 5 items that have a value and weight list below, the knapsack can contain at most 100 Lbs. Solve the problem both as fractional knapsack and 0/1 knapsack.

**背包问题** 。5个物品的价值和重量列表如下，背包最多可以装下100磅。 请解决，部分背包问题和0-1背包问题。

|                | 1    | 2    | 3    | 4    | 5    |
| -------------- | ---- | ---- | ---- | ---- | ---- |
| value (US $)   | 20   | 30   | 65   | 40   | 60   |
| weight (Lbs)   | 10   | 20   | 30   | 40   | 50   |
| value / weight | 2    | 1.5  | 2.1  | 1    | 1.2  |

## 2

> A simple **scheduling problem** . We are given jobs j1, j2… jn, all with known running times t1, t2… tn, respectively. We have a single processor. What is the best way to schedule these jobs in order to minimize the average completion time. Assume that it is a nonpreemptive scheduling: once a job is started, it must run to completion. The following is an instance.

一个简单的 **调度问题** 。我们给出作业 j1, j2, ... jn ，他们分别具有已知的运行时间 t1, t2, ... tn 。我们有单个处理器。为了最小的平均完成时间，调度这些作业的最好方法是什么。假设这是一个非抢占式的调度：一旦启动一个作业，他必须完成。以下是一个用例。

1. (j1, j2, j3, j4): (15, 8, 3, 10)

## 3

> **Single-source shortest paths** . The following is the adjaccency matrix, vertex A is the source.

**单源最短路** 。以下是邻接矩阵，以顶点 A 为源。

```text
   A  B  C  D  E
A    -1  3
B        3  2  2
C
D     1  5
E          -3
```

## 4

> **All-pairs shortest paths** . The adjacency matrix is as same as that of problem 3. (Use Floyd or Johnsons's algorithm)

**所有节点对最短路径** 。邻接矩阵同第3题。（请使用 Floyd 或 Johnsons 的算法）