## DeltaPartitioner

DeltaPartitioner is a software version history partitioning tool for Java projects. It applies delta-debugging sytle partitioning algorithm to partition the set of commits in a selected range of software history, producing 1-minimal semantic history slice (a sub-sequence of a change history that preserves the functionality of interest, which is defined by a set of test cases). 


#### Usage

1. Download delta_partitioner.jar.
2. Write a simple configuration file. Please refer to the template we provide in this directory.
3. Write a simple python script, providing the commands of compiling source code and executing test cases. Please refer to the template we provide in this directory.
2. Run the command `java -jar delta_partitioner.jar -c /path/configuration_file_name -e delta`
3. Go to the end of the output. The 1-minimal semantic history slice can be found at the lines starting with "H\*".  
