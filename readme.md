# Regular unimodular Hilbert triangulations of thick te-interlaces

This is a companion directory containing the polymake code and figures describing explicitly the combinatorics of the regular unimodular Hilbert triangulations of thick te-interlaces of size $4$ and $6$ in each of the two different types of Hilbert basis.
Namely, types
1) $\mathcal{H}(C) = \left\{\frac{1}{2} (r^i + r^j)\right\}_{i,j\in\{1,\ldots,n\}}\cup\left\{\frac{1}{4}\sum_{j} r^j\right\},$
2) $\mathcal{H}(C) = \left\{\frac{1}{2} (r^i + r^j)\right\}_{i,j\in\{1,\ldots,n\}}\cup\left\{\frac{3}{4}r^i+\frac{1}{4}\sum_{j\neq i} r^j\right\}_{i\in\{1,\ldots,n\}}.$

In the different folders `./n4_type1`, `./n4_type2`, `./n6_type1`, and `./n6_type2`, each figure corresponds to a set of $n$ Hilbert basis elements generating a unimodular Hilbert cone in one of the four regular triangulations, for each pair $(n,t)$ for $n=4,6$ the size of the thick te-interlace and $t=1,2$ the type of Hilbert basis.

In each figure, one can find $n$ vertices labelled from $1$ to $n$ and colored loops, edges and circles that correspond to Hilbert basis elements as follows.

### In both types
- $r^i$ for $i=1,\ldots,n$ is represented by a blue loop at vertex $i$ in each figure,
- $m^{ij}:=\frac{1}{2} (r^i + r^j)$ for $i\neq j$ is represented by a blue edge $ij$ in each figure.

### Type 1

In that case there is a single additional Hilbert basis element:
- $h:=\frac{1}{4}\sum_{j} r^j$ that is represented by a green circle in the center of each figure.


### Type 2

In that case there is a third type of of Hilbert basis elements:
- $h^i:=\frac{3}{4}r^i+\frac{1}{4}\sum_{j\neq i} r^j$, for $i=1,\ldots,n$, that is represented by a red circle around vertex $i$ in each figure.