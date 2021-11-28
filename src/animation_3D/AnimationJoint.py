import numpy as np


class AnimationJoint:
    def __init__(self,
                 _ax,
                 _view_matrix,
                 _plt_type='3D'):
        self.plt_ax = _ax
        self.view_matrix = _view_matrix
        self.plt_type = _plt_type

        self.x, self.y, self.z = None, None, None
        self.x_2d, self.y_2d = None, None
        self.draw_object = None

    def from_vectors(self, x, y, z):
        if len(x.shape) > 1:
            raise ValueError("x should be a 1 dimension vector!")

        if len(y.shape) > 1:
            raise ValueError("y should be a 1 dimension vector!")

        if len(z.shape) > 1:
            raise ValueError("z should be a 1 dimension vector!")

        self.x = x
        self.y = y
        self.z = z
        self.x_2d, self.y_2d = np.apply_along_axis(self.proj_frame, 0, np.vstack([self.x, self.y, self.z]))
        self.init_draw()

    def proj_frame(self, _single_frame):
        # the viewing_matrix_3d that I use here, which was borrowed from matlab's viewmtx, considers the z axis as
        # the vertical axis. The azimuth and elevation was defined based on this coordinate system. However, since I
        # use y as the vertical axis, I will need to swap y and z first and swap them back after the projection.
        x, y, z = _single_frame
        _single_frame_2d = np.dot(np.array([x, z, y, 1]), self.view_matrix)

        # swap the axis back
        _single_frame_2d = _single_frame_2d[[0, 2, 1, 3]]

        return _single_frame_2d[0], _single_frame_2d[1]

    def init_draw(self):
        if self.plt_type == '3D':
            self.draw_object = self.plt_ax.plot(self.x[0], self.y[0], self.z[0], 'o', markersize=3)[0]
        else:
            self.draw_object = self.plt_ax.plot(self.x_2d[0], self.y_2d[0], 'o', markersize=3)[0]

    def update_draw(self, frame):
        if self.plt_type == '3D':
            self.draw_object.set_data(self.x[frame], self.y[frame])
            self.draw_object.set_3d_properties(self.z[frame])
        else:
            self.draw_object.set_data(self.x_2d[frame], self.y_2d[frame])
        return self.draw_object
