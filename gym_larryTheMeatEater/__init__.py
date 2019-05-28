from gym.envs.registration import register

register(
    id='larryTheMeatEater-v0',
    entry_point='larryTheMeatEater.envs:larryTheMeatEater_env',
)