*Systems, Design, and Communication

#Two types of design interviews
1. System Design ex) Desgin Twitter

a. Make the problems more well defined
  (Users First)
  1. clairfy the scope, only core features? ex) follow or browse feed?
  2. what can the agents do, find follow, etc
  3. what are the limits on these agents


b.Think through the high level components for the system
  Think in terms of layers
  1. Presentation Layer
    a. UI components
    b. UI process Components
  2. Business Layer
    a. Workflow
    b. Components
    c. Entities
  3. Data Layer
    a. Access Componenets
    b. Helpers Utilies
    c. Service Agents

  This Translate into this
  (Tools for the Jobs) - Weigh all pros and cons and then decide
  (Three main topics to hit one)
  1. How to models relationships in the system, database
    *Model for Authors, Model for books, Each Author has many books
    *Belongs to, has_one,  has_many, has an belongs to many

  2. How to Store, Process, Serve Information (Backend System)
    -Caching
    -Monitoring
    -Lock things down
    -Clearly defined inputs and outputs

  3. How to display and interact with the user (Front End System)
    -Degredation vs enchancement
    -Authentication
    -Form and Feeds

  #How each system will communicate with each other?
  #State full or stateless, guest user is stateless while login has state

  *How to parition the applicaiton logically
    -Maintainability,
    -Modularize, monitor, and optimize separately
    -scaling the application
  1. Frontend talking straight to datastore
  2. Frontend and backend talking to data store
  3. Frontend to backend to data store
  4. Dataflow is one directional, 2 way, or multi-directional?

  # What are the functionality, try to break down and modularize as much as possible, to call
  # the same things over again
  1.
  2.
  3.

Think about the request flow, add things to a process queue, only way limit the overload
c. Become Specific on the high level components
  1. Database Technologies
    -Relational v Nonrelation
    -Cloud v non Cloud
    -Data Structures to Store

  2. Backend Technologies

  3. Frontend Technologies
    -Unidirectional
    -Two way
    -Multi directional

  #Asynch computation not tied to a request is bad, asynch to notify the error is to write into the db

  #Other things
  *What are good mechanisms to carry outs tasks, (a que to publish to 3rd parties?)
  *is a cache needed, what would it store, what to evict
  *security of the system, validation and points to entry
  *DataStorage, deliverance, scalability

d. More in detail specific questions
  a. How to reduce costliness of lots of people getching and rendering their feeds
    #pagination, fetch most recent n - feeds
  b. Caching?
  c. How to detect fake users
  d. can we order feed by other algorithms
  e. How to implement the @feature, or retweet feature
    -When rendering your feeds, include feeds that have your IDs in @list

  Application flow
  #Security/Authentication/Authentication
  1. What is the trust boundary
  2. What

  #Optomize for high throughput, vs easy to track, queue technology

  #Caching
    -Reused frontend stuff should be stored in a cache
    -



  #Exception Management and stress testing
    -Consumer dies, key expires, que job fails
    -need to process in the que, how to pass it in a timeout, rest flow
    -server fails
    1. What happens when the server crashes,
    2. How does the front end know, if its setting the state, *is reprocessing the solution
    3. Server will restart - if its a cluster you cannot find all active processes

  #Logging and instrumentation

  #Navigation

  #Page Layout/Rendering/Session Management

  #Validation

  #Deployment Concerns
  -Non distributed vs distributed deployment
  -Load Balancing
  #Optimize for durability and consistency

2. Class Design (How would you represent a football tournament in CS)
  1. Clairfy how the this class proceeds, what does it do?

  2. Create the classes -  what are the major entiies, that will be a class of their own
    ex) matches, quarters, semis, palyer, refs, cheers, presenter
    Matches have - venues, teams, results, players with red, goals, time tracker

  3. Pick the major classes, start defining methods
    getStats, calculateStats() for match, create schedule
    think about the best data structures, to be used inside the classes
    polymorphism implementation, extensibility, correct represention, not for scale

