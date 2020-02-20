# I-WANT-TO-FIND-A-JOB

This repository contains all the material and information that I prepared for job hunting as a Software developer. Hope these information can help you receive your dream offer. May the code with you! Code long and prosper!

## Algorithm

- [Backtracking](./Algorithms/Backtracking)
- [Binary Search](./Algorithms/Binary%20Search)
- [Dynamic Programming](./Algorithms/Dynamic%20Programming)

## Online Practices

### 1. [Leetcode](https://leetcode.com/)

#### How to Leetcode Effectively (If time permitted):

1. Do Breadth-First Scan of “Easy” questions from each Topic on Leetcode
   - Try to get it right on the first try
   - Should be finishing these in < 10 minutes
   - Take note of which sections you struggled at (the following was for me)
2. Do more “Easy” questions from the topics you struggled at
3. Shuffle “Medium” problems
   - Only do the problems you are not 100% sure how to do
   - Start a 25 minute pomodoro timer and attempt to solve it
   - If the problem isn’t solved in 25 minutes, take a look at the discussion section but do NOT look at code just yet
     1. Reset the timer and do another pomodoro
     2. Once the problem is done, look at the discussion section and understand how other people solved it
     3. Write this problem down in your notes as a problem you need to revisit
4. Do the popular “Hard” problems from each topic and try to finish these within 45 minutes
5. Do a mock interview AT LEAST once a week
6. Towards the last month of interview prep, do the 1-month term plan in EPI on PAPER

[Original post from Leetcode](https://leetcode.com/discuss/general-discussion/443629/How-to-Leetcode-Effectively)

#### Some great resources on Leetcode discussion

1. [Finally I Did it.Thanks Leetcode, Love you so much](https://leetcode.com/discuss/interview-experience/469785/Finally-I-Did-it.Thanks-Leetcode-Love-you-so-much-Microsoft-or-Offer)

2. Core 75 Questions: this a list from Blind who is preparing for interview with 500+ Leetcode problem and approved by others. The detail information refer to this [link](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-100-LeetCode-Questions-to-Save-Your-Time-OaM1orEU). There will be a folder contain the code for these questions and explanations.

### 2. [HankRank](https://www.hackerrank.com/)

### 3. [Codility](https://www.codility.com/)

## Object-Oriented Design

1. [SOLID Principle](https://www.youtube.com/watch?v=yxf2spbpTSw)

## System Design

### Resources

1. [Gainlo System Design](http://blog.gainlo.co/index.php/category/system-design-interview-questions/)

### Template

1. FEATURE EXPECTATIONS [5 min]
   - Use cases
   - Scenarios that will not be covered
   - Who will use
   - How many will use
   - Usage patterns

2) ESTIMATIONS [5 min]

   - Throughput (QPS for Read and Write queries)
   - Latency expected from the system (for read and write queries)
   - Read/Write ratio
   - Traffic estimates
     - Write (QPS, Volume of data)
     - Read (QPS, Volume of data)
   - Storage estimates
   - Memory estimates
     - If we are using a cache, what is the kind of data we want to store in the cache
     - How much RAM and how many machines do we need for us to achieve this?
     - Amount of data you want to store in disk/SSD

3) DESIGN GOALS [5 min]

   - Latency and Throughput requirements
   - Consistency vs Availability [Weak/strong/eventual => consistency | Failover/replication => availability]

4) HIGH-LEVEL DESIGN [5-10 min]

   - APIs for Read/Write scenarios for crucial components
   - Database schema \*　 Basic algorithm
   - High-level design for Read/Write scenario

5) DEEP DIVE [15-20 min]

   1. Scaling the algorithm
   2. Scaling individual components:
      Availability, Consistency and Scale story for each component
      Consistency and availability patterns
   3. Think about the following components, how they would fit in and how it would help
      1. DNS
      2. CDN [Push vs Pull]
      3. Load Balancers [Active-Passive, Active-Active, Layer 4, Layer 7]
      4. Reverse Proxy
      5. Application layer scaling [Microservices, Service Discovery]
      6. DB [RDBMS, NoSQL]
         - RDBMS: Master-slave, Master-master, Federation, Sharding, Denormalization, SQL Tuning
         - NoSQL:
           - Key-Value, Wide-Column, Graph, Document
           - Fast-lookups:
             - RAM [Bounded size] => Redis, Memcached
             - AP [Unbounded size] => Cassandra, RIAK,Voldemort
             - CP [Unbounded size] => HBase, MongoDB,Couchbase, DynamoDB
      7. Caches
         - Client caching, CDN caching, Web server caching, Database caching, Application caching, Cache @Query level, Cache @Object level
         - Eviction policies:
           - Least Recently Used(LRU)
           - Least Frequently Used(LFU)
           - First in First Out (FIFO)
         - Cache Loading Policies
           - Cache aside
           - Write through
           - Write behind
           - Refresh ahead
      8. Asynchronism
         - Message queues
         - Task queues
         - Backpressure
      9. Communication
         - TCP
         - UDP
         - REST
         - RPC
         - Thrift
         - GraphQL

6) JUSTIFY [5 min]
   - Throughput of each layer
   - Latency caused between each layer
   - Overall latency justification

[Oringial post from Leetcode](https://leetcode.com/discuss/career/229177/My-System-Design-Template)

## Interview

### Interview Tips

1. After the interviewer gave the question, don’t rush to the solution directly.
   Rushing to the solution is the mistake I made most frequently, even if I knew I should not. Maybe at the beginning of the interview I’m too nervous. So I put this one as the first rule. The interviewer is expecting you to ask questions, to clarify the problem. In this part, they are testing if you have the ability to clarify the problem, and also your communication intention and skill. Remember, you and your interviewer are collaborating now. It’s not your or their own game. By asking questions, you need to try to make yourself have the same understanding of the question (the aim of your function, input/output data type, edge cases needed to consider, etc.).
2. In high level, explain your algorithm first, never jump to code without the interviewer’s agreement.
   In complex questions, think from the brute force solution, and think how to optimal it. IN some cases, the brute force solution is not acceptable by the interviewer, so there is no need to write it out. And also don’t wait for the best solution if you don’t have yet. If you find some workaround in the middle, try to write it out first. It’s always better to have something than have nothing, but remember to get the interviewer’s agreement before writing code.
3. During your implementation, if the interviewer asks you some questions, stop and think about it. I know you want to finish your code, but in most cases, the interviewer is giving you a hint by asking you questions, maybe because they find a bug, and try to help you. Never ignore anything from the interviewer. The key of passing the interview is not about solving the problem perfectly, but is about making the interviewer satisfied and willing to give you hire.
4. Never “argue” about different workaround. The best practice is to write out what’s in the interviewer’s mind. If you have your own workaround, sometimes it’s OK, but you need to convince the interviewer. Remember, be nice. Treat the interviewers as your colleagues.
5. Asking hints directly is not good. You can come up with different solutions and ask for hints implicitly.
6. Never, never, never give up. Even if you don’t know how to solve the problem after maybe 30 minutes, and you have no hope to finish it in the interview, don’t give up. One interviewer told me, in this case, he won’t give hire, but he can also give something as lean hire, which can be balanced with hires in other rounds. So cheer up and leave a good impression.
7. Be a nice person, do good things, help others in your everyday life. And finger crossed, you will be treated nicely in the interviews, you will crack the problems and get HIRE!

[Oringial post from Leetcode](<https://leetcode.com/discuss/career/454990/What-I've-learned-from-tech-interviews-(my-personal-tips)>)

### Practice Interview

- [interviewing.io/](https://interviewing.io/)

## Some great articles in Software engineering

- An analysis of software jobs in Taiwan. [link](https://m.gamer.com.tw/forum/C.php?bsn=60076&page=&snA=5444020&last=)
- The 30-minute guide to rocking your next coding interview. [link](https://www.freecodecamp.org/news/coding-interviews-for-dummies-5e048933b82b/)
- 14 Patterns to Ace Any Coding Interview Question. [link](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)

## Reference

- [Tech Interview Handbook](https://yangshun.github.io/tech-interview-handbook/)
