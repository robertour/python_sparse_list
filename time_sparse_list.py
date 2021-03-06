#!/usr/bin/env python

import benchmark
import sparse_list


class Benchmark_Repr(benchmark.Benchmark):
    def setUp(self):
        self.sparse_list = sparse_list.SparseList(1000)
        self.list = [None] * 1000

    def test_sparse_list(self):
        repr(self.sparse_list)

    def test_list(self):
        repr(self.list)

class Benchmark_Insert(benchmark.Benchmark):
    def setUp(self):
        self.sparse_list = sparse_list.SparseList(1000)
        self.list = [None] * 1000

    def test_sparse_list(self):
        self.sparse_list[100] = 'apple'

    def test_list(self):
        self.list[100] = 'apple'

class Benchmark_Retrieval(benchmark.Benchmark):
    def setUp(self):
        self.sparse_list = sparse_list.SparseList(1000)
        self.list = [None] * 1000

    def test_sparse_list(self):
        self.sparse_list[100]

    def test_list(self):
        self.list[100]

if __name__ == '__main__':
    benchmark.main(format="markdown", numberFormat="%.4g")
