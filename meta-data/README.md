## Meta-data

This directory contains meta-data files of all the functionalities in the dataset. 


### Data schema

`id` is the issue key of the functionality on JIRA -- a unique identifier originally assigned by developers 
in the issue tracking system.

`description` is the developers' description of the functionality, found on the JIRA release notes page.

`project` designates the project in which the functionality belongs. The project's `name` and `url` are provided.

`issue url` designates the link of the issue report of the functionality on JIRA. The issue report page contains detailed information and activity log of the functionality.

`history start` specifies the starting point of the history segment where the functionality was developed. It is the SHA-1 ID of a release commit, which is the closest release version before the functionality was developed.

`history end` specifies the ending point of the history segment where the functionality was developed. It is the SHA-1 ID of the closest release version after the functionality was developed.

`test suite` designates the associated test suite of the functionality. The test suite exercises the behaviors of the functionality. All the test methods of the test suite are listed in this field.

`history slice` designates the 1-minimal semantic history slice with respect to the functionality, i.e., the ground truth for semantic history slicing.
