from scipy.spatial.transform import Rotation as R
import sys
import numpy as np
import pandas as pd

def quat2angle(quat):
    r = R.from_quat(quat)
    return r.as_euler('xyz', degrees=True)

#q = [0.552, 0.501, 0.487, 0.455]
#e = quat2angle(q)

#print(e)

input = sys.argv[1]

df = pd.read_excel(input)

roll = []
pitch = []
yaw = []

for i in range(0, len(df)):
    q = [df['qx'][i], df['qy'][i], df['qz'][i], df['qr'][i]]
    e = quat2angle(q)
    roll.append(e[0])
    pitch.append(e[1])
    yaw.append(e[2])

df['roll'] = roll
df['pitch'] = pitch
df['yaw'] = yaw

df.to_excel('{0}_euler.xlsx'.format(input[:-4]), index=False)