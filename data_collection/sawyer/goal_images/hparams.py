""" Hyperparameters for Large Scale Data Collection (LSDC) """

import os.path
from visual_foresight.policy.policy import NullPolicy
from visual_foresight.agent.general_agent import GeneralAgent
from visual_foresight.envs.robot_envs.autograsp_env import AutograspEnv
from visual_foresight.envs.robot_envs.util.topic_utils import IMTopic

BASE_DIR = '/'.join(str.split(__file__, '/')[:-1])
current_dir = os.path.dirname(os.path.realpath(__file__))


env_params = {
    'camera_topics': [IMTopic('/front/image_raw', flip=True)],
    'start_at_neutral': True,
    'rand_drop_reset': False
}


agent = {
    'type': GeneralAgent,
    'env': (AutograspEnv, env_params),
    'data_save_dir': BASE_DIR,
    'T': 2,
    'image_height' : 240,
    'image_width' : 320,
    'record': BASE_DIR + '/record/',
}


policy = {
    'type': NullPolicy,
    'wait_for_user': True
}


config = {
    'traj_per_file':128,
    'current_dir' : current_dir,
    'save_data': True,
    'save_raw_images': True,
    'start_index':0,
    'end_index': 120000,
    'agent': agent,
    'policy': policy,
    'ngroup': 1000
}
