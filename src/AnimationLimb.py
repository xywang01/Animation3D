import numpy as np


class AnimationLimb:
    def __init__(self,
                 _ax,
                 _view_matrix,
                 _plt_type='3D'):
        self.plt_ax = _ax
        self.view_matrix = _view_matrix
        self.plt_type = _plt_type

        self.joint1, self.joint2 = None, None
        self.draw_object = None

    def set_joints(self, joint1, joint2):
        self.joint1 = joint1
        self.joint2 = joint2
        self.init_draw()

    def init_draw(self):
        if self.plt_type == '3D':
            self.draw_object = self.plt_ax.plot(
                [self.joint1.x[0], self.joint2.x[0]],
                [self.joint1.y[0], self.joint2.y[0]],
                [self.joint1.z[0], self.joint2.z[0]],
                linewidth=2)[0]
        else:
            self.draw_object = self.plt_ax.plot(
                [self.joint1.x_2d[0], self.joint2.x_2d[0]],
                [self.joint1.y_2d[0], self.joint2.y_2d[0]],
                linewidth=2)[0]

    def update_draw(self, frame):
        if self.plt_type == '3D':
            self.draw_object.set_data(
                np.asarray([self.joint1.x[frame], self.joint2.x[frame]]),
                np.asarray([self.joint1.y[frame], self.joint2.y[frame]]),
            )
            self.draw_object.set_3d_properties([(self.joint1.z[frame]),
                                               self.joint2.z[frame]])
        else:
            self.draw_object.set_data(
                [self.joint1.x_2d[frame], self.joint2.x_2d[frame]],
                [self.joint1.y_2d[frame], self.joint2.y_2d[frame]],
            )
        return self.draw_object
