# DoSC

![DoSc logo](http://www.cs.toronto.edu/~polaris/img/benchmark/DoSC.png "DoSC")

<!--This repository is for MSR 2017 paper - *A Dataset for Dynamic Discovery of Semantic Changes in Version Controlled Software Histories*.-->
## About
DoSC is a dataset created for benchmarking semantic history slicing techniques.

## License
DoSC is distributed under Apache license. See [license.txt](https://github.com/Chenguang-Zhu/DoSC/blob/master/license.txt) for details.

## People
**Chenguang Zhu**  czhu@cs.toronto.edu  
**Yi Li**  liyi@cs.toronto.edu  
**Julia Rubin**  mjulia@ece.ubc.ca  
**Marsha Chechik**  chechik@cs.toronto.edu    

## Dataset
### Usage
1. Pick a functionality from the dataset. (See the table below.)
2. View its meta-data file. See [meta-data collections](https://github.com/Chenguang-Zhu/DoSC/blob/master/meta-data).
3. Access the repository of the project via the link provided in the `project url` field of the meta-data.
4. Use `git clone` command to clone the project repository to the user's local file system.
5. Extract the names of all test methods listed in the `test suite`	field of the meta-data.
6. Use the extracted test cases and the history segment specified by the starting point (field `history start`) and the ending point (field `history end`) as the input on which to run the history slicing tool.
7. Compare the resulting semantic history slice with the 1-minimal ground truth we provide (field `history slice`).
8. Repeat the steps 1-6 until the evaluation is sufficient. 

### Overview of the dataset
#### Columns in the table:
>+ **Functionality ID**: The JIRA issue key of the functionality - a unique identifier originally assigned by developers in the JIRA issue tracking system.
>+ **History Start**: The starting point of the history segment where the functionality was developed. It is the SHA-1 ID of a release commit, which is the closest release version before the functionality was developed.
>+ **History End**: The ending point of the history segment where the functionality was developed. It is the SHA-1 ID of the closest release version after the functionality was developed.
>+ **#Commits**: The length of history of developing a functionality.
>+ **#Files Edited**: The number of files changed during the development of the functionality.
>+ **#LOC +**: The number of code lines inserted during the development of the functionality.
>+ **#LOC -**: The number of code lines deleted during the development of the functionality.
>+ **#Test Cases**: The number of test cases in the associated test suite of the functionality.
>+ **Slice Size**: The size of the 1-minimal history slice of each functionality, expressed as the number of commits.
>+ **Reduction %**: *Reduction rate*. It stands for the proportion of the commits unrelated to its implementation.

|Functionality ID|History Start|History End|#Commits|#Files Edited|#LOC +|#LOC -|#Test cases|Slice Size|Reduction %| 
|:-------------:|-------------:|-----------:|--------:|-------------:|------:|------:|-----------:|----------:|--:|
|<sub>LANG-825</sub>|<sub>bae9f7c3</sub>|<sub>15a51f1d</sub>|<sub>475</sub>|<sub>265</sub>|<sub>27630</sub>|<sub>11935</sub>|<sub>2</sub>|<sub>118</sub>|<sub>75.16</sub>|
|<sub>LANG-839</sub>|<sub>bae9f7c3</sub>|<sub>15a51f1d</sub>|<sub>475</sub>|<sub>265</sub>|<sub>27630</sub>|<sub>11935</sub>|<sub>2</sub>|<sub>200</sub>|<sub>57.89</sub>|
|<sub>LANG-841</sub>|<sub>bae9f7c3</sub>|<sub>15a51f1d</sub>|<sub>475</sub>|<sub>265</sub>|<sub>27630</sub>|<sub>11935</sub>|<sub>2</sub>|<sub>200</sub>|<sub>57.89</sub>|
|<sub>LANG-906</sub>|<sub>bae9f7c3</sub>|<sub>15a51f1d</sub>|<sub>475</sub>|<sub>265</sub>|<sub>27630</sub>|<sub>11935</sub>|<sub>5</sub>|<sub>1</sub>|<sub>99.79</sub>|
|<sub>LANG-834</sub>|<sub>c4ecd75</sub>|<sub>66a3717</sub>|<sub>179</sub>|<sub>121</sub>|<sub>6889</sub>|<sub>1807</sub>|<sub>12</sub>|<sub>12</sub>|<sub>93.3</sub>|
|<sub>LANG-944</sub>|<sub>c4ecd75</sub>|<sub>66a3717</sub>|<sub>179</sub>|<sub>121</sub>|<sub>6889</sub>|<sub>1807</sub>|<sub>1</sub>|<sub>24</sub>|<sub>86.59</sub>|
|<sub>LANG-993</sub>|<sub>24767d6</sub>|<sub>76cc69c</sub>|<sub>262</sub>|<sub>146</sub>|<sub>6741</sub>|<sub>2076</sub>|<sub>10</sub>|<sub>6</sub>|<sub>97.71</sub>|
|<sub>LANG-999</sub>|<sub>24767d6</sub>|<sub>76cc69c</sub>|<sub>262</sub>|<sub>146</sub>|<sub>6741</sub>|<sub>2076</sub>|<sub>5</sub>|<sub>15</sub>|<sub>94.27</sub>|
|<sub>LANG-1006</sub>|<sub>24767d6</sub>|<sub>76cc69c</sub>|<sub>262</sub>|<sub>146</sub>|<sub>6741</sub>|<sub>2076</sub>|<sub>2</sub>|<sub>14</sub>|<sub>94.66</sub>|
|<sub>LANG-1033</sub>|<sub>24767d6</sub>|<sub>76cc69c</sub>|<sub>262</sub>|<sub>146</sub>|<sub>6741</sub>|<sub>2076</sub>|<sub>1</sub>|<sub>22</sub>|<sub>91.6</sub>|
|<sub>LANG-1088</sub>|<sub>24767d6</sub>|<sub>76cc69c</sub>|<sub>262</sub>|<sub>146</sub>|<sub>6741</sub>|<sub>2076</sub>|<sub>2</sub>|<sub>1</sub>|<sub>99.62</sub>|
|<sub>LANG-536</sub>|<sub>24767d6</sub>|<sub>76cc69c</sub>|<sub>262</sub>|<sub>146</sub>|<sub>6741</sub>|<sub>2076</sub>|<sub>17</sub>|<sub>30</sub>|<sub>88.55</sub>|
|<sub>LANG-883</sub>|<sub>24767d6</sub>|<sub>76cc69c</sub>|<sub>262</sub>|<sub>146</sub>|<sub>6741</sub>|<sub>2076</sub>|<sub>1</sub>|<sub>36</sub>|<sub>86.26</sub>|
|<sub>LANG-1015</sub>|<sub>24767d6</sub>|<sub>76cc69c</sub>|<sub>262</sub>|<sub>146</sub>|<sub>6741</sub>|<sub>2076</sub>|<sub>9</sub>|<sub>39</sub>|<sub>85.11</sub>|
|<sub>LANG-1021</sub>|<sub>24767d6</sub>|<sub>76cc69c</sub>|<sub>262</sub>|<sub>146</sub>|<sub>6741</sub>|<sub>2076</sub>|<sub>16</sub>|<sub>28</sub>|<sub>89.31</sub>|
|<sub>LANG-1080</sub>|<sub>24767d6</sub>|<sub>76cc69c</sub>|<sub>262</sub>|<sub>146</sub>|<sub>6741</sub>|<sub>2076</sub>|<sub>8</sub>|<sub>38</sub>|<sub>85.5</sub>|
|<sub>LANG-1093</sub>|<sub>24767d6</sub>|<sub>76cc69c</sub>|<sub>262</sub>|<sub>146</sub>|<sub>6741</sub>|<sub>2076</sub>|<sub>2</sub>|<sub>63</sub>|<sub>75.95
|<sub>LANG-1050</sub>|<sub>0d5d666</sub>|<sub>36f98d8</sub>|<sub>515</sub>|<sub>309</sub>|<sub>18885</sub>|<sub>6395</sub>|<sub>4</sub>|<sub>8</sub>|<sub>98.45</sub>|
|<sub>LANG-1074</sub>|<sub>0d5d666</sub>|<sub>36f98d8</sub>|<sub>515</sub>|<sub>309</sub>|<sub>18885</sub>|<sub>6395</sub>|<sub>9</sub>|<sub>6</sub>|<sub>98.83</sub>|
|<sub>LANG-1119</sub>|<sub>0d5d666</sub>|<sub>36f98d8</sub>|<sub>515</sub>|<sub>309</sub>|<sub>18885</sub>|<sub>6395</sub>|<sub>1</sub>|<sub>1</sub>|<sub>99.81</sub>|
|<sub>CALCITE-627</sub>|<sub>f10ea367</sub>|<sub>d60f2aa3</sub>|<sub>51</sub>|<sub>135</sub>|<sub>8274</sub>|<sub>1446</sub>|<sub>2</sub>|<sub>19</sub>|<sub>62.75</sub>|
|<sub>CALCITE-655</sub>|<sub>f10ea367</sub>|<sub>d60f2aa3</sub>|<sub>51</sub>|<sub>135</sub>|<sub>8274</sub>|<sub>1446</sub>|<sub>1</sub>|<sub>19</sub>|<sub>62.75</sub>|
|<sub>CALCITE-674</sub>|<sub>d60f2aa3</sub>|<sub>495f1859</sub>|<sub>59</sub>|<sub>196</sub>|<sub>14861</sub>|<sub>9173</sub>|<sub>1</sub>|<sub>11</sub>|<sub>81.36</sub>|
|<sub>CALCITE-718</sub>|<sub>495f1859</sub>|<sub>0c0c203d</sub>|<sub>92</sub>|<sub>304</sub>|<sub>21348</sub>|<sub>7686</sub>|<sub>1</sub>|<sub>14</sub>|<sub>84.78</sub>|
|<sub>CALCITE-758</sub>|<sub>495f1859</sub>|<sub>0c0c203d</sub>|<sub>92</sub>|<sub>304</sub>|<sub>21348</sub>|<sub>7686</sub>|<sub>1</sub>|<sub>1</sub>|<sub>98.91</sub>|
|<sub>CALCITE-811</sub>|<sub>495f1859</sub>|<sub>0c0c203d</sub>|<sub>92</sub>|<sub>304</sub>|<sub>21348</sub>|<sub>7686</sub>|<sub>1</sub>|<sub>1</sub>|<sub>98.91</sub>|
|<sub>CALCITE-803</sub>|<sub>495f1859</sub>|<sub>0c0c203d</sub>|<sub>92</sub>|<sub>304</sub>|<sub>21348</sub>|<sub>7686</sub>|<sub>1</sub>|<sub>1</sub>|<sub>98.91</sub>|
|<sub>CALCITE-925</sub>|<sub>0c0c203d</sub>|<sub>ba6e43c6</sub>|<sub>120</sub>|<sub>468</sub>|<sub>68314</sub>|<sub>6096</sub>|<sub>3</sub>|<sub>1</sub>|<sub>99.17</sub>|
|<sub>CALCITE-767</sub>|<sub>ba6e43c6</sub>|<sub>c4d346b0</sub>|<sub>103</sub>|<sub>465</sub>|<sub>31647</sub>|<sub>13594</sub>|<sub>1</sub>|<sub>8</sub>|<sub>92.23</sub>|
|<sub>CALCITE-996</sub>|<sub>ba6e43c6</sub>|<sub>c4d346b0</sub>|<sub>103</sub>|<sub>465</sub>|<sub>31647</sub>|<sub>13594</sub>|<sub>1</sub>|<sub>1</sub>|<sub>99.03</sub>|
|<sub>CALCITE-1003</sub>|<sub>ba6e43c6</sub>|<sub>c4d346b0</sub>|<sub>103</sub>|<sub>465</sub>|<sub>31647</sub>|<sub>13594</sub>|<sub>25</sub>|<sub>14</sub>|<sub>86.41</sub>|
|<sub>CALCITE-1028</sub>|<sub>ba6e43c6</sub>|<sub>c4d346b0</sub>|<sub>103</sub>|<sub>465</sub>|<sub>31647</sub>|<sub>13594</sub>|<sub>1</sub>|<sub>6</sub>|<sub>94.17</sub>|
|<sub>CALCITE-1168</sub>|<sub>8eebfc6d</sub>|<sub>aeb6bf14</sub>|<sub>122</sub>|<sub>399</sub>|<sub>30975</sub>|<sub>4800</sub>|<sub>3</sub>|<sub>2</sub>|<sub>98.36</sub>|
|<sub>CALCITE-1200</sub>|<sub>8eebfc6d</sub>|<sub>aeb6bf14</sub>|<sub>122</sub>|<sub>399</sub>|<sub>30975</sub>|<sub>4800</sub>|<sub>3</sub>|<sub>2</sub>|<sub>98.36</sub>|
|<sub>CALCITE-991</sub>|<sub>aeb6bf14</sub>|<sub>08c56b15</sub>|<sub>78</sub>|<sub>295</sub>|<sub>14908</sub>|<sub>3637</sub>|<sub>5</sub>|<sub>1</sub>|<sub>98.72</sub>|
|<sub>CALCITE-1288</sub>|<sub>aeb6bf14</sub>|<sub>08c56b15</sub>|<sub>78</sub>|<sub>295</sub>|<sub>14908</sub>|<sub>3637</sub>|<sub>1</sub>|<sub>6</sub>|<sub>92.31</sub>|
|<sub>CALCITE-1309</sub>|<sub>aeb6bf14</sub>|<sub>08c56b15</sub>|<sub>78</sub>|<sub>295</sub>|<sub>14908</sub>|<sub>3637</sub>|<sub>8</sub>|<sub>7</sub>|<sub>91.03</sub>|
|<sub>CALCITE-1337</sub>|<sub>aeb6bf14</sub>|<sub>08c56b15</sub>|<sub>78</sub>|<sub>295</sub>|<sub>14908</sub>|<sub>3637</sub>|<sub>2</sub>|<sub>5</sub>|<sub>93.59</sub>|
|<sub>MNG-4904</sub>|<sub>b175144</sub>|<sub>308d4d4</sub>|<sub>51</sub>|<sub>78</sub>|<sub>1816</sub>|<sub>713</sub>|<sub>1</sub>|<sub>7</sub>|<sub>86.27</sub>|
|<sub>MNG-4909</sub>|<sub>b175144</sub>|<sub>308d4d4</sub>|<sub>51</sub>|<sub>78</sub>|<sub>1816</sub>|<sub>713</sub>|<sub>2</sub>|<sub>7</sub>|<sub>86.27</sub>|
|<sub>MNG-4910</sub>|<sub>b175144</sub>|<sub>308d4d4</sub>|<sub>51</sub>|<sub>78</sub>|<sub>1816</sub>|<sub>713</sub>|<sub>1</sub>|<sub>7</sub>|<sub>86.27</sub>|
|<sub>MNG-4953</sub>|<sub>38ced22</sub>|<sub>0023226</sub>|<sub>47</sub>|<sub>96</sub>|<sub>2448</sub>|<sub>329</sub>|<sub>1</sub>|<sub>6</sub>|<sub>87.23</sub>|
|<sub>MNG-5159</sub>|<sub>089a9f8</sub>|<sub>6d37598</sub>|<sub>120</sub>|<sub>318</sub>|<sub>3003</sub>|<sub>1098</sub>|<sub>4</sub>|<sub>2</sub>|<sub>98.33</sub>|
|<sub>MNG-5530</sub>|<sub>b7e3ce2</sub>|<sub>ea8b2b0</sub>|<sub>97</sub>|<sub>160</sub>|<sub>4431</sub>|<sub>4144</sub>|<sub>1</sub>|<sub>1</sub>|<sub>98.97</sub>|
|<sub>MNG-5549</sub>|<sub>b7e3ce2</sub>|<sub>ea8b2b0</sub>|<sub>97</sub>|<sub>160</sub>|<sub>4431</sub>|<sub>4144</sub>|<sub>1</sub>|<sub>13</sub>|<sub>86.6</sub>|
|<sub>MNG-5754</sub>|<sub>d13c288</sub>|<sub>cab6659</sub>|<sub>97</sub>|<sub>235</sub>|<sub>9500</sub>|<sub>3930</sub>|<sub>4</sub>|<sub>8</sub>|<sub>91.75</sub>|
|<sub>MNG-5755</sub>|<sub>d13c288</sub>|<sub>cab6659</sub>|<sub>97</sub>|<sub>235</sub>|<sub>9500</sub>|<sub>3930</sub>|<sub>5</sub>|<sub>7</sub>|<sub>92.78</sub>|
|<sub>MNG-5767</sub>|<sub>d13c288</sub>|<sub>cab6659</sub>|<sub>97</sub>|<sub>235</sub>|<sub>9500</sub>|<sub>3930</sub>|<sub>3</sub>|<sub>21</sub>|<sub>78.35</sub>|
|<sub>MNG-5805</sub>|<sub>0ddab5f</sub>|<sub>bb52d85</sub>|<sub>98</sub>|<sub>341</sub>|<sub>3751</sub>|<sub>3030</sub>|<sub>2</sub>|<sub>11</sub>|<sub>88.78</sub>|
|<sub>COMPRESS-295</sub>|<sub>083e7a4</sub>|<sub>1dcab3f</sub>|<sub>169</sub>|<sub>181</sub>|<sub>6638</sub>|<sub>1580</sub>|<sub>2</sub>|<sub>1</sub>|<sub>99.41</sub>|
|<sub>COMPRESS-296</sub>|<sub>083e7a4</sub>|<sub>1dcab3f</sub>|<sub>169</sub>|<sub>181</sub>|<sub>6638</sub>|<sub>1580</sub>|<sub>3</sub>|<sub>37</sub>|<sub>78.11</sub>|
|<sub>COMPRESS-313</sub>|<sub>083e7a4</sub>|<sub>1dcab3f</sub>|<sub>169</sub>|<sub>181</sub>|<sub>6638</sub>|<sub>1580</sub>|<sub>3</sub>|<sub>40</sub>|<sub>76.33</sub>|
|<sub>COMPRESS-327</sub>|<sub>99bc508</sub>|<sub>b29395d</sub>|<sub>148</sub>|<sub>144</sub>|<sub>4644</sub>|<sub>2006</sub>|<sub>18</sub>|<sub>26</sub>|<sub>82.43</sub>|
|<sub>COMPRESS-368</sub>|<sub>99bc508</sub>|<sub>b29395d</sub>|<sub>148</sub>|<sub>144</sub>|<sub>4644</sub>|<sub>2006</sub>|<sub>6</sub>|<sub>12</sub>|<sub>91.89</sub>|
|<sub>COMPRESS-369</sub>|<sub>99bc508</sub>|<sub>b29395d</sub>|<sub>148</sub>|<sub>144</sub>|<sub>4644</sub>|<sub>2006</sub>|<sub>2</sub>|<sub>10</sub>|<sub>93.24</sub>|
|<sub>COMPRESS-373</sub>|<sub>99bc508</sub>|<sub>b29395d</sub>|<sub>148</sub>|<sub>144</sub>|<sub>4644</sub>|<sub>2006</sub>|<sub>1</sub>|<sub>14</sub>|<sub>90.54</sub>|
|<sub>COMPRESS-374</sub>|<sub>99bc508</sub>|<sub>b29395d</sub>|<sub>148</sub>|<sub>144</sub>|<sub>4644</sub>|<sub>2006</sub>|<sub>8</sub>|<sub>15</sub>|<sub>89.86</sub>|
|<sub>COMPRESS-375</sub>|<sub>99bc508</sub>|<sub>b29395d</sub>|<sub>148</sub>|<sub>144</sub>|<sub>4644</sub>|<sub>2006</sub>|<sub>2</sub>|<sub>1</sub>|<sub>99.32</sub>|
|<sub>FLUME-1710</sub>|<sub>31d45f1b</sub>|<sub>f7560038</sub>|<sub>133</sub>|<sub>258</sub>|<sub>15949</sub>|<sub>2783</sub>|<sub>1</sub>|<sub>1</sub>|<sub>99.25</sub>|
|<sub>FLUME-2052</sub>|<sub>cda3bd10</sub>|<sub>31d45f1b</sub>|<sub>101</sub>|<sub>181</sub>|<sub>14742</sub>|<sub>3097</sub>|<sub>5</sub>|<sub>3</sub>|<sub>97.03</sub>|
|<sub>FLUME-2056</sub>|<sub>cda3bd10</sub>|<sub>31d45f1b</sub>|<sub>101</sub>|<sub>181</sub>|<sub>14742</sub>|<sub>3097</sub>|<sub>1</sub>|<sub>5</sub>|<sub>95.05</sub>|
|<sub>FLUME-2130</sub>|<sub>cda3bd10</sub>|<sub>31d45f1b</sub>|<sub>101</sub>|<sub>181</sub>|<sub>14742</sub>|<sub>3097</sub>|<sub>1</sub>|<sub>3</sub>|<sub>97.03</sub>|
|<sub>FLUME-2206</sub>|<sub>cda3bd10</sub>|<sub>31d45f1b</sub>|<sub>101</sub>|<sub>181</sub>|<sub>14742</sub>|<sub>3097</sub>|<sub>1</sub>|<sub>4</sub>|<sub>96.04</sub>|
|<sub>FLUME-2498</sub>|<sub>f7560038</sub>|<sub>5e400ea8</sub>|<sub>100</sub>|<sub>428</sub>|<sub>17341</sub>|<sub>8187</sub>|<sub>17</sub>|<sub>65</sub>|<sub>35</sub>|
|<sub>FLUME-2628</sub>|<sub>f7560038</sub>|<sub>5e400ea8</sub>|<sub>100</sub>|<sub>428</sub>|<sub>17341</sub>|<sub>8187</sub>|<sub>7</sub>|<sub>1</sub>|<sub>99</sub>|
|<sub>FLUME-2955</sub>|<sub>f7560038</sub>|<sub>5e400ea8</sub>|<sub>100</sub>|<sub>428</sub>|<sub>17341</sub>|<sub>8187</sub>|<sub>1</sub>|<sub>65</sub>|<sub>35</sub>|
|<sub>FLUME-2982</sub>|<sub>f7560038</sub>|<sub>5e400ea8</sub>|<sub>100</sub>|<sub>428</sub>|<sub>17341</sub>|<sub>8187</sub>|<sub>2</sub>|<sub>35</sub>|<sub>65</sub>|
|<sub>PDFBOX-3307</sub>|<sub>a281f71</sub>|<sub>9e102f2</sub>|<sub>37</sub>|<sub>42</sub>|<sub>1138</sub>|<sub>268</sub>|<sub>2</sub>|<sub>1</sub>|<sub>97.3</sub>|
|<sub>PDFBOX-3069</sub>|<sub>3b5ae83</sub>|<sub>5848e90</sub>|<sub>272</sub>|<sub>255</sub>|<sub>9737</sub>|<sub>5398</sub>|<sub>2</sub>|<sub>1</sub>|<sub>99.63</sub>|
|<sub>PDFBOX-3418</sub>|<sub>3b5ae83</sub>|<sub>5848e90</sub>|<sub>272</sub>|<sub>255</sub>|<sub>9737</sub>|<sub>5398</sub>|<sub>2</sub>|<sub>3</sub>|<sub>98.9</sub>|
|<sub>PDFBOX-3461</sub>|<sub>3b5ae83</sub>|<sub>5848e90</sub>|<sub>272</sub>|<sub>255</sub>|<sub>9737</sub>|<sub>5398</sub>|<sub>24</sub>|<sub>3</sub>|<sub>98.9</sub>|
|<sub>PDFBOX-3262</sub>|<sub>7c1a2c8</sub>|<sub>69a8e03</sub>|<sub>162</sub>|<sub>135</sub>|<sub>3295</sub>|<sub>814</sub>|<sub>1</sub>|<sub>2</sub>|<sub>98.77</sub>|
|<sub>CONFIGURATION-466</sub>|<sub>5270237</sub>|<sub>f81ff1a</sub>|<sub>252</sub>|<sub>694</sub>|<sub>79920</sub>|<sub>80096</sub>|<sub>3</sub>|<sub>13</sub>|<sub>94.84</sub>|
|<sub>CONFIGURATION-624</sub>|<sub>89428f1</sub>|<sub>9fb4ad8</sub>|<sub>50</sub>|<sub>34</sub>|<sub>1201</sub>|<sub>655</sub>|<sub>11</sub>|<sub>48</sub>|<sub>4</sub>|
|<sub>CONFIGURATION-626</sub>|<sub>89428f1</sub>|<sub>9fb4ad8</sub>|<sub>50</sub>|<sub>34</sub>|<sub>1201</sub>|<sub>655</sub>|<sub>4</sub>|<sub>1</sub>|<sub>98</sub>|
|<sub>NET-436</sub>|<sub>d8812a3</sub>|<sub>4c3860e</sub>|<sub>77</sub>|<sub>99</sub>|<sub>2357</sub>|<sub>774</sub>|<sub>5</sub>|<sub>7</sub>|<sub>90.9</sub>|
|<sub>NET-525</sub>|<sub>d483631</sub>|<sub>abd6711</sub>|<sub>269</sub>|<sub>233</sub>|<sub>6845</sub>|<sub>2393</sub>|<sub>14</sub>|<sub>40</sub>|<sub>85.13</sub>|
|<sub>NET-527</sub>|<sub>d483631</sub>|<sub>abd6711</sub>|<sub>269</sub>|<sub>233</sub>|<sub>6845</sub>|<sub>2393</sub>|<sub>1</sub>|<sub>40</sub>|<sub>85.13</sub>|
|<sub>CSV-159</sub>|<sub>b230a6f5</sub>|<sub>7310e5c6</sub>|<sub>79</sub>|<sub>28</sub>|<sub>1640</sub>|<sub>713</sub>|<sub>1</sub>|<sub>10</sub>|<sub>87.34</sub>|
|<sub>CSV-175</sub>|<sub>b230a6f5</sub>|<sub>7310e5c6</sub>|<sub>79</sub>|<sub>28</sub>|<sub>1640</sub>|<sub>713</sub>|<sub>11</sub>|<sub>48</sub>|<sub>39.24</sub>|
|<sub>CSV-179</sub>|<sub>b230a6f5</sub>|<sub>7310e5c6</sub>|<sub>79</sub>|<sub>28</sub>|<sub>1640</sub>|<sub>713</sub>|<sub>1</sub>|<sub>56</sub>|<sub>29.11</sub>|
|<sub>CSV-180</sub>|<sub>b230a6f5</sub>|<sub>7310e5c6</sub>|<sub>79</sub>|<sub>28</sub>|<sub>1640</sub>|<sub>713</sub>|<sub>2</sub>|<sub>56</sub>|<sub>29.11</sub>|
|<sub>IO-126</sub>|<sub>61519de4</sub>|<sub>f6724182</sub>|<sub>140</sub>|<sub>140</sub>|<sub>7365</sub>|<sub>1242</sub>|<sub>2</sub>|<sub>6</sub>|<sub>95.71</sub>|
|<sub>IO-129</sub>|<sub>61519de4</sub>|<sub>f6724182</sub>|<sub>140</sub>|<sub>140</sub>|<sub>7365</sub>|<sub>1242</sub>|<sub>7</sub>|<sub>10</sub>|<sub>92.86</sub>|
|<sub>IO-130</sub>|<sub>61519de4</sub>|<sub>f6724182</sub>|<sub>140</sub>|<sub>140</sub>|<sub>7365</sub>|<sub>1242</sub>|<sub>4</sub>|<sub>11</sub>|<sub>92.14</sub>|
|<sub>IO-135</sub>|<sub>61519de4</sub>|<sub>f6724182</sub>|<sub>140</sub>|<sub>140</sub>|<sub>7365</sub>|<sub>1242</sub>|<sub>4</sub>|<sub>23</sub>|<sub>83.57</sub>|
|<sub>IO-138</sub>|<sub>61519de4</sub>|<sub>f6724182</sub>|<sub>140</sub>|<sub>140</sub>|<sub>7365</sub>|<sub>1242</sub>|<sub>7</sub>|<sub>13</sub>|<sub>90.71</sub>|
|<sub>IO-144</sub>|<sub>61519de4</sub>|<sub>f6724182</sub>|<sub>140</sub>|<sub>140</sub>|<sub>7365</sub>|<sub>1242</sub>|<sub>2</sub>|<sub>1</sub>|<sub>99.29</sub>|
|<sub>IO-145</sub>|<sub>61519de4</sub>|<sub>f6724182</sub>|<sub>140</sub>|<sub>140</sub>|<sub>7365</sub>|<sub>1242</sub>|<sub>2</sub>|<sub>61</sub>|<sub>56.43</sub>|
|<sub>IO-148</sub>|<sub>61519de4</sub>|<sub>f6724182</sub>|<sub>140</sub>|<sub>140</sub>|<sub>7365</sub>|<sub>1242</sub>|<sub>2</sub>|<sub>30</sub>|<sub>78.57</sub>|
|<sub>IO-153</sub>|<sub>61519de4</sub>|<sub>f6724182</sub>|<sub>140</sub>|<sub>140</sub>|<sub>7365</sub>|<sub>1242</sub>|<sub>6</sub>|<sub>56</sub>|<sub>60</sub>|
|<sub>IO-173</sub>|<sub>8de491fc</sub>|<sub>b1b9f1af</sub>|<sub>136</sub>|<sub>182</sub>|<sub>5647</sub>|<sub>1681</sub>|<sub>2</sub>|<sub>32</sub>|<sub>76.47</sub>|
|<sub>IO-275</sub>|<sub>8de491fc</sub>|<sub>b1b9f1af</sub>|<sub>136</sub>|<sub>182</sub>|<sub>5647</sub>|<sub>1681</sub>|<sub>2</sub>|<sub>1</sub>|<sub>99.26</sub>|
|<sub>IO-288</sub>|<sub>8de491fc</sub>|<sub>b1b9f1af</sub>|<sub>136</sub>|<sub>182</sub>|<sub>5647</sub>|<sub>1681</sub>|<sub>81</sub>|<sub>16</sub>|<sub>88.24</sub>|
|<sub>IO-290</sub>|<sub>8de491fc</sub>|<sub>b1b9f1af</sub>|<sub>136</sub>|<sub>182</sub>|<sub>5647</sub>|<sub>1681</sub>|<sub>2</sub>|<sub>5</sub>|<sub>96.32</sub>|
|<sub>IO-291</sub>|<sub>8de491fc</sub>|<sub>b1b9f1af</sub>|<sub>136</sub>|<sub>182</sub>|<sub>5647</sub>|<sub>1681</sub>|<sub>10</sub>|<sub>24</sub>|<sub>82.35</sub>|
|<sub>IO-297</sub>|<sub>8de491fc</sub>|<sub>b1b9f1af</sub>|<sub>136</sub>|<sub>182</sub>|<sub>5647</sub>|<sub>1681</sub>|<sub>9</sub>|<sub>13</sub>|<sub>90.44</sub>|
|<sub>IO-305</sub>|<sub>8de491fc</sub>|<sub>b1b9f1af</sub>|<sub>136</sub>|<sub>182</sub>|<sub>5647</sub>|<sub>1681</sub>|<sub>10</sub>|<sub>83</sub>|<sub>38.97</sub>|
