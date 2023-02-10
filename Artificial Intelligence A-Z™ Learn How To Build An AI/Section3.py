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
    
'''