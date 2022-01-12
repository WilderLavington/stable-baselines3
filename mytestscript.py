from stable_baselines3.fkl import FKL
import gym
model = FKL('MlpPolicy', gym.make('Hopper-v2'), verbose=1)
model.learn(total_timesteps=50000)
