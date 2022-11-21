/**
00 : 31 : 30 Remaining

Backend Development Test | Round 2
Question 2
IDE Submission
Taller Or Shorter
Question Name: Taller Or Shorter

Problem Statement

Antonio is one of the organizing members of this year’s Boys Scout Campaign. Antonio has been allotted N boys this year. Antonio arranged all these boys in a line from 1 to N.

Now he made a comparison array based on the heights of these boys. Comparison array is an array of size N-1, where the ith element is :

1, if the height of the ith boy is more than the height of the (i+1)th boy.
-1, if the height of the ith student is less than the height of the (i+1)th student.
0, if the height of the ith student is equal to the height of the (i+1)th student.
Now all the boys have gone home and Antonio has to answer Q queries :

In the ith query, he will be given two integers a and b and he has to tell if the height of the ath boy is more than, equal to, or less than the height of the bth boy.
Antonio is facing difficulties in answering the queries and asks his coder friend(you) for help. Given the comparison array, answer the Q queries for Antonio.

In each query print “1”(without quotes) if ath boy is taller than bth boy, “-1” if ath boy is shorter than bth boy, “0” is the ath and the bth boy have the same height. If for any query the information is insufficient print “Not Possible”(without quotes) instead.

Input Format

First line contains a single integer denoting N.
Next line contains N-1 space separated integers denoting the elements of the comparison array.
Next line contains a single integer denoting Q.
Next Q lines contains two space separated integers denoting a and b for each of the queries.
Output Format

For each query print “1”(without quotes) if ath boy is taller than bth boy, “-1” if ath boy is shorter than bth boy, “0” is the ath and the bth boy have the same height.
Print the answer for every query in a separate line.
Constraints

2<=N<=105
1<=Q<=105
1<=a,b<=N
a!=b
Sample Input 1

4

1 0 -1

3

1 2

1 4

2 4

Sample Output 1

1

Not Possible

-1

Explanation of Sample 1

Query 1 :

Clearly 1 has more height than 2, as A1 = 1.
Query 3 :

The heights of students 2 and 3 are equal as A2 = 0. As A3 = -1, the height of student 3 is less than the height of 4. Hence the height of student 2 is also less than the height of student 4.
Query 2 :

Consider that the heights of the students were: [10 8 8 9] and [10 8 8 11]. For both these heights, the comparison array is [1 0 -1]. But in the first case height of the 1st student is more than the height of the 4th student, and in the second case height of the 1st student is less than the height of the 4th student.
Hence we can’t say which one is greater/smaller from the comparison array.


Things to Note for the Candidate:



 You can use your own IDE like Visual Studio Code, Eclipse, or any other IDE that you are comfortable with to build your solution code.

The IDE provided on the platform is purely for submission. Avoid using the IDE for coding out the solution.

Test against any custom input in your own IDE. In the IDE provided on the platform, you cannot pass custom test cases and see the output.

Use standard input and standard output in your program for the IDE to run the test cases smoothly against your code. We are giving a sample problem statement along with a solution that will pass the test cases in the IDE. - Sample Problem Statement (Right Click and Open in New Tab to view.)


Code in your favorite IDE and paste in the above widget
Previous

Submit & Next
Assess your algo
Round 2 | Questions
1
Question 1
2
Question 2
0 Submitted
2 Pending
Rec
Relevel
*/

/** 
 * Sample Input 1

4

1 0 -1

3

1 2

1 4

2 4

Sample Output 1

1
 */
public class TallerOrShorter{
    public static void main(String[] args){

    }
    // Function candidate has to implement
private nameTallerShorter(n,c,q,a,b)
{
  
}
private static driverCode(){
//Driver Code
var n = readline();
var temp = readline().trim();
var c = temp.split(" ");
for(i=0;i<n-1;i++)
{
    c[i]=Number(c[i]);
}

var q=readline();
var a=[];
var b=[];
for(i=0;i<q;i++)
{
    temp=readline().trim();
    s=temp.split(" ");
    a.push(s[0]);
    b.push(s[1]);
}

var num  = nameTallerShorter(n,c,q,a,b);
print(num);
}
}