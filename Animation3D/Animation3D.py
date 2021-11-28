import numpy as np
from .AnimationJoint import AnimationJoint
from .AnimationLimb import AnimationLimb
from .view_matrix_3d import view_matrix_3d


class Animation3D:
    def __init__(self,
                 _ax,
                 _plt_type='3D',
                 _view_angle=(0, 90)):
        self.joints = []
        self.limbs = []
        self.plt_ax = _ax
        self.plt_type = _plt_type
        self.view_angle = _view_angle
        self.view_matrix = view_matrix_3d(self.view_angle[0], self.view_angle[1])

        self.n_frames, self.n_joints = None, None

    @property
    def plt_type(self):
        return self._plt_type

    @plt_type.setter
    def plt_type(self, value):
        if (value == '2D') | (value == '3D'):
            self._plt_type = value
        else:
            raise ValueError("plot type has to be either 2D or 3D!")

    def set_joints(self, data):
        shape = data.shape
        if len(shape) == 3:
            n_frames, n_joints, _ = shape
        elif len(shape) == 2:
            data = np.expand_dims(data, axis=1)
            n_frames, n_joints, _ = data.shape
        else:
            raise ValueError("The added joints have to either be a 3D or a 2D matrix!")

        if not self.joints:  # first time setting the joints
            self.n_frames, self.n_joints = n_frames, n_joints
        else:
            if n_frames != self.n_frames:  # need to check for dimensions if not the first time setting joints
                raise ValueError("The added joints have to have the same number of frames as the original data!")
            self.n_joints += n_joints

        for i_joint in range(n_joints):
            x = np.squeeze(data[:, i_joint, 0])
            y = np.squeeze(data[:, i_joint, 1])
            z = np.squeeze(data[:, i_joint, 2])

            j = AnimationJoint(_ax=self.plt_ax, _plt_type=self.plt_type, _view_matrix=self.view_matrix)
            j.from_vectors(x, y, z)
            self.joints.append(j)
        return self.n_joints - 1  # return the last added joint index

    def set_limbs(self, _connections):
        shape = _connections.shape

        if len(shape) != 2:
            raise ValueError("connections have to be a 2d matrix!")
        r, c = shape
        if c != 2:
            _connections = _connections.swapaxes(0, 1)

        for c in _connections:
            limb = AnimationLimb(_ax=self.plt_ax, _plt_type=self.plt_type, _view_matrix=self.view_matrix)
            limb.set_joints(self.joints[c[0]], self.joints[c[1]])
            self.limbs.append(limb)

    def update_animation(self, frame):
        draw_object = [j.update_draw(frame) for j in self.joints] + [l.update_draw(frame) for l in self.limbs]
        return draw_object
