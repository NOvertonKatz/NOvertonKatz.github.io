---
tags: c++, parallel
date: "2025-05-10"
category: "Software"
---
# Getting started with C++ Std Parallel
https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag_t


Of the many new exciting features in C++17 
https://developer.nvidia.com/blog/multi-gpu-programming-with-standard-parallel-c-part-1/

What I think is one of the more powerful features of the standard library execution policies, is there is support for a variety of different hardware with almost no change in code. The same code can operate on multiple CPU threads, vectorization, and both Nvidia and AMD GPUs. 

As a far as I can tell, both GCC and Clang only support mulit-threading for parallel algorithms using Intel's Thread Building blocks (TBB). It is simple to install on most linux systems, and simplex requires adding the ```-ltbb``` flag

It looks like GCC has experimental support for native std parallel threading using openmp as a backend https://gcc.gnu.org/onlinedocs/libstdc++/manual/parallel_mode_using.html

To use Nvidia GPUs
```nvc++ -stdpar=gpu```
https://docs.nvidia.com/hpc-sdk/archive/23.9/pdf/hpc239c++_par_alg.pdf


For AMD GPUs, clang has direct support
https://github.com/ROCm/llvm-project/blob/amd-mainline-open/clang/docs/HIPSupport.rst#id15
```clang++ --hipstdpar```
https://rocm.blogs.amd.com/software-tools-optimization/hipstdpar/README.html


```
std::execution::par_unseq
```


```c++
#include <algorithm>
#include <random>

#include "Config_HashBrick.hpp"

// supply main
#include "catch2ParallelMain.hpp"

#define USE_STDPAR
// macro for enabling standard parallel
#if USE_STDPAR
#include <execution>
#define SEQ std::execution::seq,
#define PAR std::execution::par_unseq,
#else // serial
#define SEQ
#define PAR
#endif

// see output in pout.# files
TEST_CASE("Simple standard library parallel", "[stdpar]")
{
  constexpr size_t dataSize = 1e6;
  // linear decreasing index
  std::vector<int> dataIdx(dataSize);
  for (int i = 0; i != dataSize; i++)
  {
    dataIdx[i] = dataSize - i;
  }

  SECTION("parallel for")
  {
    std::vector<int> data(dataSize);
    // do some parallel operation if enabled
#ifdef USE_STDPAR
    std::for_each(std::execution::par_unseq, dataIdx.begin(), dataIdx.end(),
                [&](int& i) { data[i] = (dataSize - i) * i; });
#else // serial
    std::for_each(dataIdx.begin(), dataIdx.end(), 
                [&](int& i) { data[i] = (dataSize - i) * i; });
#endif

    // or using Amhoeba created macro
    std::vector<int> data2(dataSize);
    // do some parallel operation, the PAR macro takes care of if build supports
    std::for_each(PAR dataIdx.begin(), dataIdx.end(),
                  [&](int& i) { data2[i] = (dataSize - i) * i; });

    // check values in serial
    for (int i = 0; i != dataSize; i++)
    {
      CHECK(data[i] == data2[i]);
    }
  }

  SECTION("parallel transform")
  {
    std::vector<int> transformed_data(dataSize);
    std::vector<int> data(dataSize);
    std::transform(PAR dataIdx.begin(), dataIdx.end(), transformed_data.begin(),
                   [&](int& e) { return 2 * e + 1; });

    // check values in serial
    for (int i = 0; i != dataSize; i++)
    {
      CHECK(dataIdx[i] == (dataSize - i));
      CHECK(transformed_data[i] == (2 * (dataSize - i) + 1));
    }
  }

  SECTION("parallel reduction")
  {
    long long sum = std::reduce(PAR dataIdx.begin(), dataIdx.end(), (long long)0);
    CHECK(sum == dataSize * (dataSize + 1) / 2);
  }

  SECTION("parallel sort")
  {
    // Create a vector of random integers
    std::vector<int> data(dataSize);
    // Generate random numbers in parallel
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(1, 100);
    std::for_each(PAR data.begin(), data.end(), [&](int& n) { n = distrib(gen); });
    // Sort the data in parallel
    std::sort(PAR data.begin(), data.end());

    // check for sane values in serial
    CHECK(data.front() <= data.back());
    for (int i = 1; i != dataSize - 1; i++)
    {
      CHECK(data[i] >= data[i - 1]);
      CHECK(data[i] <= data[i + 1]);
    }
  }
}
```
