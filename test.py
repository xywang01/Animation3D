import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation
import mpl_toolkits.mplot3d.axes3d as p3
from Animation3D.Animation3D import Animation3D

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    POSE_CONNECTIONS = np.array([(0, 1), (1, 2), (2, 3), (3, 7), (0, 4), (4, 5),
                                 (5, 6), (6, 8), (9, 10), (11, 12), (11, 13),
                                 (13, 15), (15, 17), (15, 19), (15, 21), (17, 19),
                                 (12, 14), (14, 16), (16, 18), (16, 20), (16, 22),
                                 (18, 20), (11, 23), (12, 24), (23, 24), (23, 25),
                                 (24, 26), (25, 27), (26, 28), (27, 29), (28, 30),
                                 (29, 31), (30, 32), (27, 31), (28, 32)])

    movement = np.genfromtxt('./movement_test.csv', delimiter=',', skip_header=True)[:, 1:]
    movement_3d = np.reshape(movement, (movement.shape[0], -1, 4))
    movement_3d = movement_3d[:, :, :3]

    mpl.use('TkAgg')

    # plt_type = '2D'
    plt_type = '3D'

    if plt_type == '3D':
        fig = plt.figure()
        ax = p3.Axes3D(fig, azim=0, elev=0, auto_add_to_figure=False)
        fig.add_axes(ax)
    else:
        fig, ax = plt.subplots()

    actor = Animation3D(ax, _plt_type=plt_type, _view_angle=(0, 90))
    actor.set_joints(movement_3d)
    actor.set_limbs(POSE_CONNECTIONS)

    frame_interval = 1 / 20
    anim = animation.FuncAnimation(fig, actor.update_animation,
                                   frames=actor.n_frames, interval=frame_interval, blit=False)
    plt.show()

