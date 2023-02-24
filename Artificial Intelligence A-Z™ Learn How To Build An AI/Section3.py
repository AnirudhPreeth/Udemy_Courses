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
P -> Probability. 
γV(s’) -> Deterministic Search, you know which state you will get into. 
γ Σ_s’ P(s,a,s’)V(s’)) -> Non-Deterministic Search, you don't know which state you will get into. 
V(s)=max_a(R(s,a)+ γ Σ_s’ P(s,a,s’)V(s’)) -> New Bellman Equation. 
Paper -> A Survey of Applications of Markov Decision Processes - DJ White (1993). 

Policy VS Plan ->
V(s)=max_a(R(s,a)+ γ Σ_s’ P(s,a,s’)V(s’)) 
Not a full 100% so its not a 1. 
Some states which may have been equal are now radically different. Due to not a full 100%.
policy will be defined by a set of pair "state -> action" which should allow from any reachable state.
plan will be a a strictly defined sequence of actions leading from the initial state to the goal. 
Can be more complex than that if you have concurrency. 
Planning involves the unrolling of a policy through time, and refining the policy based on the resulting trajectory . 
policy is a description of how an agent behaves in an environment and is represented as the probability of performing each action...
...for a given state.

Adding a "Living Penalty" ->
Rewards in ever tile. R=-0.04. No matter where he goes he will get negative penalty. Hence, it is living penalty. 
Even in starting state, there is R=-0.04, but he only gets a reward when he enters the tile. 
"Optimal Policy". Results will be different as according to the reward value. Depending upon the environment as well. 

Q-Learning Intuition ->
V(s)=max_a(R(s,a)+ γ Σ_s’ P(s,a,s’)V(s’)) 
Where's the Q? Q represents quality, quality of the action. Which action is more lucrative? (Because actions lead to states).
Q(s,a) -> Q is of the state s and action a. We perform action in state s. 
V(s) ->  maximum of all the possible actions (reward).  
Q is a recursive function of V. 
Q(s,a) = R(s,a)+ γ Σ_s’ (P(s,a,s’) V(s’))
Bellman Equation for Q values - Q(s,a) = R(s,a)+ γ Σ_s’ (P(s,a,s’) max_a Q(s’,a’)) 
They don't look at the states, they look at the action. 

Temporal Difference ->
Heart and Soul of Q-Learning Algorithm.  
Recursion is not deterministic. Subject to chance.
Q(s,a) = R(s,a)+ γ Σ max_a Q(s’, a’)
Before => Q(s,a), After => R(s,a) +γ max_a Q(s’, a’)
TD(a,s) = R(s,a)+ γ max_a Q(s’, a’) - Q(s,a)
Difference is time. 
Q(s,a) = Q(s,a) + αTD(a,s) 
Adding time, 
Q_t-1(s,a) = Q_t-1(s,a) + αTD_t(α,s) - Heart and soul of Q-learning algorithm. 
Q_t(s,a) = Q_t-1(s,a) + αTD_t(α,s) 
Q_t(s,a) = Q_t-1(s,a) + α(R(s,a)+ γ max_a’ Q(s’, a’) - Q_t-1(s,a)) - Full Equation. 
Environment is continuously changing. 

Now let's recap what is going on in terms of MDPs. At every time t:
1. The AI observes the current state st.
2. The AI plays the action at.
3. The AI receives reward rt = R(at, st).
4. The AI enters the following state st+1.
'''

#That's the end of this section. 