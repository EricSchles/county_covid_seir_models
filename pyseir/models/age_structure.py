import re
import os
import yaml
import pandas as pd
from pyper import *
from string import Template

THIS_FILE_PATH = os.path.dirname(os.path.realpath('__file__'))

def get_age_distribution():
    return None

def get_risk_profile_by_age():
    return None


def extract_contact_matrices(config):
    """

    """

    r_script_path = config['contact_matrices_r_script_path']
    r_script = Template(open(r_script_path, 'r').read()).substitute(config['r_substitution'])
    r = R()
    r.run(r_script)
    age_groups = r.m['participants']['age.group'].apply(lambda x: int(re.sub("[b'[)+]", '', str(x)) \
                                                                      .split(',')[0])).values
    contact_preferences = r.mr
    # contact_matrix = r.d * r.n * r.a
    return age_groups, contact_preferences
