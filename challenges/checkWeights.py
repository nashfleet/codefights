"""
You work for a company that makes weights that are used for balancing
    scales in high school science classes. The weights are shipped in
    boxes, and each box contains weights in a certain range. Each box
    is labeled with an array that represents the weights it contains.
    For example, a box of weights from 4 to 12 is labeled [4, 12]. The
    company never ships the same weight twice in a shipment.

A high school that needs a new set of weights orders a package that
    consists of several boxes. Once in a while, something goes wrong
    and either one weight falls off the line, or one weight is accidentally
    added to one of the boxes. Your job is to check each package before
    it goes out, and detect if this is the case.

Given the labels of the boxes about to be shipped and the actual
    packageWeight, you should return:

0 if the provided actual packageWeight equals the package weight you
    would expect according to the label;
a if weight a was accidentally added to the package;
-a if weight a is missing from the package.
"""
checkWeights = lambda b, p: p - sum(sum(range(i[0],i[1]+1)) for i in b)
