#Section 3. 

#Q Learning Intuition. 

'''
Reinforcement Learning.  Bellman Equation. Markov Decision Process (MDP). Adding a "Living Penalty".
Q-Learning Intuition. Temporal Difference. 

Reinforcement Learning -> 
Maze - Representation of our environment. Agent - AI. 
Agent performs actions on environment, state it is in might change.  
Will get rewards based on actions. By doing this it will learn about the environment.  
Which actions will lead to god rewards and which actions will lead to favorable states. 
An environment can be anything. 
Simplest way of thinking of reinforcement learning - Training a dog. 
Reinforcement Learning algorithm. 

We are using Pytorch. 
"Reinforcement Learning 1: Introduction." - Richard sutton et al. (1998).

Bellman Equation -> 
s-State, a-Action, R-Reward, γ-Discount. V-Value.
Richard Ernest Bellman. 1953.     
4*3 Maze. Flag in the right hand corner. Fire pit below it. Gray block in second row second column.  
Agent in the bottom left corner. Grey block is not accessible. 
Fire pit is R =-1. Green flag is R=+1. Up, down, left, right movements. 
"How did I get to the green square?" All sorts of questions. 
White Square is V=1. (Left to green square). And others as well. 
Look at reward then preceding state, and preceding state after that and so on. 
It doesn't really work though. If it is between the values, it can confused on where to go and so on. 
Here is where we introduce the Bellman Equation. 
V(s)=max_a(R(s,a)+ γV(s’))
The discounted factor works is it discounts the value of the state as you are further away. 

The "Plan" ->
Like a treasure map. Instead of values, it's like arrows for the agent.
Plan is not policy. Their environment is different. 

Markov Decision Process (MDP) ->
Deterministic Search vs Non-Deterministic Search.      
Deterministic Search means that 100% chance, it will do that option. 
Non-Deterministic Search means, not fully 100%. Many scenarios. 
Randomness to it. 
Markov Process - A stochastic process has the Markov Property if conditional probability distribution of future states of process...
...(conditional on both past and present states) depends only upon the present state, not on the sequence of events that preceded it. 
Process with this property is Markov process.
Only depend on where you are now. Not how you got there. 
Markov Decision Process (MDPs) - Provide mathematical framework for modelling decision making in situations where outcomes are partly...
...random and partly under the control of a decision maker. 
In order to make a decision, it applies the Markov Decision Process. 
MDP is just an add on to the Bellman Equation. 
V(s)=max_a(R(s,a)+ γV(s’)) -> 0.8*V(s’1) + 0.1*V(s’2) + 0.1*V(s’3) (example). 
V(s)=max_a(R(s,a)+ γ Σ_s’ P(s,a,s’)V(s’))
γV(s’) -> Deterministic Search, you know which state you will get into. 
γ Σ_s’ P(s,a,s’)V(s’)) -> Non-Deterministic Search, you don't know which state you will get into. 
V(s)=max_a(R(s,a)+ γ Σ_s’ P(s,a,s’)V(s’)) -> New Bellman Equation. 
Paper -> A Survey of Applications of Markov Decision Processes - DJ White (1993). 

Policy VS Plan ->
V(s)=max_a(R(s,a)+ γ Σ_s’ P(s,a,s’)V(s’)) 

'''